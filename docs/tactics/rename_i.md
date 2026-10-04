# `rename_i`

`rename_i` は、**Lean が内部的に付けた、直接使いにくい名前を付け直す**タクティクスである。

`intro` で名前を省略した場合などに使える。

```lean
example (P : Prop) : P → P := by
  intro
  rename_i hp
  exact hp
```

複数の内部名をまとめて指定することもできる。名前が既に分かっている変数には `rename 型 => newName` を使う。

```lean
example (P : Prop) (hp : P) : P := by
  rename P => h
  exact h
```

最初から名前を選べるなら、`intro hp` や `cases h with ...` と導入時に付ける方が分かりやすい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
