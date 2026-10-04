# `mclear`

`mclear` は、**状態を扱う証明モードから、不要な仮定を取り除く**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

使わない前提を消し、必要な仮定だけで証明する。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ Q → Q := by
  mintro hP hQ
  mclear hP
  mexact hQ
```

通常の `clear` に対応する。普通の局所仮定と、状態を扱う証明モードの仮定を区別して使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mclear`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mclear)。

[タクティクス一覧に戻る](README.md)
