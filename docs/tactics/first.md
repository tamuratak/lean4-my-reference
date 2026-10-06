# `first`

`first` は、複数の候補を順番に試し、最初に成功したものを採用するタクティクスである。

最初の候補が失敗すると、その候補による変更を戻して次を試す。

```lean
example (P Q : Prop) (hp : P) : P := by
  first
  | exact hp
  | contradiction
```

「成功」はゴールを閉じたという意味とは限らない。例えば `skip` はゴールを残したまま成功するため、前に置くと後の候補は試されない。

ゴールを閉じられる候補だけ採用したい場合は `solve` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`first`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.first)。

[タクティクス一覧に戻る](README.md)
