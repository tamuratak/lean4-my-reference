# `abel`

`abel` は、**可換な加法の式を整理して等式を証明する**タクティクスである。加法の結合則・交換則、可換群では減算や逆元も利用する。

```lean
import Mathlib.Tactic.Abel

example (G : Type) [AddCommGroup G] (a b c : G) : a + b - a + c = b + c := by
  abel
```

左辺の `a` と `-a` が相殺され、残る項が右辺と一致するのでゴールが閉じる。乗法を持たない型でも使える。

```lean
import Mathlib.Tactic.Abel

example (a b c : Int) : a + (b + c) = c + a + b := by
  abel
```

`abel_nf` は式を標準形へ変形し、後続の証明へ渡す変種である。`abel_nf at h` なら仮定を整理する。

加法に注目した操作なので、分配法則を使って `a*(b+c)` を展開するには [ring](ring.md) を使う。単なる結合則・交換則による並べ替えなら Lean 本体の [ac_rfl](../../tactics/ac_rfl.md) も使える。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
