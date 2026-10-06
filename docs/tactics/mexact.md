# `mexact`

`mexact` は、状態を扱う証明モードで、ゴールに合う証明を渡すタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

導入した状態を扱う仮定をそのまま使ってゴールを閉じる。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mintro hP
  mexact hP
```

ここでの `hP` は通常の局所仮定とは異なり、状態を扱う証明モードの中の名前である。普通の `exact` ではなく `mexact` で参照する。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mexact`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mexact)。

[タクティクス一覧に戻る](README.md)
