# `mvcgen`

`mvcgen` は、**プログラムの仕様を証明するための条件を、実行の構造に従って生成する**タクティクスである。

`import Std.Tactic.Do` と `open Std.Do` を使う。通常の命題の自動証明とは異なり、プログラム検証のための操作である。

```lean
open Std.Do

example : ⦃⌜True⌝⦄ (pure 3 : Id Nat) ⦃⇓ n => ⌜n = 3⌝⦄ := by
  mvcgen
```

`⦃P⦄ program ⦃Q⦄` は、前提 `P` のもとでプログラムを実行すると、結果について条件 `Q` が成り立つという仕様を表す。`⇓ n => ...` の `n` は返り値である。

この例は `3` を返すだけなので、生成される条件も自動で閉じる。複雑なプログラムでは条件が残るため、それぞれを証明する必要がある。

`mvcgen [仕様の定理, 定義名]` で使う情報を追加できる。ループでは不変条件が必要になることもある。`mvcgen?` は不変条件の候補を表示するための関連操作である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`mvcgen`](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mvcgen)。

[タクティクス一覧に戻る](README.md)
