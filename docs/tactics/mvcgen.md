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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
