# `choose`

`choose` は、全称命題の内側にある存在命題から、証人を選ぶ関数と、その関数が条件を満たす証明を取り出すタクティクスである。

```lean
import Mathlib.Tactic.Choose

example (α β : Type) (R : α → β → Prop) (h : ∀ x, ∃ y, R x y) :
    ∃ f : α → β, ∀ x, R x (f x) := by
  choose f hf using h
  exact ⟨f, hf⟩
```

操作後、次の関数と証明が得られる。

```text
f  : α → β
hf : ∀ x, R x (f x)
```

`rcases` が一つの存在命題から一つの値を取り出すのに対し、`choose` は入力 `x` ごとの証人をまとめて関数にする。存在命題の条件が論理積なら、各条件の証明も別々に取り出せる。

```lean
import Mathlib.Tactic.Choose

example (α β : Type) (R S : α → β → Prop)
    (h : ∀ x, ∃ y, R x y ∧ S x y) : ∃ f : α → β, ∀ x, S x (f x) := by
  choose f hr hs using h
  exact ⟨f, hs⟩
```

一般には古典的な選択を利用する。取り出す関数を実行可能なアルゴリズムとして得る操作ではない。証人一つの分解には Lean 本体の [rcases](../../tactics/rcases.md) を使う。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用。追加ライブラリの仕様資料については[一覧の検証・参照方針](../README.md#検証と参照方針)を参照）。

[mathlib タクティクス一覧に戻る](README.md)
