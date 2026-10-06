# `suffices`

`suffices` は、本来のゴールを証明するために十分な、別の命題を提示するタクティクスである。

ゴールが `Q` で `h : P → Q` があれば、まず `P` を示せば十分である。

```lean
example (P Q : Prop) (h : P → Q) (hp : P) : Q := by
  suffices hP : P from h hP
  exact hp
```

`from h hP` は「`P` が証明できたら本来のゴール `Q` をどう閉じるか」を指定する。その後に残るゴールは `P` である。

`have` が必要な事実を追加してから先へ進むのに対し、`suffices` は先にゴールを閉じる道筋を示す。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`suffices`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticSuffices_)。

[タクティクス一覧に戻る](README.md)
