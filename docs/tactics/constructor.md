# `constructor`

`constructor` は、ゴールの帰納型のコンストラクターを適用し、その引数をゴールにするタクティクスである。

論理積 `P ∧ Q` のコンストラクターは、`P` と `Q` の証明を受け取る。そのため `constructor` で二つのゴールに分かれる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  · exact hp
  · exact hq
```

同値 `P ↔ Q` なら、二つの向きの含意を証明することになる。

```lean
example (P : Prop) : P ↔ P := by
  constructor
  · intro hp
    exact hp
  · intro hp
    exact hp
```

コンストラクターが複数ある型では、適用できるものを試す。論理和では、証明したい側を `left`・`right` で明示すると分かりやすい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`constructor`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.constructor)。

[タクティクス一覧に戻る](README.md)
