# `do` 内の `let mut`・`for`・`while`

`do` の中では、局所変数を更新しながら、要素や条件に応じて処理を繰り返すことができる。

`let mut` は更新できる局所変数を作る。後続の `x := …` はその変数に新しい値を代入する。

```lean
def total (xs : List Nat) : Nat := Id.run do
  let mut sum := 0
  for x in xs do
    sum := sum + x
  return sum

#eval total [1, 2, 3]
```

出力は `6` である。`for x in xs do …` はリストの要素を順に `x` と呼び、ループの本体を実行する。

`Id.run do …` は、`IO` のような外部への作用を伴わず、この構文で組み立てた計算から通常の値を取り出す書き方である。`mut` はその局所変数を更新可能にする指定であり、元のリストを変更する指定ではない。

`continue` は現在の一回の残りを飛ばし、次の要素へ進む。`break` は現在のループを終える。

```lean
def collect (xs : List Nat) : List Nat := Id.run do
  let mut result := []
  for x in xs do
    if x == 0 then
      continue
    if x > 5 then
      break
    result := result ++ [x]
  return result

#eval collect [1, 0, 2, 8, 3]
```

出力は `[1, 2]` である。`0` は飛ばし、`8` に達した時点でループを終えるので、後ろの `3` は処理しない。`do` の途中の `if` は、何もしない側の `else` を省略できる。

`while 条件 do …` は、条件が成り立つ間、同じ本体を繰り返す。

```lean
def halveDown (n : Nat) : Nat := Id.run do
  let mut current := n
  let mut steps := 0
  while current > 0 do
    current := current / 2
    steps := steps + 1
  return steps

#eval halveDown 8
```

出力は `4` である。`current` は `8 → 4 → 2 → 1 → 0` と変わり、条件が偽になったところで終わる。

`break` はループの後の処理へ進む。`return` は、それを囲む `do` の計算から結果を返すので、使う位置によってはループの後の処理も行わず終了する。入れ子のループで `break`・`continue` を使うと、最も内側のループが対象になる。

## 局所変数の再代入と元の値

`let mut` で作った局所変数には、計算の途中で新しい値を代入できる。配列を代入した場合も、変数が指す値を更新する操作として扱う。

```lean
import Init

def appendThree (xs : Array Nat) : Array Nat × Array Nat := Id.run do
  let mut ys := xs
  ys := ys.push 3
  return (xs, ys)

#eval appendThree #[1, 2]
```

結果は `(#[1, 2], #[1, 2, 3])` になる。`ys := ys.push 3` は、追加後の配列を局所変数 `ys` に代入する。引数 `xs` の値は変わらない。`ys` に最初に `xs` を代入していても、再代入によって `xs` まで書き換わることはない。

`let mut` は、複数の場所から変更を共有する可変セルを作る指定ではない。共有する可変状態が必要な場合は、[`IO.Ref` など](../compiler/tasks_threads.md#ioref-とアトミックな更新)を使う。配列の内部でメモリを直接更新できる条件は、[配列の直接更新と作業バッファ](../compiler/native_compilation.md#配列の直接更新と作業バッファ)を参照。

基本的な計算のつなぎ方と `←` は [`do`](do.md) を参照。

参照：[公式リファレンス：Syntax / do-Notation](https://lean-lang.org/doc/reference/latest/Functors___-Monads-and--do--Notation/Syntax/)。

[文法要素の一覧に戻る](README.md)
