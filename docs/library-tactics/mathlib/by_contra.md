# `by_contra`・`by_contra!`

`by_contra h` は、ゴールの否定を仮定 `h` として導入し、ゴールを `False` に変えるタクティクスである。追加ライブラリの通常の `by` 証明で使う背理法をここで扱う。

```lean
import Mathlib.Tactic.ByContra

example (P : Prop) (h : ¬ ¬ P) : P := by
  by_contra hn
  exact h hn
```

操作後の状態は次のようになる。

```text
h  : ¬ ¬ P
hn : ¬ P
⊢ False
```

`by_contra!` は、導入した否定をさらに `push_neg` で整理する。

```lean
import Mathlib.Tactic.ByContra
import Mathlib.Tactic.Linarith

example (x : Int) (h : x < 0) : ¬ 0 ≤ x := by
  by_contra! hn
  linarith
```

この例では `hn : 0 ≤ x` を得て矛盾を示す。古典論理が必要な場合の準備もタクティクスが行う。

Lean 本体の [false_or_by_contra](../../tactics/false_or_by_contra.md) や `grind` 内の `by_contra` とは構文や操作を区別する。`by_contra` 自体は Batteries 由来で、mathlib のインポートを通じても利用できる。否定の整理だけなら [push_neg](push_neg.md) を使う。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用）。

[mathlib タクティクス一覧に戻る](README.md)
