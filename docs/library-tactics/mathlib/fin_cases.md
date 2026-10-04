# `fin_cases`

`fin_cases` は、**有限型の値を、取り得る具体的な値ごとに場合分けする**タクティクスである。`Fin n` など、有限個の値をすべて調べて証明したいときに使う。

```lean
import Mathlib.Tactic.FinCases
import Mathlib.Data.Fintype.Fin

example (i : Fin 2) : i = 0 ∨ i = 1 := by
  fin_cases i <;> simp
```

`i = 0` の場合と `i = 1` の場合が作られ、それぞれ具体的な値について証明する状態になる。

```lean
import Mathlib.Tactic.FinCases
import Mathlib.Data.Fintype.Fin

example (i : Fin 3) : i.val ≤ 2 := by
  fin_cases i <;> decide
```

ここでは値 `0`・`1`・`2` の三つの場合になる。Lean 本体の `cases` はコンストラクターに沿った分解だが、`fin_cases` は有限個の要素に沿った列挙である。

範囲が大きいとゴールが大量に増える。自然数や整数の上下限から値を列挙するなら [interval_cases](interval_cases.md)、列挙せず算術で証明できるなら [omega](../../tactics/omega.md) が向いている。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
