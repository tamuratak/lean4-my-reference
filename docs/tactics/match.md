# `match`

`match` は、**値の形ごとに、タクティクスの証明を分ける**タクティクスである。

式の `match` と同じように、コンストラクターのパターンで分岐できる。

```lean
example (b : Bool) : b = false ∨ b = true := by
  match b with
  | false => exact Or.inl rfl
  | true => exact Or.inr rfl
```

各分岐では、そのパターンの値についてゴールを証明する。任意の帰納型を分解する用途では `cases` も使える。

既にゴールの式に含まれる `match` の分岐を分けたい場合は `split` が便利である。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
