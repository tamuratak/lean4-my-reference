# `mexfalso`

`mexfalso` は、**状態を扱うゴールを、偽を示す形に変える**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

`⌜False⌝` は、状態によらず偽である命題を表す。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : ⌜False⌝ ⊢ₛ P := by
  mintro hFalse
  mexfalso
  mexact hFalse
```

通常の `exfalso` に対応する。仮定の矛盾そのものを探す操作ではない。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
