# `;`・`<;>`・`·`

`;`、`<;>`、`·` は、タクティクスを組み合わせたり、作られたゴールを選んだりするための構文である。

`<;>` は、左側の操作が作ったすべてのゴールに右側の操作を行う。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor <;> assumption
```

一方 `;` は単に次の操作へ進む。通常、その操作が見るのは先頭のゴールである。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor; exact hp
  exact hq
```

`·` は、先頭のゴールを一つ選んで、そのブロックで証明するための構文である。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  · exact hp
  · exact hq
```

`semicolon` という名前のタクティクスがあるわけではない。このページは `;`、`<;>`、`·` の読み方を説明している。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`;`・`<;>`・`·`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tactic_%3C%3B%3E_)。

[タクティクス一覧に戻る](README.md)
