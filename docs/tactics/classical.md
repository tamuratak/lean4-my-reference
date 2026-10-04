# `classical`

`classical` は、**古典論理に基づく判定可能性などを、後続の証明で使えるようにする**タクティクスである。

任意の命題 `P` について `P` と `¬ P` に分けたいときに使う。

```lean
example (P : Prop) : P ∨ ¬ P := by
  classical
  by_cases h : P
  · exact Or.inl h
  · exact Or.inr h
```

`classical` 自体がこのゴールを証明するわけではない。後続の `by_cases` などが必要とする古典的な判定を利用できるようにする。

数値の比較や有限の計算を扱う証明では、既に判定方法があるため不要なことも多い。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`classical`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.classical)。

[タクティクス一覧に戻る](README.md)
