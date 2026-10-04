# `solve_by_elim`

`solve_by_elim` は、**仮定や指定した補題を後ろ向きに適用し、残る前提も再帰的に証明する**タクティクスである。

ゴールが `R` なら、`Q → R` を使って `Q`、次に `P → Q` を使って `P`、という順で探せる。

```lean
example (P Q R : Prop) (hp : P) (hpq : P → Q) (hqr : Q → R) : R := by
  solve_by_elim
```

使う補題を追加することもできる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  solve_by_elim [And.intro]
```

探索には深さなどの制限がある。任意の証明を見つけるわけではないので、失敗したら必要な補題を渡すか、`apply` と `exact` で道筋を明示する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`solve_by_elim`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.solveByElim)。

[タクティクス一覧に戻る](README.md)
