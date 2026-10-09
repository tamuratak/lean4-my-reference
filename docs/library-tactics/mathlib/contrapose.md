# `contrapose`

`contrapose h` は、仮定 `h : P` とゴール `Q` を、仮定 `h : ¬ Q` とゴール `¬ P` に入れ替えるタクティクスである。含意を対偶の形で証明したいときに使う。

```lean
import Mathlib.Tactic.Contrapose

example (P Q : Prop) (f : ¬ Q → ¬ P) : P → Q := by
  intro hp
  contrapose hp
  exact f hp
```

`contrapose hp` の後は、`hp : ¬ Q` を使って `¬ P` を証明する状態になる。矛盾を直接ゴールにする `by_contra` とは異なる。

`contrapose!` は、さらに仮定とゴールの否定を整理する。

```lean
import Mathlib.Tactic.Contrapose
import Mathlib.Data.Int.Order.Basic

example (x y : Int) : (¬ y < x) → x ≤ y := by
  intro h
  contrapose! h
  exact h
```

ここでは `h : y < x` とゴール `y < x` が得られる。`contrapose h with hn` と書けば、入れ替えた仮定に別の名前を付けられる。否定の整理は [push_neg](push_neg.md) と同じ目的の処理である。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用）。

[mathlib タクティクス一覧に戻る](README.md)
