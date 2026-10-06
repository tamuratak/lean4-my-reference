# 引数の既定値：`(x : α := e)`

`(x : α := e)` は、呼び出し側が引数を省略したときに使う値を指定する書き方である。

```lean
def addDefault (x : Nat) (y : Nat := 1) : Nat := x + y

example : addDefault 3 = 4 := rfl
example : addDefault 3 5 = 8 := rfl
example : addDefault 3 (y := 5) = 8 := rfl
```

`addDefault 3` では `y` に既定値 `1` が入る。値を明示した場合は、その値が使われる。

既定値は、先に宣言した引数を使うこともできる。

```lean
def addCopy (x : Nat) (y : Nat := x) : Nat := x + y

example : addCopy 3 = 6 := rfl
example : addCopy 3 1 = 4 := rfl
```

省略した `y` は、その呼び出しで渡した `x` と同じ値になる。

既定値の位置に `by` の証明を書くと、省略した引数を呼び出し側でタクティクスによって補える。

```lean
def keepWithProof (n : Nat) (h : n = n := by rfl) : Nat := n

example : keepWithProof 3 = 3 := rfl
```

このような引数は自動引数と呼ばれる。証明のゴールは、呼び出しで渡した `n` に応じた `n = n` になる。

[`{x : α}`](binders.md) の暗黙の引数は周囲の型や引数から推論する。一方、`(x : α := e)` は省略時の値や補い方を宣言の側で指定する。どちらも省略できるが、値の決め方が違う。

参照：[公式リファレンス：Headers and Signatures](https://lean-lang.org/doc/reference/latest/Definitions/Headers-and-Signatures/)、[公式リファレンス：Function Application](https://lean-lang.org/doc/reference/latest/Terms/Function-Application/)。

[文法要素の一覧に戻る](README.md)
