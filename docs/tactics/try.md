# `try`

`try` は、指定したタクティクスを試し、失敗したら何もせず先へ進むタクティクスである。

成功すればその結果を使い、失敗すれば試す前の状態に戻る。

```lean
example (P : Prop) (hp : P) : P := by
  try rfl
  exact hp
```

この例で `rfl` が失敗しても、証明全体は止まらない。

成功してゴールが閉じた後に、さらにタクティクスを書くと「ゴールがない」というエラーになることがある。複数ゴールにまとめて試すなら `all_goals try ...` のような形も使える。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`try`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticTry_)。

[タクティクス一覧に戻る](README.md)
