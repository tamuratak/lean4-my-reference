# `try`

`try` は、**指定したタクティクスを試し、失敗したら何もせず先へ進む**タクティクスである。

成功すればその結果を使い、失敗すれば試す前の状態に戻る。

```lean
example (P : Prop) (hp : P) : P := by
  try rfl
  exact hp
```

この例で `rfl` が失敗しても、証明全体は止まらない。

成功してゴールが閉じた後に、さらにタクティクスを書くと「ゴールがない」というエラーになることがある。複数ゴールにまとめて試すなら `all_goals try ...` のような形も使える。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
