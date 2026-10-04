# `native_decide`

`native_decide` は、**命題の判定手続きをコンパイルして実行し、その結果から証明する**タクティクスである。

`decide` の計算が大きくなるときに使える。

```lean
example : (List.range 1000).length = 1000 := by
  native_decide
```

`decide` と同様、命題を判定する方法が必要である。単に仮定から論理的に推論するタクティクスではない。

通常の `decide` はカーネルの計算による検査を使う。一方 `native_decide` の結果にはコンパイラーと実行系も関わり、生成される証明は `Lean.ofReduceBool` という公理に依存する。計算量と検証の前提の違いを理解した上で使う。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
