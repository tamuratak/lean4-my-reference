# `decide`

`decide` は、**命題の判定手続きを計算して、真であることを証明する**タクティクスである。

自然数の具体的な比較など、計算で判定できる命題に使う。

```lean
example : 3 < 5 := by
  decide

example : (2 : Nat) ≠ 3 := by
  decide
```

有限個の要素すべてを調べられる型でも使える。

```lean
example : ∀ b : Bool, b = false ∨ b = true := by
  decide
```

`Decidable` による判定方法が必要である。任意の自然数変数を含む算術命題を、一般に `decide` で解けるわけではない。そうした場合は `omega` を使う。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
