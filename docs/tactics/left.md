# `left`

`left` は、論理和のゴールで、左側を証明する方針を選ぶタクティクスである。

ゴールが `P ∨ Q` のとき、`left` と書くとゴールが `P` になる。

```lean
example (P Q : Prop) (hp : P) : P ∨ Q := by
  left
  exact hp
```

これは `Or.inl` というコンストラクターを使う操作である。右側を選ぶなら `right` を使う。

仮定にある論理和を場合分けする操作は別であり、`cases` や `rcases` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`left`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.left)。

[タクティクス一覧に戻る](README.md)
