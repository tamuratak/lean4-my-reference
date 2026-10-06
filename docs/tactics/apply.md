# `apply`

`apply` は、結論がゴールに合う定理を使い、その前提を新しいゴールにするタクティクスである。

例えば、`h : P → Q` があり、ゴールが `Q` のとき、`apply h` と書くとゴールが `P` になる。

```lean
example (P Q : Prop) (h : P → Q) (hp : P) : Q := by
  apply h
  exact hp
```

前提が複数なら、複数のゴールができる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  apply And.intro
  · exact hp
  · exact hq
```

つまり、`exact` が完成した証明を渡すのに対し、`apply` は「この定理で証明するには何が必要か」を取り出す。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`apply`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.apply)。

[タクティクス一覧に戻る](README.md)
