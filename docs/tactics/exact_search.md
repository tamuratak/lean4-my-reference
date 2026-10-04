# `exact?`

`exact?` は、**ライブラリや仮定から、ゴールを閉じる証明を探して提案する**タクティクスである。

必要な定理名が思い出せないときに使う。

```lean
example (n : Nat) : 0 + n = n := by
  exact?
```

成功すると証明を閉じ、エディターに `exact ...` などの候補を表示する。提案を採用すると、使った定理が明示された証明にできる。

`apply?` は適用できる補題を探し、その前提を残すことがある。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  apply?
  all_goals assumption
```

`rw?` は書き換えに使える補題を探す関連タクティクスである。検索できる範囲はインポート済みのライブラリに依存する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`exact?`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.exact%3F)。

[タクティクス一覧に戻る](README.md)
