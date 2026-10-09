# `mpure_intro`

`mpure_intro` は、状態を扱うゴールが純粋な命題なら、普通の命題の証明へ移るタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

`⌜True⌝` は、状態によらず `True` が成り立つことを表す。

```lean
import Std.Tactic.Do
open Std.Do

example (σs : List Type) : ⊢ₛ (⌜True⌝ : SPred σs) := by
  mpure_intro
  trivial
```

この操作では状態を扱う前提を捨て、純粋な命題を証明する。捨てた前提を使う必要があるなら、先に `mpure` や `mleave` を検討する。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mpure_intro`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mpureIntro)。

[タクティクス一覧に戻る](README.md)
