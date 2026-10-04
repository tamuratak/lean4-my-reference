# `mintro`

`mintro` は、**状態を扱う証明モードで、前提を名前付きの仮定として取り出す**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

`P ⊢ₛ Q → P` から、状態を扱う仮定 `hP` と `hQ` を導入する。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ Q → P := by
  mintro hP hQ
  mexact hP
```

`intro` は普通の Lean の引数や仮定に使う。`mintro` は状態を扱う論理の前提に使う。論理積などをパターンで分解することもできる。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
