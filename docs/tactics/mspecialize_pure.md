# `mspecialize_pure`

`mspecialize_pure` は、**普通の局所仮定にある事実を、状態を扱う仮定などで具体化する**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

通常の仮定 `h` に、証明モード内の `hP` を渡す。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) (h : ⊢ₛ P → Q) : P ⊢ₛ Q := by
  mintro hP
  mspecialize_pure h hP => hQ
  mexact hQ
```

`mspecialize` は証明モード内の仮定自体を具体化する。`mspecialize_pure` は普通の局所仮定を出発点にする。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mspecialize_pure`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mspecializePure)。

[タクティクス一覧に戻る](README.md)
