# C 関数のバインディング

Lean の FFI（Foreign Function Interface）は、C の呼び出し規約を使って外部の関数を呼び出す仕組みである。Lean 側に関数の型と `@[extern "シンボル名"]` を宣言し、対応する C 関数を実行ファイルにリンクすると、Lean の通常の関数呼び出しとして利用できる。
また Lean で定義した関数へ `@[export シンボル名]` を付けて公開し、C から呼び出すこともできる。

C 側で定義した構造体やオブジェクトも、そのポインターを Lean の外部オブジェクト（`lean_alloc_external`）で包み、Lean 側では不透明な型の値として受け取る形で返せる。ただし、C の `struct` を値のまま直接返すことはできず、内容の操作やメモリの解放は C 側のバインディングで扱う。

## 固定幅整数と文字列の具体例

次のプロジェクトは、C で二つの整数を加算し、C の `puts` で文字列を出力する。`cAdd` は純粋な計算、`cPrint` は外部への出力を伴う `IO` の処理として宣言する。

```text
c-binding-demo/
  lean-toolchain
  lakefile.lean
  Main.lean
  bindings.c
```

`lean-toolchain` の内容は次のとおり。

```text
leanprover/lean4:v4.35.0-rc3
```

### Lean 側の例

`Main.lean` は、C のシンボル `ref_c_add` と `ref_c_print` に対応する Lean 関数を宣言する。`opaque` によって Lean 側の関数本体を与えず、実行時の実装を外部関数に任せる。

```lean
import Init

@[extern "ref_c_add"] opaque cAdd (a b : UInt32) : UInt32
@[extern "ref_c_print"] opaque cPrint (s : @& String) : IO Unit

def main : IO Unit := do
  IO.println (cAdd 20 22)
  cPrint "Hello from C"
```

`@& String` は、C 側が文字列を借用することを示す。`cPrint` は文字列を読み取り、引数の参照カウントを減らさずに返る。

### C 側の例

`bindings.c` では、Lean 側で指定した名前を持つ関数を定義する。`lean/lean.h` は Lean のオブジェクトや `IO` の結果を扱うためのヘッダーである。

```c
#include <stdint.h>
#include <stdio.h>
#include <lean/lean.h>

uint32_t ref_c_add(uint32_t a, uint32_t b) {
    return a + b;
}

lean_obj_res ref_c_print(b_lean_obj_arg s) {
    if (puts(lean_string_cstr(s)) == EOF) {
        return lean_io_result_mk_error(
            lean_mk_io_error_other_error(0, lean_mk_string("puts failed")));
    }
    return lean_io_result_mk_ok(lean_box(0));
}
```

`UInt32` は FFI 境界で `uint32_t` に対応する。加算は固定幅整数の演算で、範囲を超えた結果は下位 32 ビットになる。

`lean_string_cstr` は文字列の UTF-8 データへのポインターを返す。`puts` は読み取りだけなので、借用した `s` に `lean_dec` を呼ぶ必要はない。ポインターは Lean の文字列が生存する間だけ有効であり、後で使うために無条件に保存できない。また、`puts` は最初の NUL バイトで出力を止めるため、埋め込まれた NUL を含む文字列全体の出力には別の処理が必要になる。

`IO Unit` の成功結果は `lean_io_result_mk_ok(lean_box(0))` で作る。`lean_box(0)` は `Unit.unit` の実行時表現である。失敗時は `IO.Error` のオブジェクトを作って `lean_io_result_mk_error` に渡す。単に `Unit` の値を返すだけでは `IO` の結果にならない。

### Lake のビルド設定

`lakefile.lean` は、C ファイルからオブジェクトファイルと静的ライブラリを作り、Lean の実行ファイルへリンクする。

```text
import Lake
open System Lake DSL

package cBindingDemo

target bindings.o pkg : FilePath := do
  let srcJob ← inputTextFile (pkg.dir / "bindings.c")
  let oFile := pkg.buildDir / "c" / "bindings.o"
  let weakArgs := #["-I", (← getLeanIncludeDir).toString]
  buildO oFile srcJob weakArgs #["-fPIC"] "cc" getLeanTrace

extern_lib libbindings pkg := do
  let obj ← bindings.o.fetch
  buildStaticLib (pkg.staticLibDir / nameToStaticLib "bindings") #[obj]

@[default_target]
lean_exe cBindingDemo where
  root := `Main
```

`getLeanIncludeDir` は使用中の Lean のヘッダーディレクトリを返す。`buildO` は C コンパイラ `cc` で `bindings.c` をコンパイルし、`buildStaticLib` はオブジェクトファイルを静的ライブラリへまとめる。`nameToStaticLib` はプラットフォームに合うライブラリ名を作る。`extern_lib` の生成物は、パッケージの Lean 実行ファイルのリンクに組み込まれる。

### ビルドと実行

指定した Lean と C コンパイラ `cc` が利用できる環境で、プロジェクトのディレクトリから実行する。

```sh
lake build
lake exe cBindingDemo
```

出力は次のとおり。

```text
42
Hello from C
```

`@[extern]` は C のソースファイルを探したりコンパイルしたりする属性ではない。C のビルドとリンクを省くと、実行ファイルの作成時に外部シンボルが見つからない。

## 型と所有権の対応

C 関数の引数と戻り値は、Lean の型から決まる ABI（バイナリの呼び出し規約）に合わせる必要がある。

ここでいう所有権は、オブジェクトへの参照を管理する責任である。所有する参照が不要になったら、`lean_dec` で手放すか、別の関数へ所有権を渡す。借用は、その責任を受け取らずに参照を使うことである。

| Lean 側 | C 側 | 意味 |
| --- | --- | --- |
| `UInt8`・`UInt16`・`UInt32`・`UInt64` | `uint8_t`・`uint16_t`・`uint32_t`・`uint64_t` | 固定幅の符号なし整数 |
| `USize` | `size_t` | ポインター幅の符号なし整数 |
| `Float` | `double` | 浮動小数点数 |
| `Nat`・`Int` | `lean_object *` | 小さい値のエンコードまたは多倍長整数のオブジェクト |
| 所有される `String` 引数 | `lean_obj_arg` | 受け取った参照の所有権を C 側が処理 |
| 借用される `@& String` 引数 | `b_lean_obj_arg` | 呼び出し中の読み取り用の参照 |
| `String` などのオブジェクトの戻り値 | `lean_obj_res` | 呼び出し元へ所有権を渡す結果 |

`Nat` は任意精度なので、`uint64_t` に置き換えられない。文字列も `char *` そのものではなく、Lean のオブジェクトとして受け取る。`lean_obj_arg`、`b_lean_obj_arg`、`lean_obj_res` はいずれも `lean_object *` の別名だが、所有権の約束を区別するために使う。

### 参照カウントによるメモリ管理

Lean は参照カウント方式でメモリを管理し、参照カウントが 0 になったオブジェクトを解放する。Lean のコードではコンパイラが増減の処理を挿入するが、C 側では所有権の約束に従って処理する必要がある。到達可能なオブジェクトにマークを付けて回収する方式ではなく、C 側で GC 用のマーク・アンマークを行う必要はない。

- 所有される引数は、所有権を受け取る関数へ渡すか、不要になった時点で `lean_dec` する。所有権を渡した後に、同じ参照をさらに `lean_dec` してはいけない。
- 借用した引数を呼び出し中に読むだけなら、増減は不要である。戻り値として返す場合や、呼び出し後も C 側に保持する場合は、`lean_inc` で所有する参照を一つ増やす。保持した参照は、不要になったら `lean_dec` する。
- 新しく作ったオブジェクトを戻り値として返す場合は、その所有権を呼び出し元へ渡す。たとえば `lean_mk_string("hello")` の結果をそのまま返せばよく、返す前に `lean_dec` しない。

Lean のオブジェクト自体に C の `free` を呼んではいけない。一方、C 側で確保した構造体などは C 側で解放する。`lean_alloc_external` で包む場合は、`lean_register_external_class` に登録するファイナライザー（解放処理）で内部のメモリを解放できる。この処理は、包んだ Lean オブジェクトが解放されるときに呼ばれる。

## 副作用・論理上の定義・評価の注意

ファイル操作、外部の状態の読み書きなどは `IO` を返す関数として宣言する。純粋な関数として宣言すると、コンパイラが計算結果を再利用したり不要な呼び出しを消したりできるため、副作用を持つ C 関数には適さない。

`@[extern] def` で Lean の本体も与えることはできる。その場合、論理上の定義と C の実行時実装が一致する責任はバインディングの作者にある。Lean の型検査は C の実装を検証しない。また、上の `opaque` 宣言には計算を展開できる Lean の本体がないため、`rfl` などで `cAdd 20 22 = 42` を計算によって証明する用途には使えない。

`#eval` から外部関数を呼び出すには、シンボルを含む共有ライブラリを Lean のプロセスへ読み込む必要がある。ネイティブ実行ファイルへの静的リンクだけでは、エディター内の `#eval` で利用可能になるとは限らない。ライブラリを利用する構成では Lake の `precompileModules` と、そのモジュールのインポートを使える。

FFI とコンパイラ内部の ABI は変更される可能性がある。上の `IO` 関数の C シグネチャは Lean 4.35.0-rc3 に合わせており、古い例にある追加の `world` 引数は付けない。別の版でバインディングを作るときは、Lean が生成する C ファイルの外部関数宣言も確認すると、型や引数のずれを見つけやすい。

参照：[公式リファレンス：FFI](https://lean-lang.org/doc/reference/latest/Run-Time-Code/Foreign-Function-Interface/)、[参照カウント](https://lean-lang.org/doc/reference/latest/Run-Time-Code/Reference-Counting/)、[文字列の FFI](https://lean-lang.org/doc/reference/latest/find/?domain=Verso.Genre.Manual.section&name=string-ffi)、[Lake の外部ライブラリ](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/)。

[コンパイラと外部コードの一覧に戻る](README.md)
