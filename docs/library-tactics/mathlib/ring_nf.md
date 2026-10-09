# `ring_nf`

`ring_nf` は、ゴールや仮定にある多項式を標準形へ整理するタクティクスである。`ring` は等式を閉じることを目的とするのに対し、`ring_nf` は不等式や仮定の中でも式を変形できる。

```lean
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

example (x : Int) (h : 0 < x) : x + x > 0 := by
  ring_nf
  linarith
```

`ring_nf` の後、ゴールは `0 < x * 2` という形に整理される。正であることの判断は、後続の `linarith` が仮定 `h` を使って行う。

仮定を整理するには `at h` を付ける。

```lean
import Mathlib.Tactic.Ring

example (x : Int) (h : (x + 1)^2 = 0) : 1 + x * 2 + x^2 = 0 := by
  ring_nf at h
  exact h
```

標準形の項の順番は入力やバージョンによって変わり得る。多項式の等式をただ証明したいなら [ring](ring.md) の方が意図を直接表せる。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用）。

[mathlib タクティクス一覧に戻る](README.md)
