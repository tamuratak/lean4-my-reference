# `mrefine`

`mrefine` は、**状態を扱う証明の形を指定し、穴をゴールとして残す**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

論理積の左側だけを埋め、右側を後で証明する。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ∧ Q ⊢ₛ P ∧ Q := by
  mintro ⟨hP, hQ⟩
  mrefine ⟨hP, ?_⟩
  mexact hQ
```

通常の `refine` に対応する。純粋な値を渡す箇所では `⌜...⌝` という特有の構文も使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
