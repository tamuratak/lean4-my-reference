# `infer_instance`

`infer_instance` は、型クラスのインスタンスを探して、ゴールを閉じるタクティクスである。

型クラスは、型に備わる操作や性質を表す仕組みである。

```lean
example : Inhabited Nat := by
  infer_instance
```

この例では、自然数に既定の値があるというインスタンスを探す。

`haveI` や `letI` を使うと、証明の途中で局所的なインスタンスを追加できる。

```lean
example (α : Type) (a : α) : Inhabited α := by
  letI : Inhabited α := ⟨a⟩
  infer_instance
```

普通の `have h : Inhabited α := ...` と異なり、`haveI`・`letI` はインスタンス探索に使わせるための書き方である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`infer_instance`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticInfer_instance)。

[タクティクス一覧に戻る](README.md)
