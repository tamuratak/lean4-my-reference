# 解析系の `At` と点・近傍の条件

mathlib の解析系 API では、`At` は基準点を指定する命題の名前に使われる。`ContDiffAt` のように、近傍での条件を含む命題にも `At` が付く。名前の `At` は基準点を指定し、要求する条件の範囲は各命題の定義が決める。

## 全体・領域・基準点の命名パターン

連続性、微分可能性、連続微分可能性には、全体・領域・基準点による共通の命名パターンがある。

| API の版 | 連続性 | 微分可能性 | 連続微分可能性 |
| --- | --- | --- | --- |
| 全空間 | `Continuous` | `Differentiable` | `ContDiff` |
| 領域を指定 | `ContinuousOn` | `DifferentiableOn` | `ContDiffOn` |
| 基準点を指定 | `ContinuousAt` | `DifferentiableAt` | `ContDiffAt` |
| 領域と基準点を指定 | `ContinuousWithinAt` | `DifferentiableWithinAt` | `ContDiffWithinAt` |

例えば `ContDiffAt 𝕜 n f x` は、`ContDiffWithinAt 𝕜 n f Set.univ x` として定義される。`At` と `WithinAt` の対応は、近づく領域を全空間にするか、指定した集合にするかという API の構造に沿っている。

```lean
import Mathlib.Analysis.Calculus.ContDiff.Defs

example {f : ℝ → ℝ} {x : ℝ} :
    ContDiffAt ℝ 1 f x ↔ ContDiffWithinAt ℝ 1 f Set.univ x := by
  rfl
```

## 局所的な API と近傍での一致

連続性・連続微分可能性・解析性の API には、関数が基準点の近傍で一致すれば性質を移せる定理がある。`ContinuousAt.congr_of_eventuallyEq`、`ContDiffAt.congr_of_eventuallyEq`、`AnalyticAt.congr` などである。`ContinuousAt`・`ContDiffAt`・`AnalyticAt` は、基準点の近くでの関数の振る舞いを扱う。

```lean
import Mathlib.Analysis.Calculus.ContDiff.Defs

open scoped Topology

example {f g : ℝ → ℝ} {x : ℝ}
    (h : ContDiffAt ℝ 1 f x) (hgf : g =ᶠ[𝓝 x] f) :
    ContDiffAt ℝ 1 g x := by
  exact h.congr_of_eventuallyEq hgf
```

階数 `∞` では近傍を有限階ごとに選べる。定義と利用例は[点での連続微分可能性と近傍](higher_derivatives.md#点での連続微分可能性と近傍)を参照。

## `At` を持つ命題の範囲

| 数学の対象 | Lean | 条件の範囲 |
| --- | --- | --- |
| 連続性 | `ContinuousAt f x` | 点 $x$ での極限が $f(x)$ と一致 |
| 微分の存在と値 | `HasDerivAt f a x`、`HasFDerivAt f A x` | 点 $x$ を固定した一次近似 |
| 微分可能性 | `DifferentiableAt 𝕜 f x` | 点 $x$ で全微分が存在 |
| 方向微分 | `HasLineDerivAt 𝕜 f a x v`、`LineDifferentiableAt 𝕜 f x v` | $t\mapsto f(x+tv)$ の $t=0$ での微分 |
| 勾配 | `HasGradientAt f g x` | 点 $x$ の全微分を内積で表現 |
| 等角性 | `ConformalAt f x` | 点 $x$ の全微分が等角な線形写像 |
| 狭義微分 | `HasStrictDerivAt f a x`、`HasStrictFDerivAt f A x` | 二点 $y,z$ をともに $x$ に近づけた一次近似 |
| 有限階の連続微分可能性 | `ContDiffAt 𝕜 n f x`（`n : ℕ`） | ある近傍で $C^n$ |
| 全有限階の連続微分可能性 | `ContDiffAt 𝕜 ∞ f x` | 各有限階 $n$ について、ある近傍で $C^n$ |
| 解析性 | `AnalyticAt 𝕜 f x` | $x$ を中心とする冪級数がある近傍で $f$ に収束 |
| 指定した冪級数による展開 | `HasFPowerSeriesAt f p x` | 指定した級数 `p` がある近傍で $f$ に収束 |
| 有限冪級数による展開 | `CPolynomialAt 𝕜 f x`、`HasFiniteFPowerSeriesAt f p x n` | ある近傍で有限冪級数と一致。後者は級数 `p` と、次数が `n` 未満であることも指定 |
| 有理型性 | `MeromorphicAt f x` | 穴あき近傍で、有限次数の極を許す解析的な振る舞い |
| 調和性 | `InnerProductSpace.HarmonicAt f x` | ある近傍で $C^2$ かつラプラシアンが零 |
| 局所的な積分曲線 | `IsIntegralCurveAt gamma v t₀` | ある近傍の各時刻で $\gamma'(t)=v(t,\gamma(t))$ |
| 畳み込みの存在 | `ConvolutionExistsAt f g x L μ` | $x$ を固定した被積分関数 `fun t => L (f t) (g (x - t))` が `μ` に関して可積分。積分変数 `t` の全域にわたる条件 |

## 解析性の領域内と近傍での条件

`AnalyticOn 𝕜 f s` と `AnalyticOnNhd 𝕜 f s` は、冪級数展開と関数値の一致を要求する範囲が異なる。

| 命題 | 冪級数展開を要求する範囲 |
| --- | --- |
| `AnalyticOn 𝕜 f s` | $s$ に属する点 $x$ ごとに、$x$ の近傍のうち $s$ 内で展開が成立。$s$ 外の関数値には条件を課さない |
| `AnalyticOnNhd 𝕜 f s` | $s$ に属する点 $x$ ごとに、$s$ 外も含む $x$ の近傍全体で展開が成立 |

特に境界では、`AnalyticOn` は領域内だけの展開でよいが、`AnalyticOnNhd` は領域外にも同じ展開が成立することを要求する。

関連：[領域・極限・連続性](limits_continuity.md)、[フィルターと極限](filters.md)、[一変数微分](deriv.md)、[全微分](fderiv.md)、[高階微分と滑らかさ](higher_derivatives.md)、[解析性](spaces.md#解析性)。

[mathlib の索引に戻る](README.md)
