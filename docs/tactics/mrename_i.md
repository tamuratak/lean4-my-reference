# `mrename_i`

`mrename_i` は、状態を扱う仮定の内部名に、使いやすい名前を付けるタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

名前を指定せずに導入した仮定を、後から参照できるようにする。

```lean
import Std.Tactic.Do
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mintro _
  mrename_i hP
  mexact hP
```

通常の `rename_i` は普通の局所仮定に使う。状態を扱う証明モードの名前には `mrename_i` を使う。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mrename_i`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mrenameI)。

[タクティクス一覧に戻る](README.md)
