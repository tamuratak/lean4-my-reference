# `mspec`

`mspec` は、**プログラムの仕様を表す定理を適用し、前提や事後条件の確認をゴールにする**タクティクスである。

`import Std.Tactic.Do` と `open Std.Do` を使う。プログラムの仕様に対する `apply` のような操作である。

```lean
open Std.Do

example : ⦃⌜True⌝⦄ (pure 3 : Id Nat) ⦃⇓ n => ⌜n = 3⌝⦄ := by
  mintro hTrue
  mspec Spec.pure
  all_goals (mleave; simp)
```

`Spec.pure` は、値をそのまま返す操作の仕様である。それを適用した後、前提と事後条件の関係を確認する課題を証明する。

`mspec` と引数を省略すると、`@[spec]` が付いた仕様を探して利用する。`mvcgen` はプログラムの構造に従って、このような適用を自動で進める。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/blob/v4.34.1/src/Std/Tactic/Do/Syntax.lean)。

[タクティクス一覧に戻る](README.md)
