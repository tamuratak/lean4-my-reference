# `apply_rules`

`apply_rules` は、指定した補題や仮定を繰り返し適用して、ゴールを小さな課題へ分けるタクティクスである。

例えば論理積を作る補題と、手元の証明を組み合わせられる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  apply_rules [And.intro]
```

`solve_by_elim` はゴールを閉じる証明を探索するが、`apply_rules` は前提が残った状態でも成功できる。

```lean
example (P Q : Prop) (h : P → Q) (hp : P) : Q := by
  apply_rules [h]
```

使う規則が多すぎると意図しない分解になることがある。短い証明では `apply h` の方が道筋を明示できる。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`apply_rules`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.applyRules)。

[タクティクス一覧に戻る](README.md)
