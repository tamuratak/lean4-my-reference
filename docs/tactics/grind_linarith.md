# `grind_linarith`

`grind_linarith` は、**`grind` の線形算術の機能に絞って証明する**タクティクスである。

変数を一次式として扱える関係に使う。

```lean
example (x y : Int) (h : x ≤ y) : x + 1 ≤ y + 1 := by
  grind_linarith
```

利用できる型は、線形算術の構造が登録されているものに依存する。整数の離散的な性質も使うなら `lia`、自然数と整数の線形算術なら `omega` も選択肢になる。

`grind` は算術に加えて等式や論理の推論も連携させる。まず `grind` で証明できたものを、必要に応じて機能を絞って書ける。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`grind_linarith`](https://lean-lang.org/doc/api/Init/Grind/Tactics.html#Lean.Parser.Tactic.grind_linarith)。

[タクティクス一覧に戻る](README.md)
