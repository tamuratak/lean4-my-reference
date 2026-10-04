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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`cases`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.cases)。

[タクティクス一覧に戻る](README.md)
