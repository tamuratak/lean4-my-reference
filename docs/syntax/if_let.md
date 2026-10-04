# `if let … := … then … else …`

`if let` は、**値が指定したパターンに一致するかどうかで分岐し、一致した場合はその成分も使う**構文である。

```lean
def valueOrZero (x : Option Nat) : Nat :=
  if let some n := x then n else 0

example : valueOrZero (some 7) = 7 := rfl
example : valueOrZero none = 0 := rfl
```

`x` が `some n` の形なら、`then` 側で中身を `n` と呼んで使う。それ以外、ここでは `none` の場合は `else` 側へ進む。

これは次の `match` と同じ分岐を書く短い形である。

```lean
def valueOrZero (x : Option Nat) : Nat :=
  match x with
  | some n => n
  | _ => 0

example : valueOrZero (some 7) = 7 := rfl
```

リストの先頭を取り出す場合にも使える。

```lean
def firstOrZero (xs : List Nat) : Nat :=
  if let n :: _ := xs then n else 0

example : firstOrZero [4, 5] = 4 := rfl
example : firstOrZero [] = 0 := rfl
```

パターンで導入する `n` は `then` 側だけで使える。`else` 側には一致した成分がないので、`n` は使えない。

普通の [`if`](if.md) は条件の真偽で分岐する。`if let` は値の形に一致するかで分岐するので、任意の命題を判定するための構文ではない。

複数のコンストラクターについてそれぞれ異なる結果を書く場合は、[`match`](match.md) の方が見通しよく書ける。

参照：[公式リファレンス：Conditionals](https://lean-lang.org/doc/reference/latest/Terms/Conditionals/)。

[文法要素の一覧に戻る](README.md)
