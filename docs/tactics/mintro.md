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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mintro`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mintro)。

[タクティクス一覧に戻る](README.md)
