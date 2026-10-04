# `specialize`

`specialize` は、**全称命題や含意の仮定に引数を渡し、具体化した仮定に置き換える**タクティクスである。

`h : ∀ n, P n` に対して `specialize h 3` とすると、`h` が `P 3` の証明になる。

```lean
example (P : Nat → Prop) (h : ∀ n, P n) : P 3 := by
  specialize h 3
  exact h
```

含意にも使える。

```lean
example (P Q : Prop) (h : P → Q) (hp : P) : Q := by
  specialize h hp
  exact h
```

元の一般的な仮定も残したいなら、`have h3 := h 3` のように別名で事実を追加する。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
