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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`refine`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.refine)。

[タクティクス一覧に戻る](README.md)
