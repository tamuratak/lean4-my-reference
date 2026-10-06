# `as_aux_lemma`

`as_aux_lemma` は、内側のタクティクスで作る証明を、補助的な定理にまとめるタクティクスである。

証明項の構造や大きさを調整するための操作である。

```lean
example (P : Prop) (hp : P) : P := by
  as_aux_lemma =>
    exact hp
```

内側の証明で元のゴールを閉じる。日常的な証明で必要な補助的な事実を追加する `have` とは用途が異なる。

まず読みやすい証明を書き、証明項の扱いが問題になるときに使うとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`as_aux_lemma`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.as_aux_lemma)。

[タクティクス一覧に戻る](README.md)
