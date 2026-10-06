# `classical`

`classical` は、古典論理に基づく判定可能性などを、後続の証明で使えるようにするタクティクスである。

例えば、任意の命題 `P` を条件にする式の `if` には `[Decidable P]` が必要になる。`classical` は、この判定を古典論理に基づいて利用できるようにする。

```lean
import Std.Tactic

example (P : Prop) : P ∨ ¬ P := by
  fail_if_success exact if h : P then Or.inl h else Or.inr h
  classical
  exact if h : P then Or.inl h else Or.inr h
```

ここでの `if` は `exact` に渡す証明の式である。`then` 側は `h : P` から、`else` 側は `h : ¬ P` から証明を作る。`classical` の前は、式の `if` に必要な `Decidable P` が見つからないためエラーになる。最初の `fail_if_success` は、その失敗を検査する。`classical` の後は同じ式が使える。

`classical` 自体がゴールを閉じるわけではない。また、指定バージョンの [`by_cases`](by_cases.md) や[タクティクスの `if`](if.md)は必要な古典的判定を内部で利用するため、それらで場合分けするだけなら `classical` は不要である。

数値の比較や有限の計算を扱う証明では、既に判定方法があるため不要なことも多い。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`classical`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.classical)。

[タクティクス一覧に戻る](README.md)
