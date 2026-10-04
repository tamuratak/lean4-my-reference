# `mleave`

`mleave` は、**状態を扱う証明モードを抜け、普通の Lean の命題へ展開する**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

通常の論理のタクティクスで証明を続けたいときに使う。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mleave
  simp
```

`mvcgen` の後に残った条件を、`grind` や `simp` で扱える形にしたいときにも利用する。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
