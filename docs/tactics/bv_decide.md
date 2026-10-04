# `bv_decide`

`bv_decide` は、**固定ビット幅の演算や論理を、SAT ソルバーを使って証明する**タクティクスである。

`BitVec 8` は 8 ビットの値であり、加算などはビット幅で折り返す。

```lean
example (x y : BitVec 8) : x + y = y + x := by
  bv_decide

example (x : BitVec 8) : x ^^^ x = 0 := by
  bv_decide
```

このページの例には `import Std.Tactic` が必要である。一般の自然数の線形算術には `omega` を使う。

`bv_normalize` はソルバーに渡す前の正規化を行い、`bv_decide?` は証明の再実行に使える情報を提案する。`bv_check` は既に用意した証明書を検査するための操作で、証明書ファイルが必要になる。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
