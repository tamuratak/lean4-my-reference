# `exists`

`exists` は、存在命題のゴールで、具体的な証人を指定するタクティクスである。

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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`exists`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticExists_%2C%2C)。

[タクティクス一覧に戻る](README.md)
