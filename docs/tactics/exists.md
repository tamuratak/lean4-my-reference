# `exists`

`exists` は、**存在命題のゴールで、具体的な証人を指定する**タクティクスである。

ゴールが `∃ n : Nat, n = 3` のとき、`exists 3` と書くと、証人が `3` に決まる。

```lean
example : ∃ n : Nat, n = 3 := by
  exists 3
```

`exists` は証人を入れた後に簡単なゴールを `trivial` で閉じることも試す。この例の `3 = 3` は自動で閉じる。

条件が残る例では、その条件を続けて証明する。

```lean
example (P : Nat → Prop) (h : P 1 → P 3) (h1 : P 1) : ∃ n, P n := by
  exists 3
  apply h
  exact h1
```

自動で閉じるかどうかに頼らず課題を明示するなら、`refine ⟨3, ?_⟩` と書くこともできる。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
