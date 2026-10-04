# `mcases`

`mcases` は、**状態を扱う仮定を、パターンで分解する**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

仮定の論理積から、それぞれの成分を取り出す。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ∧ Q ⊢ₛ Q := by
  mintro h
  mcases h with ⟨hP, hQ⟩
  mexact hQ
```

通常の `rcases` に対応する。不要な成分を取り除くパターン `-` も使える。状態を扱う論理和の分解では `⟨hP | hQ⟩` というパターンを使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
