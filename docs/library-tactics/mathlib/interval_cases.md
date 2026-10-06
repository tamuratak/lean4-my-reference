# `interval_cases`

`interval_cases n` は、自然数や整数の変数について、仮定にある上下限から取り得る値を列挙するタクティクスである。有限な区間に限られた変数を、具体的な値ごとのゴールに分ける。

```lean
import Mathlib.Tactic.IntervalCases

example (n : Int) (h₁ : 1 ≤ n) (h₂ : n ≤ 3) : n = 1 ∨ n = 2 ∨ n = 3 := by
  interval_cases n <;> norm_num
```

`n = 1`・`n = 2`・`n = 3` の三つの場合になり、数値についてのゴールを `norm_num` で閉じる。

```lean
import Mathlib.Tactic.IntervalCases

example (n : Nat) (h : n < 3) : n^2 ≤ 4 := by
  interval_cases n <;> norm_num
```

自然数の下限は `0` なので、ここでは `0`・`1`・`2` を調べる。変数の値が確定すると、冪を含む条件も数値計算で扱える。

整数なら有限な上下限、自然数なら有限な上限が必要になる。大きな区間の列挙は非効率なので、線形な条件だけで証明できる場合は Lean 本体の [omega](../../tactics/omega.md) を先に考える。有限型を列挙する [fin_cases](fin_cases.md) とは入力の形が異なる。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
