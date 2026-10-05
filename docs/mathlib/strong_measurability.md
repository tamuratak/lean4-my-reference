# 強可測性と、ほとんど至る所での同一視

実数値関数の可測性だけを扱うときは、`Measurable` が中心になる。ベクトル値の積分を扱う mathlib では、単関数で近似できるという強可測性と、零測度の例外を許す条件も使う。

## 可測性と強可測性

以下の `StronglyMeasurable`・`AEStronglyMeasurable` などは `MeasureTheory` 名前空間のもの。

| 意味 | 数学の条件 | Lean |
| --- | --- | --- |
| 可測集合 | 指定した可測集合の族に属する | `MeasurableSet s` |
| 可測関数 | 可測集合の逆像が可測 | `Measurable f` |
| 単関数 | 有限個の値を取る可測関数 | `MeasureTheory.SimpleFunc E F` |
| 強可測関数 | 単関数列が各点で $f$ に収束する | `StronglyMeasurable f` |
| ほとんど至る所で可測 | 可測な関数とほとんど至る所で等しい | `AEMeasurable f μ` |
| ほとんど至る所で強可測 | 強可測な関数とほとんど至る所で等しい | `AEStronglyMeasurable f μ` |

強可測性は、各 $x$ に対して単関数列 $s_n(x)$ が $f(x)$ に収束することをいう。

$$
\exists(s_n),\ \forall x,\quad s_n(x)\longrightarrow f(x).
$$

ここで単関数の「単」は滑らかさなどではなく、有限個の値しか取らないことを指す。強可測性には入力の可測空間と出力の位相が必要であり、`StronglyMeasurable f` 自体は測度を指定しない。`AEStronglyMeasurable f μ` は、例外の大きさを測るために `μ` も指定する。

実数値では標準の Borel 可測構造のもとで、`StronglyMeasurable f` と `Measurable f` は同値になる。ほとんど至る所での二つの条件も同値である。一般の値域では同一視できず、例えば距離に対応する位相、第二可算性、Borel 可測構造など、対応定理の条件を確認する。

```lean
import Mathlib.MeasureTheory.Function.StronglyMeasurable.AEStronglyMeasurable
import Mathlib.MeasureTheory.Constructions.BorelSpace.Basic

open MeasureTheory

example (f : ℝ → ℝ) (hf : Measurable f) : StronglyMeasurable f :=
  hf.stronglyMeasurable

example (f : ℝ → ℝ) (μ : Measure ℝ) (hf : AEMeasurable f μ) :
    AEStronglyMeasurable f μ := hf.aestronglyMeasurable
```

## 零測度の例外を許す

`AEStronglyMeasurable f μ` は、ある強可測関数 $g$ について $f=g$ がほとんど至る所で成り立つという命題である。

| 意味 | Lean |
| --- | --- |
| ほとんど至る所で条件が成立 | `∀ᵐ x ∂μ, P x` |
| ほとんど至る所で等しい | `f =ᵐ[μ] g` |
| 強可測な代表とほとんど至る所で等しい | `∃ g, StronglyMeasurable g ∧ f =ᵐ[μ] g` |

例えば Lebesgue 測度では、$f(0)=1$、$x\ne0$ なら $f(x)=0$ という関数と、恒等的に零の関数はほとんど至る所で等しい。しかし点 $0$ の値が違うので、普通の関数としての等式 `f = g` は成立しない。

零測度の例外は測度に依存する。同じ二つの関数でも、点 $0$ に質量を持つ Dirac 測度では、ほとんど至る所で等しいとは言えない。

## 関数を同一視した空間

積分や $L^p$ のノルムでは、零測度の集合で値を変更しても結果が変わらない。このため、関数をほとんど至る所での等しさによって同一視した空間を使う。

| 対象 | Lean | 要素の意味 |
| --- | --- | --- |
| 点ごとの関数 | `f : E → F` | すべての点での値を指定 |
| ほとんど至る所で強可測な関数の同値類 | `E →ₘ[μ] F` または `AEEqFun E F μ` | ほとんど至る所で等しい関数を同じ要素とみなす |
| $L^p$ の要素 | `u : MeasureTheory.Lp F p μ` | 上の同値類に $p$ に対応する有限性条件を課したもの |
| 関数を同値類に入れる | `AEEqFun.mk f hf` | `hf : AEStronglyMeasurable f μ` を使う |

この固定バージョンの `Lp` は `AEEqFun` の加法部分群として定義され、要素を扱う場所ではその部分群の型を使う。$p=1$ では可積分な関数、$p=\infty$ では本質的に有界な関数の同値類に対応する。通常のノルム空間として使うには $1\le p$ など、必要な条件を確認する。

`Integrable f μ` は、もとの関数が可積分であるという命題であり、`f` の型を `Lp` に変えるものではない。逆に、同値類を代表する関数を取り出しても、特定の一点の値は同値類から一意に決まらない。

```lean
import Mathlib.MeasureTheory.Function.LpSpace.Basic
import Mathlib.MeasureTheory.Constructions.BorelSpace.Basic

open MeasureTheory
open scoped MeasureTheory

variable (μ : Measure ℝ)

#check (ℝ →ₘ[μ] ℝ)
#check (ℝ →₁[μ] ℝ)
#check (ℝ →₂[μ] ℝ)

example (μ : Measure ℝ) (f g : ℝ → ℝ)
    (hf : AEStronglyMeasurable f μ) (hg : AEStronglyMeasurable g μ)
    (h : f =ᵐ[μ] g) : AEEqFun.mk f hf = AEEqFun.mk g hg := by
  exact AEEqFun.mk_eq_mk.mpr h
```

関連：[測度と可積分性](measure_integrals.md)、[優収束定理](function_sequences.md#積分と極限の交換優収束定理)、[フィルター](filters.md#測度と級数で現れるフィルター)、[WithLp との違い](with_lp.md#測度論の-lp-との違い)。商の仕組み：[商型](../basic-types/quotient.md)、[公式リファレンス：Quotients](https://lean-lang.org/doc/reference/latest/The-Type-System/Quotients/)。

[mathlib の索引に戻る](README.md)
