# `linear_combination`

`linear_combination` は、等式に掛ける係数と足し引きを指定して、ゴールの等式を導くタクティクスである。自動で組み合わせを探す `linarith` と違い、どの等式をどう使うかを証明に書く。

```lean
import Mathlib.Tactic.LinearCombination

example (x y : Int) (h₁ : x + y = 3) (h₂ : x - y = 1) : 2*x = 4 := by
  linear_combination h₁ + h₂
```

`h₁` と `h₂` の両辺をそれぞれ加えると `y` が消え、ゴールの等式になる。

```lean
import Mathlib.Tactic.LinearCombination

example (x y : Int) (h₁ : x + y = 3) (h₂ : x + 2*y = 5) : x = 1 := by
  linear_combination 2*h₁ - h₂
```

ここでは `2*(x+y) - (x+2*y) = 2*3 - 5` を整理する。指定した組み合わせとゴールの差を、既定では環の正規化で確認する。

組み合わせの係数を自動で見つけたいなら [linarith](linarith.md)、仮定を使わず多項式の恒等式を証明したいなら [ring](ring.md) を使う。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用）。

[mathlib タクティクス一覧に戻る](README.md)
