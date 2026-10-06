# `and_intros`

`and_intros` は、ゴールに入れ子で現れる論理積を、まとめて分解するタクティクスである。

`constructor` を繰り返す代わりに使える。

```lean
example (P Q R : Prop) (hp : P) (hq : Q) (hr : R) : P ∧ Q ∧ R := by
  and_intros
  · exact hp
  · exact hq
  · exact hr
```

残るゴールは `P`、`Q`、`R` の三つである。仮定にある論理積を取り出す用途には、`rcases` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`and_intros`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticAnd_intros)。

[タクティクス一覧に戻る](README.md)
