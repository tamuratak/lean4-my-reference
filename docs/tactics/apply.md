# `apply`

`apply` は、**結論がゴールに合う定理を使い、その前提を新しいゴールにする**タクティクスである。

例えば、`h : P → Q` があり、ゴールが `Q` のとき、`apply h` と書くとゴールが `P` になる。

```lean
example (P Q : Prop) (h : P → Q) (hp : P) : Q := by
  apply h
  exact hp
```

前提が複数なら、複数のゴールができる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  apply And.intro
  · exact hp
  · exact hq
```

つまり、`exact` が完成した証明を渡すのに対し、`apply` は「この定理で証明するには何が必要か」を取り出す。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
