# `apply_assumption`

`apply_assumption` は、**ゴールに合う仮定を適用し、必要な前提を新しいゴールにする**タクティクスである。

`assumption` はゴールそのものの証明を探す。`apply_assumption` は含意の仮定なども利用できる。

```lean
example (P Q : Prop) (hp : P) (h : P → Q) : Q := by
  apply_assumption
  assumption
```

例えば `h : P → Q` をゴール `Q` に適用すると、前提 `P` が残る。上の例では、続けた `assumption` でそれを閉じている。

```lean
example (P Q : Prop) (h : P → Q) : P → Q := by
  intro hp
  apply_assumption
  assumption
```

複数段の探索を明示的に頼むなら `solve_by_elim`、使う仮定が分かっているなら `apply h` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`apply_assumption`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.applyAssumption)。

[タクティクス一覧に戻る](README.md)
