# `case`

`case` は、**名前の付いたゴールを選び、その場合の証明を書く**タクティクスである。

`constructor` で作った論理積のゴールには、`left` と `right` という名前が付く。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  case left => exact hp
  case right => exact hq
```

帰納法や場合分けで付いた `zero`、`succ` なども選べる。`case succ n ih => ...` のように、その場合の変数や仮定に名前を付けることもできる。

通常の `case` のブロックでは、選んだゴールをそのブロック内で閉じる。`case'` はゴールが残ることを許す変種である。

単に順番に証明するだけなら、箇条書きの点に似た `·` でもよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`case`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.case)。

[タクティクス一覧に戻る](README.md)
