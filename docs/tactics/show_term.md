# `show_term`

`show_term` は、タクティクスが作った証明項を表示するタクティクスである。

タクティクスの証明が、どのような項に対応するのかを調べられる。

```lean
example (P : Prop) (hp : P) : P := by
  show_term exact hp
```

例えばこの証明では、`hp` をそのまま渡す証明項が表示される。`show_term` の内側のタクティクスは通常どおり実行されるため、ゴールも閉じる。

長い自動証明では表示される項も長くなる。定理名を探したいだけなら `exact?`、使った簡単化補題を知りたいなら `simp?` が便利である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`show_term`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.showTerm)。

[タクティクス一覧に戻る](README.md)
