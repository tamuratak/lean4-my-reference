# `mspecialize`

`mspecialize` は、状態を扱う全称命題や含意の仮定を具体化するタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

含意の仮定に、その前提の証明を渡す。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ (P → Q) → Q := by
  mintro hP hPQ
  mspecialize hPQ hP
  mexact hPQ
```

この後の `hPQ` は `Q` の証明になる。通常の `specialize` に対応する。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mspecialize`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mspecialize)。

[タクティクス一覧に戻る](README.md)
