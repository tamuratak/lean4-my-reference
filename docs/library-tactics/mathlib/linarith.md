# `linarith`

`linarith` は、仮定にある線形な等式・不等式を組み合わせ、算術のゴールを証明するタクティクスである。ゴールを否定した条件と仮定から矛盾を導くので、成功すると証明が完了する。

```lean
import Mathlib.Tactic.Linarith

example (x y : Int) (h₁ : x ≤ y) (h₂ : y < 5) : x < 5 := by
  linarith
```

手で `x ≤ y < 5` という推移性の証明を書く操作をまとめている。数値係数を含む条件も扱える。

```lean
import Mathlib.Tactic.Linarith

example (x y : Int) (h₁ : 2*x + y = 7) (h₂ : y = 3) : x = 2 := by
  linarith only [h₁, h₂]
```

`only [h₁, h₂]` は、利用する局所的な事実を指定したものに絞る。`linarith [補助的な証明]` は、通常の仮定に加えてその事実も使う。

`x*y` や `x^2` のような項の算術的な関係までは、線形推論だけではわからない。[nlinarith](nlinarith.md) は非線形の補助条件も作る。自然数・整数の離散的な条件には Lean 本体の [omega](../../tactics/omega.md) も候補になる。Lean 本体の `grind_linarith` と mathlib の `linarith` は別のタクティクスである。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
