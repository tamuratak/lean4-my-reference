# `;`・`<;>`・`·`

`;`、`<;>`、`·` は、**タクティクスを組み合わせたり、作られたゴールを選んだりする**ための構文である。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
