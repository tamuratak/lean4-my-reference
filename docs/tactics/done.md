# `done`

`done` は、未解決のゴールが残っていないことを確認するタクティクスである。

ゴールが残っていれば失敗し、残っていなければ成功する。

```lean
example (P : Prop) (hp : P) : P := by
  exact hp
  done
```

例えば `simp` はゴールが残ったまま成功することがある。組合せの中で `simp; done` と書けば、簡単化だけで証明を完了できたことも確認できる。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`done`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.done)。

[タクティクス一覧に戻る](README.md)
