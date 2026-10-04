# `focus`

`focus` は、**現在の先頭のゴールにだけ注目して、内側の証明を進める**タクティクスである。

複数のゴールがあっても、内側の `all_goals` などが他のゴールに触れないようにできる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  focus
    exact hp
  exact hq
```

この例では `focus` 内で `P` だけを証明し、ブロックの外で `Q` を証明する。

`focus` は選んだゴールを完全に閉じることまでは要求しない。`·` のブロックは、通常そのブロック内で選んだゴールを閉じるために使う。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
