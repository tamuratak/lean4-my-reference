# 式の `haveI`・`letI`

式の `haveI` と `letI` は、**後続の式で使う型クラスのインスタンスを、その場で用意する**構文である。

```lean
def defaultNat : Nat :=
  letI : Inhabited Nat := ⟨7⟩
  default

example : defaultNat = 7 := rfl
```

`Inhabited Nat` は既定値となる自然数を持つ型クラスである。`letI` の後では、この局所的な実装が使われるので、`default` は `7` になる。

`haveI` でも、同様に局所的な実装を用意できる。

```lean
def defaultBool : Bool :=
  haveI : Inhabited Bool := ⟨true⟩
  default

example : defaultBool = true := rfl
```

Lean 4.34.1 の式の `haveI` と `letI` は、与えた値をインライン化する。そのため、通常の [`have`](have.md) と [`let`](let.md) の本体の展開についての違いを、そのまま当てはめない。

実装する値に応じたインスタンスを用意することもできる。

```lean
def useAsDefault {α : Type} (x : α) : α :=
  letI : Inhabited α := ⟨x⟩
  default

example : useAsDefault (3 : Nat) = 3 := rfl
```

局所インスタンスは後続の式で使えるが、定義の外で使うグローバルなインスタンスとして登録されるわけではない。広く登録する場合は [`instance`](class.md) を使う。

このページは `by` の外に書く式を扱う。`by` の中で使う操作は[タクティクスのインスタンス探索のページ](../tactics/infer_instance.md)を参照。

参照：[公式 API：式の `haveI`](https://lean-lang.org/doc/api/Lean/Parser/Term.html#Lean.Parser.Term.haveI)、[公式 API：式の `letI`](https://lean-lang.org/doc/api/Lean/Parser/Term.html#Lean.Parser.Term.letI)。

[文法要素の一覧に戻る](README.md)
