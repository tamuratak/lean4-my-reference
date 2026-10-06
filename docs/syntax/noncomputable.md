# `noncomputable`

`noncomputable` は、論理上の定義として使い、実行用のコード生成から除外する修飾子である。

例えば、値が存在することから、選択公理で一つの値を選ぶ定義に使う。

```lean
noncomputable def chooseElement (α : Type) [Nonempty α] : α :=
  Classical.choice inferInstance

#check chooseElement Nat
```

`Nonempty α` は「`α` の値が存在する」という命題である。`Classical.choice` はその証明から値を選ぶが、実行可能な選択手順を与えるものではない。

存在命題から証人を選び、その性質を証明する用途にも使える。

```lean
noncomputable def witness (P : Nat → Prop) (h : ∃ n, P n) : Nat :=
  Classical.choose h

theorem witness_spec (P : Nat → Prop) (h : ∃ n, P n) :
    P (witness P h) := Classical.choose_spec h
```

`witness P h` は `P` を満たす自然数を表す。値を `#eval` で実行して求めることはできないが、選んだ値が `P` を満たすという証明には使える。

複数の定義に対しては `noncomputable section` で範囲を指定できる。

```lean
noncomputable section

def chooseElement (α : Type) [Nonempty α] : α :=
  Classical.choice inferInstance

end
```

`noncomputable` は型の確認や再帰の停止条件を省略する指定ではない。また、証明で古典論理を使ったというだけで、すべての定義に必要になるわけではない。ここでは、計算の結果として必要なデータを実行不能な方法で取り出している。

[`opaque`](opaque_axiom.md) の「証明の計算で本体を展開しない」という指定とは違う。`opaque` は実行可能な本体を持つこともできる。

参照：[公式リファレンス：Modifiers](https://lean-lang.org/doc/reference/latest/Definitions/Modifiers/)。

[文法要素の一覧に戻る](README.md)
