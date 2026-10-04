# `assumption`

`assumption` は、**現在の仮定から、ゴールをそのまま証明できるものを探す**タクティクスである。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
