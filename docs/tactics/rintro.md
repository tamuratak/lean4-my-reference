# `rintro`

`rintro` は、**`intro` と `rcases` を組み合わせ、導入した仮定をその場で分解する**タクティクスである。

ゴールが `(P ∧ Q) → Q` なら、論理積を仮定として受け取ってから分解する必要がある。`rintro ⟨hp, hq⟩` はこの二つをまとめて行う。

```lean
example (P Q : Prop) : (P ∧ Q) → Q := by
  rintro ⟨hp, hq⟩
  exact hq

example (P Q : Prop) : (P ∨ Q) → (Q ∨ P) := by
  rintro (hp | hq)
  · exact Or.inr hp
  · exact Or.inl hq
```

既に仮定にあるものは `rcases`、これからゴールから導入するものは `rintro` と使い分ける。

`rintro?` は導入と分解のパターンを提案する。自分で付けたい名前が決まっているなら `rintro` で直接指定する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`rintro`](https://lean-lang.org/doc/api/Init/RCases.html#Lean.Parser.Tactic.rintro)。

[タクティクス一覧に戻る](README.md)
