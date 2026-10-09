# `tauto`

`tauto` は、仮定やゴールの命題論理の構造を調べ、論理的に成り立つ結論を証明するタクティクスである。論理積・論理和・含意・否定などを分解し、必要な場合分けも行う。

```lean
import Mathlib.Tactic.Tauto

example (P Q : Prop) : P ∧ (P → Q) → Q := by
  tauto
```

前提から `P` と `P → Q` を取り出し、それらを組み合わせれば `Q` を証明できるので、ゴールが閉じる。

```lean
import Mathlib.Tactic.Tauto

example (P Q : Prop) : ¬ (P ∨ Q) ↔ ¬ P ∧ ¬ Q := by
  tauto
```

命題内部の算術や関数の性質を解析することが目的ではない。例えば `x < y` を一つの命題として扱っても、その数値的な意味から別の不等式を導くわけではない。

論理構造の自動化だけで十分なら `tauto`、追加の補題を登録して探索したいなら Aesop の [aesop](../aesop/aesop.md)、算術の条件なら [linarith](linarith.md) などを選ぶ。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用）。

[mathlib タクティクス一覧に戻る](README.md)
