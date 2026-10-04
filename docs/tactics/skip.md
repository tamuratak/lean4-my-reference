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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
