# `infer_instance`

`infer_instance` は、**型クラスのインスタンスを探して、ゴールを閉じる**タクティクスである。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
