# `apply_ext_theorem`

`apply_ext_theorem` は、**ゴールに合う外延性の定理を適用する**タクティクスである。

外延性の定理を適用する部分だけを行い、引数の導入などは自分で続ける。

```lean
example (f g : Nat → Nat) (h : ∀ n, f n = g n) : f = g := by
  apply_ext_theorem
  intro n
  exact h n
```

関数の例では、定理の適用によって各入力で値が等しいことを示すゴールになる。

普通の証明では `funext n` や `ext n` の方が短く、何を導入するかも明示できる。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
