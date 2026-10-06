# `all_goals`

`all_goals` は、現在あるすべてのゴールに、同じタクティクスを適用するタクティクスである。

論理積を分けた後、どちらも仮定で閉じるならまとめて処理できる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  all_goals assumption
```

どのゴールでも指定した操作が成功する必要がある。成功するゴールだけで処理したい場合には `any_goals` を使う。

`constructor <;> assumption` のように、前の操作が作ったゴールを続けて処理する書き方もある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`all_goals`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.allGoals)。

[タクティクス一覧に戻る](README.md)
