# `inductive`

`inductive` は、**値を作る方法をコンストラクターとして列挙し、新しい型を定義する**構文である。

```lean
inductive Color where
  | red
  | blue

def code (c : Color) : Nat :=
  match c with
  | .red => 0
  | .blue => 1

example : code Color.blue = 1 := rfl
```

`Color` の値は `Color.red` または `Color.blue` である。`match` の `.red` と `.blue` は、期待される型 `Color` から名前空間を補う記法である。

コンストラクターは、型で指定した値を受け取ることもできる。

```lean
inductive Result where
  | ok (value : Nat)
  | error (message : String)

def valueOrZero (r : Result) : Nat :=
  match r with
  | .ok n => n
  | .error _ => 0

example : valueOrZero (Result.ok 7) = 7 := rfl
```

`Result.ok` の型は `Nat → Result`、`Result.error` の型は `String → Result` になる。`|` は新しいコンストラクターの区切りである。

定義している型自身を成分に持たせると、再帰的な構造を作れる。

```lean
inductive Tree where
  | leaf (value : Nat)
  | node (left right : Tree)

def sample : Tree := .node (.leaf 1) (.leaf 2)
```

`Tree.node` に二つの `Tree` を渡して、より大きな木を作る。帰納型にはコンストラクター以外に、場合分けや帰納法のための原理も生成される。

成分を一つの形にまとめる型には [`structure`](structure.md) が便利である。

互いを成分として使う型の定義は [`mutual`](mutual.md)、インスタンスの自動生成は [`deriving`](deriving.md) を参照。

参照：[公式リファレンス：Inductive Types](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

[文法要素の一覧に戻る](README.md)
