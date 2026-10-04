# `exact`

`exact` は、**ゴールそのものの証明を渡して、そのゴールを閉じる**タクティクスである。

`hp : P` があり、ゴールも `P` なら、`exact hp` で証明が終わる。

```lean
example (P : Prop) (hp : P) : P := by
  exact hp

example (P Q : Prop) (hp : P) (h : P → Q) : Q := by
  exact h hp
```

`h hp` は、`P → Q` の証明 `h` に `P` の証明 `hp` を渡して作った、`Q` の証明である。

`exact` は残りの前提を自動で証明しない。前提を別のゴールとして残したい場合は `apply` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`exact`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.exact)。

[タクティクス一覧に戻る](README.md)
