# `cases`

`cases` は、**帰納型の値を、コンストラクターごとに場合分けする**タクティクスである。

例えば `h : P ∨ Q` は、左側の証明を持つ場合と右側の証明を持つ場合に分かれる。

```lean
example (P Q : Prop) (h : P ∨ Q) : Q ∨ P := by
  cases h with
  | inl hp => exact Or.inr hp
  | inr hq => exact Or.inl hq
```

自然数なら、ゼロの場合と後者の場合に分かれる。

```lean
example (n : Nat) : n = 0 ∨ ∃ k, n = Nat.succ k := by
  cases n with
  | zero => exact Or.inl rfl
  | succ k => exact Or.inr ⟨k, rfl⟩
```

`cases` は帰納法の仮定を作らない。小さい値についての結論を使いたい場合は `induction` を使う。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
