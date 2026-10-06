# `apply?`

`apply?` は、適用できる補題を探し、残る前提も確認できるようにするタクティクスである。

`exact?` が証明を閉じる候補を探すのに対し、`apply?` は前提が残る候補も提案できる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  apply?
  all_goals assumption
```

候補によってはその場で証明が完了することもある。この例では、残ったゴールがあれば `all_goals assumption` で閉じる。

エディターに表示された提案を採用すると、適用した定理を明示した証明にできる。検索の範囲はインポート済みの定理に依存する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`apply?`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.apply%3F)。

[タクティクス一覧に戻る](README.md)
