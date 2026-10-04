# `mstart`

`mstart` は、**状態を扱う命題の証明モードを開始する**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

状態についての命題を `SPred` と書く。`P ⊢ₛ Q` は、各状態で `P` が成り立てば `Q` が成り立つことを表す。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mstart
  mintro hP
  mexact hP
```

`mintro` から直接始めると、このモードの開始も自動で試される。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
