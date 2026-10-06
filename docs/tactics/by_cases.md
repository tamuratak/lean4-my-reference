# `by_cases`

`by_cases` は、命題が成り立つ場合と、成り立たない場合に分けるタクティクスである。

`by_cases h : P` と書くと、次の二つの場合を証明することになる。

```text
h : P       ⊢ 元のゴール
h : ¬ P     ⊢ 元のゴール
```

```lean
import Std.Tactic

example (P : Prop) : P ∨ ¬ P := by
  by_cases h : P
  · exact Or.inl h
  · exact Or.inr h
```

指定バージョンの `by_cases` は、必要な古典的判定を内部で利用する。そのため、任意の `P : Prop` に使え、この例に `classical` や `[Decidable P]` を追加する必要はない。式の `if` など、後続の操作にも古典的判定を使いたい場合は [`classical`](classical.md) を指定する。

`cases h` は既にある値をコンストラクターで分解するが、`by_cases h : P` は命題の真偽を新しく場合分けする。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`by_cases`](https://lean-lang.org/doc/api/Init/ByCases.html)。

[タクティクス一覧に戻る](README.md)
