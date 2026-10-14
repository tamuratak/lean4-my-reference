# タスク・スレッドと共有状態の同期

Lean は、`Task α` で表した計算を OS のスレッドに割り当てて、並列・並行に実行できる。通常の値は不変な値として共有でき、共有する可変状態には `IO.Ref` や `Std.Mutex` を使う。メモリの寿命は参照カウントで管理し、複数の操作をまとめて保護する範囲はプログラマーが指定する。

## タスクとスレッドプール

`Task α` は、完了すると `α` 型の結果が得られる計算を表す。ランタイムは通常、スレッドプールのワーカースレッドでタスクを実行する。タスクごとに専用の OS スレッドが一つ作られるわけではない。

| 操作 | 用途 |
| --- | --- |
| `Task.spawn (fun () => 計算)` | 純粋な計算のタスクの作成 |
| `IO.asTask action` | `IO` の副作用を含むタスクの作成 |
| `task.get` | 完了を待って結果を取得 |
| `task.map f`・`task.bind f` | 先行タスクの結果に依存する計算の組み立て |

スレッドプールのサイズは環境変数 `LEAN_NUM_THREADS` で指定でき、未指定なら論理プロセッサ数が基準になる。タスクの結果を待つ際のプール枯渇によるデッドロックを避けるため、一時的にスレッド数が増える場合がある。専用スレッドが必要な処理には、タスク作成時の `prio := Task.Priority.dedicated` を指定できる。

### 純粋な計算の並列実行

`Task.spawn` は `Unit → α` の関数を受け取り、関数本体を非同期に評価するタスクを作る。次の `sumParts` は、二つの部分和をタスクとして作り、両方の結果を加える。

```lean
import Init

def sumParts (xs ys : List Nat) : Nat :=
  let a := Task.spawn (fun () => xs.foldl (· + ·) 0)
  let b := Task.spawn (fun () => ys.foldl (· + ·) 0)
  a.get + b.get

#eval sumParts [1, 2, 3] [4, 5, 6]
```

結果は `21` になる。`get` は未完了なら呼び出し元のスレッドを待機させ、完了済みなら保存された結果を返す。実際に二つの計算が同時に走るかはスケジューリングによる。小さな計算では、タスク作成のコストが並列化の利点を上回ることもある。

後続の計算が先行タスクに依存する場合は、`map` や `bind` を使うと、後続タスクの中で `get` によって待機する必要を減らせる。必要になるまで計算を遅らせる [`Thunk`](../basic-types/thunk.md) と異なり、`Task.spawn` は結果の要求より先に計算を進められる。

### `IO` のタスクと例外

`IO.asTask` は、渡した `IO` アクションを別のタスクで実行する。結果の型は `Task (Except IO.Error α)` であり、成功時の値と例外を区別して受け取る。

```lean
import Init

def taskResult : IO Nat := do
  let task ← IO.asTask (pure (20 + 22) : IO Nat)
  IO.ofExcept task.get

#eval taskResult
```

結果は `42` になる。`IO.ofExcept` は成功なら値を返し、エラーなら呼び出し元の `IO` で例外を投げる。`IO.asTask` は `IO` アクションを実行した時点でタスクを作成するため、`←` で実行してタスクを受け取る。

`IO` のタスクは、最後の参照を手放しただけでは実行を停止しない。中止に対応する長時間の処理では、タスク側で `IO.checkCanceled` を確認する必要がある。

参照：[公式リファレンス：タスクとスレッド](https://lean-lang.org/doc/reference/latest/IO/Tasks-and-Threads/)、[公式 API：`IO.asTask`](https://lean-lang.org/doc/api/Init/System/IO.html#IO.asTask)。

## 不変な値の共有と参照カウント

Lean の [`List`](../basic-types/list.md#変換結果と元のリスト) や [`Array`](../basic-types/array.md#更新結果と元の配列) は、不変な値として複数のタスクで共有できる。一方のタスクが更新結果を作っても、他方が持つ元の値は変わらない。内部の更新やメモリ再利用の条件は、[参照カウントとメモリ再利用](native_compilation.md#参照カウントとメモリ再利用)を参照。

タスク間で変更を共有する場合には、`IO.Ref` などの可変セルを使う。[`let mut`](../syntax/do_control.md#局所変数の再代入と元の値) は局所変数への再代入の構文であり、共有する可変セルを作る指定ではない。

Lean は単一スレッド用と複数スレッドから到達可能なオブジェクトを区別し、複数スレッド用では参照カウントの更新を同期する。通常のタスク API を使う際に、プログラマーが参照カウントを手動で増減する必要はない。

参照カウントの同期が守るのはオブジェクトの寿命である。共有カウンターの更新の取りこぼしや、複数の値の整合性を守るには、操作そのものの同期が必要になる。

参照：[公式リファレンス：参照カウント](https://lean-lang.org/doc/reference/latest/Run-Time-Code/Reference-Counting/)。

## `IO.Ref` とアトミックな更新

`IO.Ref α` は、`α` 型の値を読み書きできる可変セルへの参照である。`IO.mkRef` で作成し、`get` で読み出し、`set` で置き換える。同じ参照を複数のタスクに渡すと、同じセルへの書き込みが共有される。

### 読み出しと書き込みの間の競合

次の `increment` は、セルの値を読み、1 を加えて書き戻す。単独の実行なら一回の加算になる。

```lean
import Init

def increment (r : IO.Ref Nat) : IO Unit := do
  let n ← r.get
  r.set (n + 1)
```

ただし、同じセルに二つのタスクが `increment` を実行すると、両方が同じ古い値を読む場合がある。

| 順番 | タスク A | タスク B |
| --- | --- | --- |
| 1 | `0` を読む | |
| 2 | | `0` を読む |
| 3 | `1` を書く | |
| 4 | | `1` を書く |

最終値は、期待した `2` ではなく `1` になる。各 `get`・`set` はスレッド間のアクセスに対応しているが、読み出しと書き込みの組全体は不可分にならない。Lean は上のコードをコンパイル時には拒否しない。

### `modify` による更新の一体化

`r.modify f` は、セルの現在値に純粋な関数 `f` を適用し、結果を書き戻すまでをアトミックに実行する。アトミックな更新では、同じセルに対する他の読み書きが途中に割り込まない。

```lean
import Init

def countTasks : IO Nat := do
  let counter ← IO.mkRef (0 : Nat)
  let a ← IO.asTask (counter.modify (fun n => n + 1))
  let b ← IO.asTask (counter.modify (fun n => n + 1))
  IO.ofExcept a.get
  IO.ofExcept b.get
  counter.get

#eval countTasks
```

両方の完了後に値を読むので、結果は `2` になる。`modifyGet` は、セルの新しい値と呼び出し元への返り値を同時に計算する場合に使う。`swap` は新しい値への置き換えと古い値の取得をアトミックに行う。

`modify` の引数は純粋な関数であり、更新中に任意の `IO` アクションを実行する用途には使えない。また、複数のセルをそれぞれ `modify` しても、複数セルの更新全体が不可分になるわけではない。

参照：[公式リファレンス：可変参照](https://lean-lang.org/doc/reference/latest/IO/Mutable-References/)、[公式 API：`modify`](https://lean-lang.org/doc/api/Init/System/ST.html#ST.Ref.modify)、[`modifyGet`](https://lean-lang.org/doc/api/Init/System/ST.html#ST.Ref.modifyGet)、[`swap`](https://lean-lang.org/doc/api/Init/System/ST.html#ST.Ref.swap)。

## Mutex による共有状態の排他制御

`Std.Mutex α` は、共有状態 `α` と、その状態を保護するロックをまとめた型である。`atomically` はロックを取得して処理を実行し、正常終了時にも例外時にもロックを解放する。処理中の `get`・`set` は、Mutex 内部の状態を読み書きする。

```lean
import Std.Sync.Mutex

def countWithMutex : IO Nat := do
  let counter ← Std.Mutex.new (0 : Nat)
  let increment : IO Unit := counter.atomically do
    let n ← get
    set (n + 1)
  let a ← IO.asTask increment
  let b ← IO.asTask increment
  IO.ofExcept a.get
  IO.ofExcept b.get
  counter.atomically do get

#eval countWithMutex
```

結果は `2` になる。同じ Mutex を使う二つの `atomically` は、同時にロックを保持できないため、読み出しから書き戻しまでを一つの処理として保護できる。複数の値の整合性を守る場合は、値を構造体などにまとめて一つの Mutex の状態にするとよい。`atomically` 内では `IO` も実行できるが、長い処理を行うと、同じロックを必要とする他のタスクを待たせる。

### 保護範囲とロックの注意点

Mutex の排他制御は、同じロックを使う処理間で働く。たとえば、外部でも共有している `IO.Ref` を Mutex の中に入れても、外部からその参照を直接更新する処理まで同じロックに従わせることはできない。

複数のロックの取得順によるデッドロックなどは、プログラマーが避ける必要がある。また、通常の `Mutex` のロックを保持しているスレッドが、解放せずに再度ロックすることは未定義動作である。ロック中に同じ Mutex の `atomically` を呼ぶ構造を避け、再入が必要なら `Std.RecursiveMutex` を検討する。

参照：[公式 API：`Std.Mutex`](https://lean-lang.org/doc/api/Std/Sync/Mutex.html)、[`Std.RecursiveMutex`](https://lean-lang.org/doc/api/Std/Sync/RecursiveMutex.html)。

## チャネルによるタスク間通信

`Std.Channel α` は、タスク間で `α` 型の値を送受信するための FIFO チャネルである。共有する状態を複数のタスクから直接更新する代わりに、更新を担当するタスクへ要求をメッセージとして送る設計にも使える。

参照：[公式 API：`Std.Channel`](https://lean-lang.org/doc/api/Std/Sync/Channel.html)。

## Rust の所有権・借用との対応

Rust は、所有権と借用規則に加え、スレッド間の移動・共有を制約する `Send`・`Sync` によって、安全なコードでのデータ競合を防ぐ。Lean は不変な値の共有を基本とし、参照カウントと同期用 API の実装によってメモリや共有セルを扱う。

| 観点 | Rust | Lean |
| --- | --- | --- |
| 値の寿命 | 所有権・借用規則。共有所有には `Rc`・`Arc` など | 参照カウントによる自動管理 |
| スレッド間の移動・共有 | `Send`・`Sync` の制約を静的に検査 | 通常のタスク API に同種の型クラス制約はない |
| 共有する可変状態 | `Mutex`・アトミック操作など | `IO.Ref.modify`・`Std.Mutex` など |
| 複数操作の整合性 | 必要な範囲を同期する設計が必要 | 必要な範囲を同期する設計が必要 |

Rust でも、別々にロックした読み出しと書き込みの間で他のタスクが更新すれば、論理的な競合は起こり得る。メモリ上のデータ競合の防止と、「残高確認と引き落としをひとまとまりにする」といった処理全体の整合性は区別する必要がある。

Lean のコンパイラにも、[参照カウント操作を減らす借用の推論](native_compilation.md#参照カウントとメモリ再利用)がある。借用の推論は最適化のための仕組みであり、Rust の借用チェッカーのように共有可変アクセスを利用者のコードに対する規則として検査するものではない。上の `get` と `set` による加算も、型検査を通るため、プログラマーが `modify` や Mutex で同期範囲を指定する。

`unsafe` な処理や FFI で独自の可変データを扱う場合は、通常の値や標準 API の保護だけで安全性が保証されるとは限らない。外部コード側でも、寿命とスレッド間アクセスの契約を守る必要がある。[C 関数のバインディング](c_bindings.md)も参照。

[リファレンスの概要に戻る](../../README.md)
