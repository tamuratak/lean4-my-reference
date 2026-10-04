# `next`

`next` は、**次のゴールを選び、必要ならその仮定に名前を付けて証明する**タクティクスである。

ゴール名が分からなくても、先頭から順に証明できる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  constructor
  next => exact hp
  next => exact hq
```

`next h => ...` のように、直接使いにくい名前の仮定に名前を付けることもできる。

`case` がゴールの名前で選ぶのに対し、`next` は順番で選ぶ。順番だけで十分なら `·` のブロックも同様に使える。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
