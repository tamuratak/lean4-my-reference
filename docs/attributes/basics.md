# 属性の付け方：`@[…]`・`attribute`

属性は、宣言に追加の扱いを指定する仕組みである。例えば `@[simp]` は、定理を簡単化で使う規則として登録する。

```lean
def wrap (n : Nat) : Nat := n

@[simp] theorem wrap_eq (n : Nat) : wrap n = n := rfl

example (n : Nat) : wrap (wrap n) = n := by
  simp
```

`@[simp]` は直後の `theorem` 宣言に付く。これにより、`simp` が `wrap_eq` を使い、ゴールの入れ子の `wrap` を取り除ける。属性自体が定理を証明するわけではなく、証明は `:= rfl` で別に与えている。

## 既存の宣言に付ける

既にある宣言には、`attribute` コマンドを使う。

```lean
def wrap (n : Nat) : Nat := n

theorem wrap_eq (n : Nat) : wrap n = n := rfl
attribute [simp] wrap_eq

example (n : Nat) : wrap n = n := by
  simp
```

`@[simp] theorem ...` は宣言と同時に付ける書き方、`attribute [simp] wrap_eq` は宣言後に付ける書き方である。

## 複数の属性

同じ宣言に複数の属性を付けるときは、角括弧の中でコンマで区切る。

```lean
@[reducible, simp] def wrapped (n : Nat) : Nat := n

example (n : Nat) : wrapped n = n := by
  simp
```

この例では、定義を展開しやすくする `reducible` と、簡単化に登録する `simp` を付けている。属性の名前は自由なコメントではなく、Lean に登録されたものを使う必要がある。指定できる属性や組み合わせは宣言の種類によっても異なる。

## 登録を外す

```lean
def wrap (n : Nat) : Nat := n

@[simp] theorem wrap_eq (n : Nat) : wrap n = n := rfl
attribute [-simp] wrap_eq

example (n : Nat) : wrap n = n := by
  simp only [wrap_eq]
```

`attribute [-simp] wrap_eq` は、標準の簡単化の規則から登録を外す。定理そのものを削除するわけではないので、`simp only [wrap_eq]` のように明示して使うことはできる。

すべての属性が削除に対応しているわけではない。追加や削除の有効範囲については、[有効範囲](scopes.md)を参照。

参照：[公式リファレンス：Attributes](https://lean-lang.org/doc/reference/latest/Attributes/)。

[属性の一覧に戻る](README.md)
