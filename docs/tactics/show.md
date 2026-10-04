# `show`

`show` は、**証明したいゴールを、型を書いて選び直す**タクティクスである。

現在のゴールを定義上等しい形で明示する用途に使える。

```lean
example (n m : Nat) (h : n = m) : n + 0 = m := by
  show n = m
  exact h
```

複数のゴールがある場合は、指定した型に合うゴールを探して先頭に移す。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  show Q
  exact hq
  exact hp
```

`change` は主に現在のゴールや指定した仮定の書き方を変える操作、`show` は証明したい型を明示してゴールを選ぶ操作と考えるとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
