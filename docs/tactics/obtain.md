# `obtain`

`obtain` は、**事実を受け取り、パターンに従ってその中身を取り出す**タクティクスである。

存在命題の証明から証人と条件を取り出すときに便利である。

```lean
example (α : Type) (P Q : α → Prop)
    (h : ∃ x, P x ∧ Q x) : ∃ x, Q x := by
  obtain ⟨x, hp, hq⟩ := h
  exact ⟨x, hq⟩
```

事実をその場で証明してから分解することもできる。

```lean
example : ∃ n : Nat, n = 3 := by
  obtain ⟨n, hn⟩ : ∃ n : Nat, n = 3 := by
    exact ⟨3, rfl⟩
  exact ⟨n, hn⟩
```

`have h := ...` と `rcases h with ...` をまとめた書き方として考えると分かりやすい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
