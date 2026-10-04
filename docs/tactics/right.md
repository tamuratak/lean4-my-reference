# `right`

`right` は、**論理和のゴールで、右側を証明する方針を選ぶ**タクティクスである。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
