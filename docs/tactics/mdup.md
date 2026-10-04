# `mdup`

`mdup` は、**状態を扱う仮定に、複製した別名を付ける**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

元の仮定を加工する前に、同じ内容を別名で残せる。

```lean
open Std.Do

example (σs : List Type) (P : SPred σs) : P ⊢ₛ P := by
  mintro hP
  mdup hP => hCopy
  mclear hP
  mexact hCopy
```

この例では元の名前を消しても、複製した仮定からゴールを閉じられる。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
