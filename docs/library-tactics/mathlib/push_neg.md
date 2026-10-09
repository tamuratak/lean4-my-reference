# `push_neg`・`push Not`

`push_neg` は、否定を論理結合子や量化子の内側へ押し込み、使いやすい形にするタクティクスである。仮定に使うなら `push_neg at h`、ゴールに使うなら `push_neg` と書く。

```lean
import Mathlib.Tactic.Push

example (α : Type) (P : α → Prop) (h : ¬ ∃ x, P x) : ∀ x, ¬ P x := by
  push_neg at h
  exact h
```

操作後の仮定は次の形になる。

```text
h : ∀ x, ¬ P x
```

この依存バージョンでは `push_neg` は非推奨で、`push Not` が推奨される。`push_neg at h` の代わりに `push Not at h` と書ける。

順序の否定も整理できる。

```lean
import Mathlib.Tactic.Push
import Mathlib.Data.Int.Order.Basic

example (x y : Int) (h : ¬ x ≤ y) : y < x := by
  push Not at h
  exact h
```

ここでは `h : y < x` になる。否定の位置や形を変える操作であり、仮定から算術の結論を探す操作ではない。背理法で否定を導入するときには [by_contra!](by_contra.md) と組み合わせられる。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用）。

[mathlib タクティクス一覧に戻る](README.md)
