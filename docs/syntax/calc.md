# 式の `calc`

`calc` は、中間の式と各段階の証明を並べ、等式などの証明をつなぐ構文である。`:=` の右側に直接書ける。

```lean
example (a b c : Nat) (hab : a = b) (hbc : b = c) : a = c :=
  calc
    a = b := hab
    _ = c := hbc
```

最初の行で `a = b`、次の行で `b = c` を示す。二行目の左辺 `_` は、直前の右辺 `b` を引き継ぐ。全体は推移性により `a = c` の証明になる。

各行の `:=` の右側には、その行の関係を証明する項を書く。そこだけ `by` を使うこともできる。

```lean
example (a b : Nat) : a + b + 0 = b + a :=
  calc
    a + b + 0 = a + b := by rfl
    _ = b + a := Nat.add_comm a b
```

同じ構文で不等式をつなぐこともできる。

```lean
example (a b c : Nat) (hab : a ≤ b) (hbc : b ≤ c) : a ≤ c :=
  calc
    a ≤ b := hab
    _ ≤ c := hbc
```

関係をつなぐには対応する推移性の仕組みが必要であり、任意の記号を自由につなげられるわけではない。

`by` の中で使う場合の証明状態については、[タクティクスの `calc`](../tactics/calc.md)を参照。

参照：[公式リファレンス：Tactic Reference / calc](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)。

[文法要素の一覧に戻る](README.md)
