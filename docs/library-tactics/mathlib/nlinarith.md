# `nlinarith`

`nlinarith` は、積や平方を含む条件から補助的な不等式を作り、線形算術の推論へ渡すタクティクスである。平方の非負性などを利用して、`linarith` だけでは足りないゴールを閉じる。

```lean
import Mathlib.Tactic.Linarith

example (x : Int) : 0 ≤ x^2 + 1 := by
  nlinarith
```

ゴールに含まれる平方について `0 ≤ x^2` という事実を利用し、そこに `1` を加えても非負であることを証明する。

```lean
import Mathlib.Tactic.Linarith

example (x : Int) (h : x^2 ≤ 0) : x = 0 := by
  nlinarith
```

補助条件を明示する `nlinarith [証明]` や、利用する仮定を絞る `nlinarith only [h]` も使える。

任意の非線形問題を解く完全な手続きではない。必要な積や平方についての事実を別途渡す方がよい場合もある。多項式の等式そのものを整理するだけなら [ring](ring.md)、式の正・非負を構造から調べるなら [positivity](positivity.md) が向いている。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
