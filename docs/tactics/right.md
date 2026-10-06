# `right`

`right` は、論理和のゴールで、右側を証明する方針を選ぶタクティクスである。

ゴールが `P ∨ Q` のとき、`right` と書くとゴールが `Q` になる。

```lean
example (P Q : Prop) (hq : Q) : P ∨ Q := by
  right
  exact hq
```

これは `Or.inr` というコンストラクターを使う操作である。入れ子の論理和では、選択を繰り返せる。

```lean
example (P Q R : Prop) (hq : Q) : P ∨ Q ∨ R := by
  right
  left
  exact hq
```

`P ∨ Q ∨ R` は `P ∨ (Q ∨ R)` と読まれるので、右へ進んでから左を選ぶと `Q` に届く。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`right`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.right)。

[タクティクス一覧に戻る](README.md)
