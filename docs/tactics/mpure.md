# `mpure`

`mpure` は、**状態によらない仮定を、普通の Lean の仮定として取り出す**タクティクスである。

このページは、標準ライブラリのプログラム検証用の操作である。`import Std.Tactic.Do` と `open Std.Do` を使う。

`⌜P⌝` から `hp : P` を取り出して、普通の `exact` で使う。

```lean
open Std.Do

example (σs : List Type) (P : Prop) : (⌜P⌝ : SPred σs) ⊢ₛ ⌜P⌝ := by
  mintro hp
  mpure hp
  mpure_intro
  exact hp
```

状態を扱う仮定すべてを普通の命題として取り出せるわけではない。純粋な命題に対応する仮定が対象になる。

通常の命題の証明から読み始める場合は、まず `intro`、`exact`、`cases` などのページを参照するとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
