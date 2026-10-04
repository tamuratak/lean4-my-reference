# `structure … extends …`

`extends` は、**既存の構造体のフィールドを引き継ぎ、新しい構造体を定義する**構文である。

```lean
structure Point where
  x : Nat
  y : Nat

structure NamedPoint extends Point where
  name : String

def home : NamedPoint := { x := 2, y := 3, name := "home" }

example : home.x = 2 := rfl
example : home.name = "home" := rfl
```

`NamedPoint` は、親の `x`・`y` と、自分で追加した `name` を持つ。値の構築では親のフィールドも名前で指定できる。

親の値は、生成された `toPoint` で取り出せる。親の型を受け取る関数には、その射影で取り出した値を渡す。

```lean
structure Point where
  x : Nat
  y : Nat

structure NamedPoint extends Point where
  name : String

def coordinateSum (p : Point) : Nat := p.x + p.y

def home : NamedPoint := { x := 2, y := 3, name := "home" }

example : home.toPoint = (⟨2, 3⟩ : Point) := rfl
example : coordinateSum home.toPoint = 5 := rfl
```

`coordinateSum home.toPoint` では、`NamedPoint` から `Point` の部分を取り出して渡す。この `extends` だけで、子の値を親の型へ自動変換するインスタンスが登録されるわけではない。

複数の親はカンマで並べる。

```lean
structure HasPosition where
  x : Nat

structure HasName where
  name : String

structure Item extends HasPosition, HasName where
  enabled : Bool

def item : Item := { x := 3, name := "sample", enabled := true }

example : item.toHasName.name = "sample" := rfl
```

`extends` はフィールドや親への射影を引き継ぐ仕組みである。親の名前空間にあるすべての定義を、子の名前空間へコピーするものではない。

構造体の基本的な構築と更新は [`structure`](structure.md) を参照。

参照：[公式リファレンス：Inductive Types / Structure Inheritance](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

[文法要素の一覧に戻る](README.md)
