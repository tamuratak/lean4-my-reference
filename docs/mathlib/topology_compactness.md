# 開集合・閉集合・コンパクト性

領域 $s\subseteq E$ の内部や境界を調べるには、空間 $E$ に位相を指定する。Lean では `[TopologicalSpace E]` がその条件を表す。

## 開集合・閉集合と境界

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 開集合である | $s$ の各点の近傍が $s$ に含まれる | `IsOpen s` |
| 閉集合である | 補集合 $s^c$ が開集合 | `IsClosed s` |
| 内部 | $\operatorname{int}(s)$ | `interior s` |
| 閉包 | $\overline{s}$ | `closure s` |
| 境界 | $\partial s=\overline{s}\setminus\operatorname{int}(s)$ | `frontier s` |
| 内点である | $x\in\operatorname{int}(s)$ | `x ∈ interior s` |

`IsOpen s`・`IsClosed s` は命題、`interior s`・`closure s`・`frontier s` は集合を返す操作。開集合と閉集合は互いに否定の関係ではない。例えば空集合と全空間は両方の性質を持つ。

実数の閉区間 $s=[0,1]$ なら、内部は $(0,1)$、閉包は $[0,1]$、境界は $\{0,1\}$。ここでの内部は周囲の空間 $\mathbb{R}$ に関するもの。領域自体を部分型として空間にした場合の位相とは区別する。

内点では `nhdsWithin x s` が `nhds x` と一致するため、領域内からの連続性・微分と、通常の点での連続性・微分を結び付けられる。

## コンパクト性と有界性

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 集合がコンパクト | 開被覆から有限部分被覆を取れる | `IsCompact s` |
| 全空間がコンパクト | $E$ がコンパクト空間 | `CompactSpace E` |
| 距離空間で有界 | ある有限半径の球に含まれる | `Bornology.IsBounded s` |
| 空でない | $s\ne\varnothing$ | `s.Nonempty` |

実ユークリッド空間では、コンパクト性は閉かつ有界であることと同値になる。一般のノルム空間で「閉かつ有界ならコンパクト」とは限らない。無限次元空間の閉単位球が典型的な違いである。

実数の閉区間 `Set.Icc a b` は `isCompact_Icc` でコンパクトと分かる。ただし $a>b$ なら空なので、点の存在には別途非空性が必要になる。閉集合 $\mathbb{R}$ 全体は非有界であり、コンパクトではない。

## 最大値・最小値

空でないコンパクト集合上の連続な実数値関数は、最大値と最小値を取る。

$$
\exists x\in s,\ \forall y\in s,\ f(y)\le f(x).
$$

| 意味 | Lean（`f : E → ℝ`） |
| --- | --- |
| $x$ で領域上の最大値を取る | `IsMaxOn f s x` |
| $x$ で領域上の最小値を取る | `IsMinOn f s x` |
| 最大値を取る点がある | `∃ x ∈ s, IsMaxOn f s x` |
| 最大値の存在を与える定理 | `IsCompact.exists_isMaxOn` |
| 最小値の存在を与える定理 | `IsCompact.exists_isMinOn` |

`IsMaxOn f s x` 自体は `x ∈ s` を含まない。最大点として述べるには、所属条件も合わせる。最大値が存在することと、単に上に有界であることも別の条件である。

```lean
import Mathlib.Topology.Order.Compact
import Mathlib.Topology.Instances.Real.Lemmas

example (f : ℝ → ℝ) (hf : ContinuousOn f (Set.Icc 0 1)) :
    ∃ x ∈ Set.Icc (0 : ℝ) 1, IsMaxOn f (Set.Icc 0 1) x := by
  exact isCompact_Icc.exists_isMaxOn
    ⟨0, by constructor <;> norm_num⟩ hf
```

この例は、最大値を計算するのではなく、閉区間上の連続性から最大点の存在を表している。

例中の [`norm_num`](../library-tactics/mathlib/norm_num.md) は、具体的な数の等式・不等式を証明するタクティクスである。ここでは $0\in[0,1]$ に必要な数値の不等式を処理している。

関連：[領域と連続性](limits_continuity.md)、[領域内の全微分](fderiv.md#領域内の全微分)。共通の構文：[公式リファレンス：型クラス](https://lean-lang.org/doc/reference/latest/Type-Classes/)。

[mathlib の索引に戻る](README.md)
