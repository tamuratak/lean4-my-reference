# `mframe`

`mframe` は、**状態によらない仮定を見つけ、普通の仮定へ移す**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

純粋な仮定を通常の証明に引き継ぎたいときに使う。

```lean
open Std.Do

example (σs : List Type) (P : Prop) : (⌜P⌝ : SPred σs) ⊢ₛ ⌜P⌝ := by
  mintro hp
  mframe
  mpure_intro
  assumption
```

`mpure hp` は仮定を指定して取り出す。`mframe` は取り出せる仮定を探して処理し、`mspec` による仕様の適用にも使われる。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mframe`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mframe)。

[タクティクス一覧に戻る](README.md)
