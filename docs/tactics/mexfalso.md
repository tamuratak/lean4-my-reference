# `mexfalso`

`mexfalso` は、状態を扱うゴールを、偽を示す形に変えるタクティクスである。

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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mexfalso`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mexfalso)。

[タクティクス一覧に戻る](README.md)
