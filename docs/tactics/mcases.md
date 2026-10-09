# `mcases`

`mcases` は、状態を扱う仮定を、パターンで分解するタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

仮定の論理積から、それぞれの成分を取り出す。

```lean
import Std.Tactic.Do
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ∧ Q ⊢ₛ Q := by
  mintro h
  mcases h with ⟨hP, hQ⟩
  mexact hQ
```

通常の `rcases` に対応する。不要な成分を取り除くパターン `-` も使える。状態を扱う論理和の分解では `⟨hP | hQ⟩` というパターンを使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mcases`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mcases)。

[タクティクス一覧に戻る](README.md)
