# `massumption`

`massumption` は、状態を扱う仮定から、ゴールに合うものを探すタクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

使う仮定の名前を指定せずに、ゴールを閉じる。

```lean
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ⊢ₛ Q → P := by
  mintro hP hQ
  massumption
```

通常の命題に対する `assumption` に対応する。含意の前提をたどる一般的な探索を行うわけではない。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`massumption`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.massumption)。

[タクティクス一覧に戻る](README.md)
