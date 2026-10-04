# `done`

`done` は、**未解決のゴールが残っていないことを確認する**タクティクスである。

ゴールが残っていれば失敗し、残っていなければ成功する。

```lean
example (P : Prop) (hp : P) : P := by
  exact hp
  done
```

例えば `simp` はゴールが残ったまま成功することがある。組合せの中で `simp; done` と書けば、簡単化だけで証明を完了できたことも確認できる。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
