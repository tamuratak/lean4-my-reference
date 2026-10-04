# 関数適用：`f x`・名前付き引数・`@`

`f x` は、**関数 `f` に引数 `x` を渡す**書き方である。呼び出し専用の括弧やカンマは使わない。

```lean
def add (x y : Nat) : Nat := x + y

example : add 2 3 = 5 := rfl
example : (add 2) 3 = 5 := rfl
```

`add 2 3` は `(add 2) 3` と読む。引数自体が計算式なら、括弧でまとめる。

```lean
def double (n : Nat) : Nat := n + n

example : double (2 + 3) = 10 := rfl
example : double 2 + 3 = 7 := rfl
```

関数適用は `+` より強く結び付くので、`double 2 + 3` は `(double 2) + 3` になる。

引数名を使うと、暗黙の引数も明示できる。`@` を付けると、暗黙の引数も位置順に渡せる。

```lean
def keep {α : Type} (x : α) : α := x

example : keep (α := Nat) 3 = 3 := rfl
example : @keep Nat 3 = 3 := rfl
```

`@keep` の最初の引数は型 `α`、次が値 `x` である。引数の順序が分かりにくいときは、名前付き引数の方が読みやすい。

ドットで書く関数適用もある。

```lean
example : [1, 2, 3].length = List.length [1, 2, 3] := rfl
```

この `.length` は `List.length` にリストを渡す記法である。構造体のフィールドを取り出すドット記法については [`structure`](structure.md) を参照。

参照：[公式リファレンス：Function Application](https://lean-lang.org/doc/reference/latest/Terms/Function-Application/)。

[文法要素の一覧に戻る](README.md)
