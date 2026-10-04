# `if`

`if` は、**判定可能な条件に応じて、証明の分岐を選ぶ**タクティクスである。

タクティクスの中でも条件を使って分岐できる。

```lean
example (n : Nat) : n = 0 ∨ n ≠ 0 := by
  if h : n = 0 then
    exact Or.inl h
  else
    exact Or.inr h
```

真の場合には `h : n = 0`、偽の場合には `h : n ≠ 0` を使える。

命題の真偽に沿って両方の場合を証明する用途では `by_cases h : n = 0` と書く方法もある。ゴールの中にある `if` を分けたい場合は `split` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`if`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacDepIfThenElse)。

[タクティクス一覧に戻る](README.md)
