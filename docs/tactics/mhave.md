# `mhave`

`mhave` は、**状態を扱う証明モードに、補助的な事実を追加する**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

途中で得られる事実を、別の名前で保存する。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ (P → Q) → Q := by
  mintro hP hPQ
  mhave hQ : Q := by
    mspecialize hPQ hP
    mexact hPQ
  mexact hQ
```

通常の `have` に対応する。`mhave` の内側では、現在の状態を扱う仮定を使って補助的なゴールを証明できる。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
