# `rotate_left`

`rotate_left` は、ゴールの順番を左へ回し、次のゴールを先頭にするタクティクスである。

二つのゴールなら、先頭と次のゴールを入れ替えられる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  rotate_left
  exact hq
  exact hp
```

`rotate_left 2` のように回す数を指定できる。`rotate_right` は逆方向に回す。

順番だけを変え、ゴールの内容は変えない。名前の付いたゴールを選びたいなら `case`、型で選びたいなら `show` が使える。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`rotate_left`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.rotateLeft)。

[タクティクス一覧に戻る](README.md)
