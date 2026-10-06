# `#print axioms`

`#print axioms 名前` は、宣言が直接・間接に依存している公理を表示するコマンドである。

```lean
theorem selfEq (n : Nat) : n = n := rfl

#print axioms selfEq
```

この定理については、依存する公理がないことが表示される。

自分で仮定した公理を使うと、その依存が分かる。

```lean
axiom assumedFact : (3 : Nat) = 3

theorem copiedFact : (3 : Nat) = 3 := assumedFact

#print axioms copiedFact
```

`copiedFact` は `assumedFact` に依存する。命題自体は `rfl` でも証明できるが、この定義で与えた証明は公理を使っているので、その依存が表示される。

調べるのは元の証明方法の名前ではなく、登録された宣言とその依存関係である。証明を通じて使った別の定理が公理に依存していれば、間接的な依存も含まれる。

[`#print`](print.md) は宣言の型や本体、`#print axioms` はその宣言の依存公理を表示する。公理を仮定する `axiom` の説明は[宣言のページ](../syntax/opaque_axiom.md)を参照。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
