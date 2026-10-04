# `skip`

`skip` は、**証明状態を変えずに成功する**タクティクスである。

タクティクスの組合せで「何もしない」を表す。

```lean
example (P : Prop) (hp : P) : P := by
  skip
  exact hp
```

`skip` はゴールを閉じない。例えば `first | skip | exact hp` では最初の `skip` が成功するので、`exact hp` は試されない。

証明が完了したかを確認する操作は `done` である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`skip`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.skip)。

[タクティクス一覧に戻る](README.md)
