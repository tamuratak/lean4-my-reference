# `rotate_left`

`rotate_left` は、**ゴールの順番を左へ回し、次のゴールを先頭にする**タクティクスである。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
