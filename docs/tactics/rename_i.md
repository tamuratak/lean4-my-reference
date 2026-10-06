# `rename_i`

`rename_i` は、Lean が内部的に付けた、直接使いにくい名前を付け直すタクティクスである。

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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`rename_i`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.renameI)。

[タクティクス一覧に戻る](README.md)
