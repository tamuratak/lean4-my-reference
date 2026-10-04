# `gcongr`

`gcongr` は、**登録された単調性などの補題を使い、大小関係のゴールを部分式の関係へ分解する**タクティクスである。等式だけを分解する `congr` と違い、不等式にも使う。

```lean
import Mathlib.Tactic.GCongr
import Mathlib.Data.Real.Basic

example (a b : Real) (h : a ≤ b) : a + 3 ≤ b + 3 := by
  gcongr
```

加法の単調性から必要な条件が `a ≤ b` へ減り、手元の仮定 `h` が使われるので、この例ではゴールが閉じる。

```lean
import Mathlib.Tactic.GCongr
import Mathlib.Data.Real.Basic

example (a b c d : Real) (h₁ : a ≤ b) (h₂ : c ≤ d) : a + c ≤ b + d := by
  gcongr
```

乗法や冪では、単調性のために非負などの追加条件が必要になることがある。その条件が自動で解けなければゴールとして残る。

仮定の不等式をまとめて算術的に推論する [linarith](linarith.md) とは違い、式の形に沿って分解する。使える演算は、必要な一般化合同補題がインポートされているかによる。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
