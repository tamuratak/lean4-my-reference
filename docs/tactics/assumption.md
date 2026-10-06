# `assumption`

`assumption` は、現在の仮定から、ゴールをそのまま証明できるものを探すタクティクスである。

ゴールが `P` で、仮定に `hp : P` があれば `assumption` で閉じられる。

```lean
example (P Q : Prop) (hq : Q) (hp : P) : P := by
  assumption
```

仮定の名前を覚えていなくても使える。ただし、`P → Q` と `P` を組み合わせて `Q` を証明するような探索は行わない。その場合は `exact h hp` や `apply_assumption` を使う。

```lean
example (P Q : Prop) (h : P → Q) (hp : P) : Q := by
  apply h
  assumption
```

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`assumption`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.assumption)。

[タクティクス一覧に戻る](README.md)
