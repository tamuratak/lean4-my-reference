# `omega`

`omega` は、**自然数や整数の線形な等式・不等式を使って、算術的なゴールを証明する**タクティクスである。

仮定の不等式を組み合わせる例である。

```lean
example (n m : Nat) (h : n ≤ m) : n ≤ m + 3 := by
  omega

example (n : Int) (h : n < 5) : n ≤ 4 := by
  omega
```

自然数の引き算のように、ゼロで止まる計算も扱える。

```lean
example (n : Nat) (h : 3 ≤ n) : n - 3 + 3 = n := by
  omega
```

定数倍を含む線形算術が主な対象である。変数どうしの積 `n * m` などの非線形な関係を、一般に解くタクティクスではない。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
