# `structure`・フィールド・更新

`structure` は、複数の名前付きの成分をまとめる型を定義する構文である。

```lean
structure Point where
  x : Nat
  y : Nat

def origin : Point := { x := 0, y := 0 }

example : origin.x = 0 := rfl
example : origin.y = 0 := rfl
```

`Point` が新しい型、`x` と `y` がフィールドである。`origin.x` のように書くと成分を取り出せる。

値を作るには、フィールド名で指定するほか、コンストラクターや [`⟨…⟩`](anonymous_constructor.md) も使える。

```lean
structure Point where
  x : Nat
  y : Nat

example : (Point.mk 2 3).x = 2 := rfl
example : (⟨2, 3⟩ : Point).y = 3 := rfl

def p : Point where
  x := 2
  y := 3

example : p.x = 2 := rfl
```

既定のコンストラクター名は `Point.mk` である。位置で成分を渡す記法では、フィールドの宣言順を使う。`def p : Point where …` は、フィールドを複数行で指定する別の書き方である。

`{ p with x := … }` は、一部のフィールドを変えた新しい値を作る。

```lean
structure Point where
  x : Nat
  y : Nat

def moveRight (p : Point) : Point := { p with x := p.x + 1 }

example : moveRight ⟨2, 3⟩ = (⟨3, 3⟩ : Point) := rfl
```

元の `p` を変更する操作ではなく、`y` を引き継いだ別の値を返す。

複数の形を持つ型や再帰的な型を定義する場合は [`inductive`](inductive.md) を使う。

既存の構造体のフィールドを引き継ぐ [`extends`](extends.md) と、インスタンスを自動生成する [`deriving`](deriving.md) も使える。

参照：[公式リファレンス：Inductive Types / Structures](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

[文法要素の一覧に戻る](README.md)
