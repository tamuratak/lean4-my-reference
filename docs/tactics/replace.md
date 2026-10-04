# `replace`

`replace` は、**新しい事実を追加し、同じ名前の古い仮定が不要なら取り除く**タクティクスである。

仮定を加工した結果だけを残したいときに使う。

```lean
example (P Q : Prop) (h : P ∧ Q) : Q := by
  replace h : Q := h.2
  exact h
```

この後の `h` は `P ∧ Q` ではなく `Q` の証明になる。

`have h : Q := h.2` でも新しい名前を付けられるが、古い仮定は内部に残り得る。`replace` は古い仮定の除去も試す。ほかの型が古い仮定に依存していて除去できないときは、元の仮定が残ることがある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`replace`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.replace)。

[タクティクス一覧に戻る](README.md)
