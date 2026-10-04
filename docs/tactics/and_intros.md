# `and_intros`

`and_intros` は、**ゴールに入れ子で現れる論理積を、まとめて分解する**タクティクスである。

`constructor` を繰り返す代わりに使える。

```lean
example (P Q R : Prop) (hp : P) (hq : Q) (hr : R) : P ∧ Q ∧ R := by
  and_intros
  · exact hp
  · exact hq
  · exact hr
```

残るゴールは `P`、`Q`、`R` の三つである。仮定にある論理積を取り出す用途には、`rcases` を使う。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
