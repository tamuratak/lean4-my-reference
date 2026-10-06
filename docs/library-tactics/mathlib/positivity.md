# `positivity`

`positivity` は、式の構造と仮定から、正・非負・非零であることを証明するタクティクスである。正の数の和、平方の非負性など、登録された規則を再帰的に使う。

```lean
import Mathlib.Tactic.Positivity

example (x : Int) : 0 < x^2 + 1 := by
  positivity
```

`x^2` は非負、`1` は正なので、その和が正であると判断し、ゴールを閉じる。

```lean
import Mathlib.Tactic.Positivity

example (x y : Int) (hx : 0 < x) (hy : 0 < y) : x * y ≠ 0 := by
  positivity
```

仮定の正値性から積が正であることがわかり、非零というゴールも証明できる。

任意の不等式の大小を比較するタクティクスではない。`x ≤ y` のような関係には [linarith](linarith.md) などを使う。どの演算を扱えるかは、その型や演算についての規則が登録されているかによる。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
