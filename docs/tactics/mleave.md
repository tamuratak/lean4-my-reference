# `mleave`

`mleave` は、状態を扱う証明モードを抜け、普通の Lean の命題へ展開するタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

通常の論理のタクティクスで証明を続けたいときに使う。

```lean
import Std.Tactic.Do
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mleave
  simp
```

`mvcgen` の後に残った条件を、`grind` や `simp` で扱える形にしたいときにも利用する。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mleave`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mleave)。

[タクティクス一覧に戻る](README.md)
