# `calc`

`calc` は、**中間の式を並べ、等式や不等式を推移性でつなぐ**タクティクスである。

`a = b` と `b = c` があれば、その間を `calc` でつなげられる。

```lean
example (a b c : Nat) (hab : a = b) (hbc : b = c) : a = c := by
  calc
    a = b := hab
    _ = c := hbc
```

二行目の `_` は、直前の右辺 `b` を表す。各行には、その一段階を証明する項を書く。

```lean
example (a b c : Nat) (hab : a ≤ b) (hbc : b ≤ c) : a ≤ c := by
  calc
    a ≤ b := hab
    _ ≤ c := hbc
```

途中の証明にも `by ...` を使える。長い書き換えを、何を経由したかが見える形で書きたいときに便利である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`calc`](https://lean-lang.org/doc/api/Lean/Elab/Tactic/Calc.html)。

[タクティクス一覧に戻る](README.md)
