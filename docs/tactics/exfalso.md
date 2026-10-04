# `exfalso`

`exfalso` は、**現在のゴールを `False` に変え、矛盾から証明する形にする**タクティクスである。

矛盾が示せれば、どんな命題も証明できる。`exfalso` はその方針を選ぶ。

```lean
example (P Q : Prop) (hp : P) (hnp : ¬ P) : Q := by
  exfalso
  exact hnp hp
```

`¬ P` は `P → False` なので、`hnp hp` が `False` の証明になる。

`exfalso` はゴールを変えるだけで、矛盾そのものを探さない。手元の矛盾を自動で使いたいなら `contradiction` を試せる。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
