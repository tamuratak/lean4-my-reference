# `mright`

`mright` は、状態を扱う論理和のゴールで、右側を選ぶタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

`Q ∨ P` を証明するため、`P` の側を選ぶ。

```lean
import Std.Tactic.Do
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ Q ∨ P := by
  mintro hP
  mright
  mexact hP
```

通常の `right` に対応する。仮定にある論理和を分けるには `mcases` を使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mright`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mright)。

[タクティクス一覧に戻る](README.md)
