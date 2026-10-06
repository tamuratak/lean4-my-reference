# `mrevert`

`mrevert` は、状態を扱う仮定を、ゴールの前提へ戻すタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

一度導入した仮定を戻して、改めて名前を付ける。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mintro hP
  mrevert hP
  mintro hAgain
  mexact hAgain
```

通常の `revert` に対応する。普通の局所変数を戻す場合は `revert` を使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mrevert`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mrevert)。

[タクティクス一覧に戻る](README.md)
