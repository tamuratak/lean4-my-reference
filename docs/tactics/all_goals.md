# `all_goals`

`all_goals` は、**現在あるすべてのゴールに、同じタクティクスを適用する**タクティクスである。

論理積を分けた後、どちらも仮定で閉じるならまとめて処理できる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  all_goals assumption
```

どのゴールでも指定した操作が成功する必要がある。成功するゴールだけで処理したい場合には `any_goals` を使う。

`constructor <;> assumption` のように、前の操作が作ったゴールを続けて処理する書き方もある。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
