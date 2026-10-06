# `class`・`instance`

`class` は、型などに対して用意すべき操作や性質を、型クラスとして定義する構文である。`instance` は、その具体的な実装を登録する。

[`List`・`Option`](../basic-types/README.md) はデータ型を作るものであり、型クラスではない。例えば `List Nat` は自然数のリストの型、`ToString (List Nat)` はそのリストを文字列に変える実装の型である。

```lean
class HasLabel (α : Type) where
  label : α → String

instance : HasLabel Nat where
  label n := "nat:" ++ toString n

def render {α : Type} [HasLabel α] (x : α) : String :=
  HasLabel.label x

#eval render (3 : Nat)
```

`HasLabel Nat` は「自然数のラベルを作る実装」の型である。`instance` によって実装が登録され、`render` の `[HasLabel α]` に対して Lean が必要な実装を探す。

出力は `"nat:3"` になる。呼び出す側は `label` の実装を毎回渡さなくてよい。

標準の型クラスに、自分の型の実装を用意することもできる。

```lean
structure Score where
  value : Nat

instance : ToString Score where
  toString s := toString s.value

#eval toString (Score.mk 8)
```

この出力は `"8"` である。`ToString` は標準の型クラスなので、新たに `class` を定義する必要はない。

[`structure`](structure.md) は成分をまとめる型を作り、`class` はそれをインスタンス探索で使う型として扱う。普通の値を `def` で作るだけでは、探索対象として自動登録されない。

`[HasLabel α]` は真偽を場合分けする記法ではなく、使える実装を引数として要求する記法である。

インスタンスを自動生成する [`deriving`](deriving.md) と、一つの式の後続部分だけで使う [`haveI`・`letI`](local_instances.md) もある。

参照：[公式リファレンス：Type Classes](https://lean-lang.org/doc/reference/latest/Type-Classes/)。

[文法要素の一覧に戻る](README.md)
