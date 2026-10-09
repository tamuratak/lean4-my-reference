# `bv_decide`

`bv_decide` は、固定ビット幅の演算や論理を、SAT ソルバーを使って証明するタクティクスである。

`BitVec 8` は 8 ビットの値であり、加算などはビット幅で折り返す。

```lean
import Std.Tactic

example (x y : BitVec 8) : x + y = y + x := by
  bv_decide

example (x : BitVec 8) : x ^^^ x = 0 := by
  bv_decide
```

このページの例には `import Std.Tactic` が必要である。一般の自然数の線形算術には `omega` を使う。

`bv_normalize` はソルバーに渡す前の正規化を行い、`bv_decide?` は証明の再実行に使える情報を提案する。`bv_check` は既に用意した証明書を検査するための操作で、証明書ファイルが必要になる。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`bv_decide`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.bvDecide)。

[タクティクス一覧に戻る](README.md)
