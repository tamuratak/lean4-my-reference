# `congr!`

`congr!` は、等式を対応する部分式の等式へ分解し、反射性などで解ける部分も処理するタクティクスである。Lean 本体の `congr` を使う場面で、mathlib の強化された分解を利用したいときに使う。

```lean
import Mathlib.Tactic.CongrExclamation

example (f : Nat → Nat) (a b : Nat) : f (a + b) = f (b + a) := by
  congr! 1
  exact Nat.add_comm a b
```

関数 `f` が共通なので、引数についてのゴール `a + b = b + a` が残る。`1` は分解の深さを指定している。

```lean
import Mathlib.Tactic.CongrExclamation

example (f : Nat → Nat) (a b : Nat) (h : a = b) : (f a, a) = (f b, b) := by
  congr! 2 <;> exact h
```

組の成分と関数の引数を分解する。`congr!` が仮定を使ってその場で閉じることもある。分解しすぎると不要なゴールが増える場合があるので、深さを指定して使える。

構造の外延性の定理を利用するなら Lean 本体の [ext](../../tactics/ext.md)、不等式を単調性で分解するなら [gcongr](gcongr.md) を使う。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
