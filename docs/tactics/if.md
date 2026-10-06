# `if`

タクティクスの `if` は、命題が成り立つ場合と成り立たない場合に分け、両方の場合を証明する操作である。

`if h : P then ... else ...` は、`then` 側に `h : P`、`else` 側に `h : ¬ P` を追加する。どちらも元のゴールを証明する必要がある。

```lean
import Std.Tactic

example (P : Prop) : P ∨ ¬ P := by
  if h : P then
    exact Or.inl h
  else
    exact Or.inr h
```

この例では `then` 側で `P` から左側を、`else` 側で `¬ P` から右側を証明する。一方の分岐だけを選んで実行する操作ではない。

これは [`by_cases h : P`](by_cases.md) の二つのゴールを `then` と `else` に書く構文である。指定バージョンでは古典的な判定を内部で利用するため、任意の命題に使え、利用者が `[Decidable P]` や `classical` を用意する必要はない。

条件に応じて値を返す[式の `if`](../syntax/if.md)とは役割が違う。ゴールの中にある式の `if` を分けたい場合は `split` を使う。

参照：[公式リファレンス：タクティクスの条件分岐](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`if`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacDepIfThenElse)。

[タクティクス一覧に戻る](README.md)
