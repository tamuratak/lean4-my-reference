# `have`

`have` は、途中で使う補助的な事実を証明し、仮定に追加するタクティクスである。

例えば `have hq : Q := h hp` と書くと、以後の証明で `hq : Q` を使える。

```lean
example (P Q : Prop) (hp : P) (h : P → Q) : Q ∧ P := by
  have hq : Q := h hp
  exact ⟨hq, hp⟩
```

補助的な事実自体をタクティクスで証明することもできる。

```lean
example (P Q : Prop) (hp : P) (h : P → Q) : Q := by
  have hq : Q := by
    apply h
    exact hp
  exact hq
```

`have` はゴールを置き換えず、手元で使える事実を増やす。

`have'` は内部で `refine'` に対応する処理を使う変種で、通常の穴 `_` などの扱いが異なる。最初は `have h : 型 := 証明` と型と証明を明示すればよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`have`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticHave__)。

[タクティクス一覧に戻る](README.md)
