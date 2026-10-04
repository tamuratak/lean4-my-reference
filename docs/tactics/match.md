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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`match`](https://lean-lang.org/doc/api/Lean/Parser/Tactic.html#Lean.Parser.Tactic.match)。

[タクティクス一覧に戻る](README.md)
