# `guard_target`

`guard_target` は、**ゴールが想定した型になっていることを確認する**タクティクスである。

証明の途中で状態を確かめるために使う。

```lean
example (P : Prop) : P → P := by
  intro hp
  guard_target = P
  guard_hyp hp : P
  exact hp
```

`guard_target` はゴール、`guard_hyp` は仮定の型や値を確認する。想定と違えば、その場所でエラーになる。

式どうしを調べる関連タクティクスとして `guard_expr` がある。

```lean
example : True := by
  guard_expr (2 + 2 : Nat) = 4
  trivial
```

これらは確認用で、ゴールを証明する操作ではない。ここでの `=` は定義上の等しさによる照合を指定する。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
