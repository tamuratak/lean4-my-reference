# `revert`

`revert` は、局所変数や仮定を、ゴールの引数や前提へ戻すタクティクスである。

`hp : P` が仮定にあるとき、`revert hp` はゴール `Q` を `P → Q` に変える。

```lean
example (P : Prop) (hp : P) : P := by
  revert hp
  intro hp
  exact hp
```

変数に依存する仮定がある場合、それも一緒に戻される。

```lean
example (n : Nat) (h : n = 0) : n = 0 := by
  revert n
  intro n h
  exact h
```

この例では `h` が `n` に依存するため、`n` を戻すと `h` も戻る。帰納法を始める前に、命題を一般化したいときによく使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`revert`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.revert)。

[タクティクス一覧に戻る](README.md)
