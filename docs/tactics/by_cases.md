# `by_cases`

`by_cases` は、**命題が成り立つ場合と、成り立たない場合に分ける**タクティクスである。

`by_cases h : P` と書くと、次の二つの場合を証明することになる。

```text
h : P       ⊢ 元のゴール
h : ¬ P     ⊢ 元のゴール
```

```lean
example (P : Prop) : P ∨ ¬ P := by
  classical
  by_cases h : P
  · exact Or.inl h
  · exact Or.inr h
```

任意の命題を場合分けするため、この例では `classical` を使う。自然数の等式など、判定可能な命題なら不要である。

`cases h` は既にある値をコンストラクターで分解するが、`by_cases h : P` は命題の真偽を新しく場合分けする。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
