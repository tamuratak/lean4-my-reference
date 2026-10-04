# `field_simp`

`field_simp` は、**体の除算・逆数を含む式で、分母の非零を確認しながら分母を払う**タクティクスである。分数を含むゴールを、除算を含まない等式へ変えるために使う。

```lean
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

example (x y : Real) (hy : y ≠ 0) : (x + 1) / y = x / y + 1 / y := by
  field_simp
  <;> ring
```

分母 `y` の非零には仮定 `hy` を利用する。分母を払った後に残る多項式の等式は `ring` で閉じる。

利用する非零の証明を明示することもできる。

```lean
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp

example (x : Real) (hx : x ≠ 0) : x / x = 1 := by
  field_simp [hx]
```

Lean では `0` による除算も定義されているため、分母を無条件に払ってよいわけではない。非零を確認できない場合は、その条件の証明が必要になる。`field_simp at h` は仮定の中の分数を整理する。[ring](ring.md) 単独では変数を含む分母を払えない。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
