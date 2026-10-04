# `do`・`←`・`return`

`do` は、**結果を伴う計算を順番につなぎ、次の計算でその結果を使う**構文である。`IO` や `Option` などで使う。

```lean
def addOptions (x y : Option Nat) : Option Nat := do
  let a ← x
  let b ← y
  return a + b

example : addOptions (some 2) (some 3) = some 5 := rfl
example : addOptions none (some 3) = none := rfl
```

この `Option` の例では、`let a ← x` は `some` の中身を取り出して `a` と呼ぶ。`none` ならそこで計算全体が `none` になり、後続を進めない。

`return` は値をその計算の結果として返す。ここでは `return 5` が `some 5` に対応する。

`:=` と `←` は役割が違う。

```lean
def addOne (x : Option Nat) : Option Nat := do
  let a ← x
  let b := a + 1
  return b

example : addOne (some 3) = some 4 := rfl
```

`a` は計算の結果を受け取る名前、`b` は通常の式の値に付けた名前である。

`IO` では、出力などの処理を順に実行する。

```lean
def greet : IO Unit := do
  IO.println "hello"
  IO.println "Lean"

#eval greet
```

順に `hello` と `Lean` が表示される。`do` は [`by`](by.md) のように証明のゴールを操作するものではなく、モナドの計算をつなぐ構文である。`←` の具体的な動きは、使うモナドによって変わる。

局所変数の更新、`for`・`while` による繰り返し、`break`・`continue` は [`do` 内の更新と繰り返し](do_control.md)を参照。

`>>=`・`<$>`・`<*>`・`<|>` などを使って計算を組み合わせる書き方は[計算をつなぐ演算子](monad_operators.md)を参照。

参照：[公式リファレンス：Functors, Monads and do-Notation](https://lean-lang.org/doc/reference/latest/Functors___-Monads-and--do--Notation/)。

[文法要素の一覧に戻る](README.md)
