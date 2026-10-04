# `left`

`left` は、**論理和のゴールで、左側を証明する方針を選ぶ**タクティクスである。

ゴールが `P ∨ Q` のとき、`left` と書くとゴールが `P` になる。

```lean
example (P Q : Prop) (hp : P) : P ∨ Q := by
  left
  exact hp
```

これは `Or.inl` というコンストラクターを使う操作である。右側を選ぶなら `right` を使う。

仮定にある論理和を場合分けする操作は別であり、`cases` や `rcases` を使う。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
