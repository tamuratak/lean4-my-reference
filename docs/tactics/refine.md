# `refine`

`refine` は、**証明の形を指定し、`?_` の部分を新しいゴールとして残す**タクティクスである。

`⟨hp, ?_⟩` は「論理積の左側は `hp`、右側は後で証明する」という指定である。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  refine ⟨hp, ?_⟩
  exact hq

example : ∃ n : Nat, n = 3 := by
  refine ⟨3, ?_⟩
  rfl
```

存在命題の例では、証人を `3` に決めたので、残るゴールは `3 = 3` になる。

`refine` では `?_` が明示的な穴になる。`refine'` はさらに、推論で解決されなかった通常の穴 `_` などもゴールとして扱う。最初は `refine` と `?_` の組合せを使うと、残す課題が分かりやすい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
