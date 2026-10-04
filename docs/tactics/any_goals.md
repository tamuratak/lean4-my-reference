# `any_goals`

`any_goals` は、**現在あるゴールのうち、指定したタクティクスが成功するものを処理する**タクティクスである。

少なくとも一つのゴールで成功すれば、全体として成功する。

```lean
example (P : Prop) (hp : P) : P ∧ True := by
  constructor
  any_goals assumption
  trivial
```

`assumption` は `P` のゴールを閉じ、証明のない `True` のゴールは残す。その後、`trivial` で閉じる。

どのゴールでも成功しなければ `any_goals` も失敗する。すべてのゴールで成功することを求めるなら `all_goals` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`any_goals`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.anyGoals)。

[タクティクス一覧に戻る](README.md)
