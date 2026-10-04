# `mpure_intro`

`mpure_intro` は、**状態を扱うゴールが純粋な命題なら、普通の命題の証明へ移る**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

`⌜True⌝` は、状態によらず `True` が成り立つことを表す。

```lean
open Std.Do

example (σs : List Type) : ⊢ₛ (⌜True⌝ : SPred σs) := by
  mpure_intro
  trivial
```

この操作では状態を扱う前提を捨て、純粋な命題を証明する。捨てた前提を使う必要があるなら、先に `mpure` や `mleave` を検討する。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
