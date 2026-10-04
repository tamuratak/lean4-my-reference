# `mutual … end`

`mutual … end` は、**互いの名前を使う複数の関数や型を、一つのまとまりとして定義する**構文である。

```lean
mutual
  def evenFlag : Nat → Bool
    | 0 => true
    | n + 1 => oddFlag n

  def oddFlag : Nat → Bool
    | 0 => false
    | n + 1 => evenFlag n
end

example : evenFlag 4 = true := rfl
example : oddFlag 4 = false := rfl
```

`evenFlag` は一つ小さい入力で `oddFlag` を呼び、`oddFlag` は一つ小さい入力で `evenFlag` を呼ぶ。同じブロックに置くことで、先に書いた関数から後の関数も参照できる。

各再帰呼び出しで入力が小さくなるので、この例は構造的な再帰として停止が確認される。`mutual` は停止条件を省略する指定ではない。

型どうしが互いを成分として使う場合にも使える。

```lean
mutual
  inductive Tree where
    | leaf (value : Nat)
    | node (children : Forest)

  inductive Forest where
    | nil
    | cons (first : Tree) (rest : Forest)
end

def sample : Tree :=
  .node (.cons (.leaf 1) (.cons (.leaf 2) .nil))

#check sample
```

`Tree.node` は木の集まり `Forest` を受け取り、`Forest.cons` は一つの `Tree` と残りの `Forest` を受け取る。

相互に定義する帰納型には、通常の帰納型に加えて、共通のパラメーターや型の階層などに制約がある。単に宣言をまとめたいだけで、互いの参照がない場合には `mutual` は必要ない。

関数の再帰は[再帰のページ](recursive.md)、型の基本形は [`inductive`](inductive.md) を参照。

参照：[公式リファレンス：Recursive Definitions / Mutual Recursion](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/)、[公式リファレンス：Inductive Types / Mutual Inductive Types](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

[文法要素の一覧に戻る](README.md)
