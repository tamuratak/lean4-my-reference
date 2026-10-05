# 関数列と極限の交換

関数列 $(F_n)$ と極限関数 $f$ は、`F : ℕ → E → ℝ`・`f : E → ℝ` で表す。`F n` は第 $n$ 関数、`F n x` はその関数の点 $x$ での値である。

収束に使う `atTop`・`nhds`・`Tendsto` の意味は[フィルターと極限](filters.md)を参照。

## 各点収束と一様収束

領域 $s$ 上の各点収束と一様収束は、誤差を小さくする添字を点ごとに選ぶか、領域全体で共通に選ぶかの違いがある。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 点 $x$ で収束 | $F_n(x)\to f(x)$ | `Filter.Tendsto (fun n => F n x) Filter.atTop (nhds (f x))` |
| 領域上で各点収束 | $\forall x\in s,\ F_n(x)\to f(x)$ | `∀ x ∈ s, Filter.Tendsto (fun n => F n x) Filter.atTop (nhds (f x))` |
| 領域上で一様収束 | $F_n\to f$ 一様に、$s$ 上で | `TendstoUniformlyOn F f Filter.atTop s` |
| 全空間で一様収束 | $F_n\to f$ 一様に | `TendstoUniformly F f Filter.atTop` |

実数値の一様収束は、次の量化に対応する。

$$
\forall\varepsilon>0,\ \exists N,\ \forall n\ge N,\ \forall x\in s,
\quad\lvert F_n(x)-f(x)\rvert<\varepsilon.
$$

各点収束では $N$ が $x$ に依存してよい。一様収束では、一つの $N$ が領域内のすべての点に使える。mathlib の一様収束は、実数値に限らず `UniformSpace` を持つ値域に定義される。

例えば $F_n(x)=x^n$ は $[0,1]$ 上で、$x<1$ では $0$、$x=1$ では $1$ に各点収束する。極限は不連続なので、この閉区間全体での一様収束は成立しない。

```lean
import Mathlib.Topology.UniformSpace.UniformConvergence
import Mathlib.Topology.Instances.Real.Lemmas

open scoped Topology

variable (F : ℕ → ℝ → ℝ) (f : ℝ → ℝ) (s : Set ℝ)

#check (∀ x ∈ s, Filter.Tendsto (fun n => F n x)
  Filter.atTop (𝓝 (f x)) : Prop)
#check (TendstoUniformlyOn F f Filter.atTop s : Prop)
#check (TendstoUniformly F f Filter.atTop : Prop)
```

## 連続性と微分への影響

連続関数列が領域上で一様収束すると、極限もその領域上で連続になる。対応する定理名は `TendstoUniformlyOn.continuousOn`（`Mathlib.Topology.UniformSpace.UniformApproximation` をインポート）。自然数列の場合、`∀ n, ContinuousOn (F n) s` と一様収束を使って `ContinuousOn f s` を得る。

各点収束だけでは連続性は保存されない。また、関数自体の一様収束だけでも微分と極限を交換できるとは限らない。例えば

$$
F_n(x)=\frac{\sin((n+1)x)}{n+1}
$$

は実数全体で $0$ に一様収束するが、$F_n'(0)=1$ であり、極限関数の微分 $0$ と一致しない。微分の交換では導関数列の収束など、追加条件を確認する。

## 積分と極限の交換：優収束定理

測度 $\mu$ に対して、ほとんど至る所で収束する関数列を、一つの可積分関数 $g$ で抑えられる場合を考える。

$$
F_n(x)\to f(x)\quad\text{a.e.},\qquad
\lvert F_n(x)\rvert\le g(x),\qquad \int g\,d\mu<\infty.
$$

以下の名前は `MeasureTheory` 名前空間のもの。`F : ℕ → E → ℝ`、`g : E → ℝ`、`μ : Measure E` とする。

| 条件・結論 | Lean |
| --- | --- |
| 各関数がほとんど至る所で強可測 | `∀ n, AEStronglyMeasurable (F n) μ` |
| 抑える関数が可積分 | `Integrable g μ` |
| 全項を同じ関数で抑える | `∀ n, ∀ᵐ x ∂μ, ‖F n x‖ ≤ g x` |
| ほとんど至る所で各点収束 | `∀ᵐ x ∂μ, Filter.Tendsto (fun n => F n x) Filter.atTop (nhds (f x))` |
| 積分値が収束 | `Filter.Tendsto (fun n => ∫ x, F n x ∂μ) Filter.atTop (nhds (∫ x, f x ∂μ))` |
| 上の条件から結論を得る定理 | `tendsto_integral_of_dominated_convergence` |

実数値では、ほとんど至る所で強可測という条件は、零測度の例外を除いて可測な関数で表せることを意味する。優収束は一様収束を要求しないが、項ごとに異なる可積分な上界があるだけでは足りない。全項に共通の可積分な上界を使う。

例えば $F_n(x)=x^n$ を $[0,1]$ で積分するなら、上界 $g(x)=1$ を使える。全実数上では定数 $1$ は Lebesgue 測度で可積分ではないので、領域上の積分には `μ.restrict s` を使う。

```lean
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Topology.Instances.Real.Lemmas

open MeasureTheory
open scoped Topology

example (μ : Measure ℝ) (F : ℕ → ℝ → ℝ) (f g : ℝ → ℝ)
    (hF : ∀ n, AEStronglyMeasurable (F n) μ)
    (hg : Integrable g μ)
    (hbound : ∀ n, ∀ᵐ x ∂μ, ‖F n x‖ ≤ g x)
    (hlim : ∀ᵐ x ∂μ, Filter.Tendsto (fun n => F n x)
      Filter.atTop (𝓝 (f x))) :
    Filter.Tendsto (fun n => ∫ x, F n x ∂μ)
      Filter.atTop (𝓝 (∫ x, f x ∂μ)) := by
  exact tendsto_integral_of_dominated_convergence g hF hg hbound hlim
```

関連：[数列と級数](sequences_series.md)、[連続性](limits_continuity.md#連続性)、[測度と可積分性](measure_integrals.md)。共通の構文：[公式リファレンス：関数](https://lean-lang.org/doc/reference/latest/The-Type-System/Functions/)。

[mathlib の索引に戻る](README.md)
