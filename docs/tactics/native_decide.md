# `native_decide`

`native_decide` は、命題の判定手続きをコンパイルして実行し、その結果から証明するタクティクスである。

`decide` の計算が大きくなるときに使える。

```lean
import Std.Tactic

theorem nativeLength : (List.range 1000).length = 1000 := by
  native_decide

#print axioms nativeLength
```

`decide` と同様、命題を判定する方法が必要である。単に仮定から論理的に推論するタクティクスではない。

通常の `decide` はカーネルの計算による検査を使う。一方、指定バージョンの `native_decide` はコンパイルした計算が `true` を返すことを確認し、その結果を主張する個別の公理を生成して証明に使う。固定の `Lean.ofReduceBool` という公理に依存する仕組みではない。

上の `#print axioms` で依存先を確認できる。

```text
'nativeLength' depends on axioms: [nativeLength._native.native_decide.ax_1_1]
```

生成名は定理名や実行箇所によって変わる。この証明の検証の前提にはコンパイラーと実行系も含まれるので、計算量と検証の前提の違いを理解した上で使う。

参照：[公式 API：`native_decide`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.nativeDecide)、[公式 API：計算結果の公理を生成する `nativeEqTrue`](https://lean-lang.org/doc/api/Lean/Meta/Native.html#Lean.Meta.nativeEqTrue)。

[タクティクス一覧に戻る](README.md)
