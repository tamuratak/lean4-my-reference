# `mexists`

`mexists` は、**状態を扱う存在命題のゴールに、証人を渡す**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

具体的な自然数を証人として指定する。

```lean
open Std.Do

example (σs : List Type) (P : Nat → SPred σs) : P 7 ⊢ₛ ∃ n, P n := by
  mintro hP
  mexists 7
```

この例では渡した証人の条件が仮定にあるので、その場で閉じる。通常の `exists` に対応する。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
