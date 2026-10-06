# `focus`

`focus` は、現在の先頭のゴールにだけ注目して、内側の証明を進めるタクティクスである。

複数のゴールがあっても、内側の `all_goals` などが他のゴールに触れないようにできる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  focus
    exact hp
  exact hq
```

この例では `focus` 内で `P` だけを証明し、ブロックの外で `Q` を証明する。

`focus` は選んだゴールを完全に閉じることまでは要求しない。`·` のブロックは、通常そのブロック内で選んだゴールを閉じるために使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`focus`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.focus)。

[タクティクス一覧に戻る](README.md)
