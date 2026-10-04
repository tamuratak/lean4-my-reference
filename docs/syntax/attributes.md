# 属性：`@[…]`・`attribute`

属性は、**宣言を特定の処理で使うために登録するなど、Lean に追加の扱いを指示する**仕組みである。

例えば `@[simp]` は、定理を簡単化の際に使う規則として登録する。

```lean
def wrap (n : Nat) : Nat := n

@[simp] theorem wrap_eq (n : Nat) : wrap n = n := rfl

example (n : Nat) : wrap (wrap n) = n := by
  simp
```

`@[simp]` は次の宣言に付く。この例では `simp` が `wrap_eq` を使い、入れ子の `wrap` を取り除く。

既にある宣言には `attribute` で属性を付けられる。

```lean
def wrap (n : Nat) : Nat := n

theorem wrap_eq (n : Nat) : wrap n = n := rfl
attribute [simp] wrap_eq

example (n : Nat) : wrap n = n := by
  simp
```

`attribute [local simp] wrap_eq` のように `local` を付けると、現在のセクションの範囲だけで属性を有効にできる。`attribute [-simp] wrap_eq` はその登録を外す書き方である。

属性の意味は名前ごとに違う。`@[simp]` と書くだけで定理が証明されるわけではなく、定理の本体は別に与える必要がある。

`@[…]` は宣言に付ける属性、関数の引数の `[ToString α]` はインスタンス引数である。括弧が似ていても用途が違う。

簡単化そのものの説明は、[タクティクスの `simp`](../tactics/simp.md)を参照。

参照：[公式リファレンス：Attributes](https://lean-lang.org/doc/reference/latest/Attributes/)。

[文法要素の一覧に戻る](README.md)
