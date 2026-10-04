# `trivial`

`trivial` は、**仮定、反射性、簡単化などで閉じられる簡単なゴールを試す**タクティクスである。

`True` や、手元に証明がある命題などに使える。

```lean
example : True := by
  trivial

example (P : Prop) (hp : P) : P := by
  trivial
```

簡単な論理積も扱える。

```lean
example (P : Prop) (hp : P) : P ∧ True := by
  trivial
```

名前は「自明」という意味だが、あらゆる短い証明を探すわけではない。使っている事実を明示したい場合は `exact hp` や `rfl` を選ぶ。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
