# `generalize`

`generalize` は、**式を新しい変数に置き換え、必要なら元の式との等式を残す**タクティクスである。

`generalize h : n + 1 = k` と書くと、ゴールにある `n + 1` が `k` に置き換わり、`h : n + 1 = k` が追加される。

```lean
example (n : Nat) : n + 1 = n + 1 := by
  generalize h : n + 1 = k
  rfl
```

元の式との関係が必要なときは、等式の名前を付けておく。

```lean
example (n : Nat) : n + 1 > 0 := by
  generalize h : n + 1 = k
  omega
```

`generalize n + 1 = k` と名前を省略すると、その等式は残らない。式を変数にした後で `cases k` などを使いたいときに役立つ。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
