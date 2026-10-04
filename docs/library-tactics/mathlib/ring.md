# `ring`

`ring` は、**可換な環や半環の演算で書かれた多項式の等式を、両辺を同じ標準形にして証明する**タクティクスである。展開・同類項の整理・項の並べ替えをまとめて行い、成功するとゴールを閉じる。

```lean
import Mathlib.Tactic.Ring

example (x y : Int) : (x + y)^2 = x^2 + 2*x*y + y^2 := by
  ring
```

`rw` で分配法則を一つずつ指定する必要はない。変数があっても多項式として扱える。

```lean
import Mathlib.Tactic.Ring

example (x y : Nat) : (x + y) * (x + y) = x*x + 2*x*y + y*y := by
  ring
```

自然数の減算は環の減算とは異なり、一般には多項式の演算として整理できない。変数を含む除算や不等式を解くためのタクティクスでもない。

仮定の等式を組み合わせたいなら [linear_combination](linear_combination.md)、分母を払いたいなら [field_simp](field_simp.md) を使う。[ring_nf](ring_nf.md) は証明を閉じるだけでなく、式を整理して後続の操作へ渡したい場合に使う。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
