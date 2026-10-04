# `mreplace`

`mreplace` は、**状態を扱う仮定を、新しく証明した事実に置き換える**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

一般的な含意を、その前提を使って具体化した結果で置き換える。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ (P → Q) → Q := by
  mintro hP hPQ
  mreplace hPQ : Q := by
    mspecialize hPQ hP
    mexact hPQ
  mexact hPQ
```

通常の `replace` に対応する。元の事実も使いたいときは `mhave` で別名を付ける。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
