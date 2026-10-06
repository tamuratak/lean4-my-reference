# `opaque`・`axiom`

`opaque` は、型と本体を確認して定数を定義し、証明の計算ではその本体を展開しない構文である。

```lean
opaque hidden : Nat := 3

#check hidden
#eval hidden
```

`hidden` の型は `Nat` で、`#eval` の出力は `3` である。実行時には本体を使うが、Lean のカーネルが定義上の等しさを確認する際には、本体を展開しない。

そのため、次の断片は `rfl` では証明できない。

```text
example : hidden = 3 := rfl
```

通常の [`def`](def.md) なら、本体の計算で等しさが分かる例でも、`opaque` では同じようには使えない。[`noncomputable`](noncomputable.md) は実行用のコードを作らない指定なので、実行できるこの `opaque` とは別の性質である。

`axiom` は、本体や証明を与えず、指定した型を持つ定数を仮定として登録する構文である。

```lean
axiom chosenNumber : Nat
axiom chosenNumber_eq : chosenNumber = 3

theorem chosenNumber_add_one : chosenNumber + 1 = 4 := by
  rw [chosenNumber_eq]

#print axioms chosenNumber_add_one
```

最初の宣言は自然数の値を仮定し、次の宣言はその値が `3` と等しいという命題を仮定する。後続の定理は、その仮定を使って証明している。

[`#print axioms`](../commands/print_axioms.md) で定理が依存する公理を確認できる。この例で Lean が確認するのは、仮定した公理から定理の結論を導けることであり、`chosenNumber_eq` 自体を証明したわけではない。

`opaque` は本体を与えて型を確認する一方、`axiom` はその型の値が存在することから仮定する。単に定理の証明を書きたい場合は [`theorem`](theorem.md) を使う。

参照：[公式リファレンス：Definitions / Opaque Constants](https://lean-lang.org/doc/reference/latest/Definitions/Definitions/)、[公式リファレンス：Axioms](https://lean-lang.org/doc/reference/latest/Axioms/)。

[文法要素の一覧に戻る](README.md)
