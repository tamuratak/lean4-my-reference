# `mstop`

`mstop` は、**状態を扱う証明モードを止め、そのモードで付けた仮定の名前を忘れる**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

開始と停止によって表示や名前の扱いが変わることを確認できる。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mstart
  mstop
  mintro hP
  mexact hP
```

命題の内容を証明する操作ではない。普通の命題へ展開して自動化を使いたいなら、単にモードを止める `mstop` ではなく `mleave` を使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mstop`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mstop)。

[タクティクス一覧に戻る](README.md)
