# `mconstructor`

`mconstructor` は、**状態を扱うゴールの論理積などを分ける**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

同じ前提を使って、二つの成分を証明する。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P ∧ P := by
  mintro hP
  mconstructor
  · mexact hP
  · mexact hP
```

通常の `constructor` に対応する。複数のゴールができた後は、通常どおり `·` や `<;>` で処理できる。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mconstructor`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mconstructor)。

[タクティクス一覧に戻る](README.md)
