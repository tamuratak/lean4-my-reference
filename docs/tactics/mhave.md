# `mhave`

`mhave` は、**状態を扱う証明モードに、補助的な事実を追加する**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

途中で得られる事実を、別の名前で保存する。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ (P → Q) → Q := by
  mintro hP hPQ
  mhave hQ : Q := by
    mspecialize hPQ hP
    mexact hPQ
  mexact hQ
```

通常の `have` に対応する。`mhave` の内側では、現在の状態を扱う仮定を使って補助的なゴールを証明できる。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mhave`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mhave)。

[タクティクス一覧に戻る](README.md)
