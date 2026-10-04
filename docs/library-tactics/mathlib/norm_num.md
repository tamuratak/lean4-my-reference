# `norm_num`

`norm_num` は、**具体的な数の計算と、その結果に関する等式・不等式を証明する**タクティクスである。四則演算や冪などを計算し、数値についてのゴールならその場で閉じられる。

```lean
import Mathlib.Tactic.NormNum

example : (7 : Int)^2 + 3 * 5 = 64 := by
  norm_num

example : (12 : Int) < 3^3 := by
  norm_num
```

変数があっても、式に含まれる数値の部分を整理できる。`at h` で仮定を対象にする。

```lean
import Mathlib.Tactic.NormNum

example (x : Int) (h : x = 2 + 3 * 4) : x = 14 := by
  norm_num at h
  exact h
```

この操作の後、仮定は `h : x = 14` になる。変数を含む多項式の恒等式には [ring](ring.md)、仮定を使う線形不等式には [linarith](linarith.md) を選ぶ。`norm_num [定義名]` で定義を展開しながら計算することもできる。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
