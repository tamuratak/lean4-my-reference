# `induction`

`induction` は、**帰納型の値について場合分けし、再帰的な成分について帰納法の仮定を作る**タクティクスである。

自然数では、ゼロの場合と後者の場合に分かれる。後者の場合には、小さい自然数についての結論を使える。

```lean
example (n : Nat) : 0 + n = n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    change Nat.succ (0 + n) = Nat.succ n
    rw [ih]
```

`succ` の場合の `ih` は `0 + n = n` の証明である。これを使って `n + 1` の場合を示す。

`cases` との違いは、この `ih` が手に入ることである。証明したい命題に他の変数が依存する場合は、`induction n generalizing ...` で帰納法の仮定を一般化することもある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`induction`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.induction)。

[タクティクス一覧に戻る](README.md)
