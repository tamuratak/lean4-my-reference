# 高階微分と滑らかさ

高階微分は、微分をさらに微分したもの。一変数では再び数やベクトル、多変数では複数の方向を受け取る多重線形写像として表す。

## 一変数の高階微分

$f:\mathbb{R}\to\mathbb{R}$ とする。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 第 $k$ 階微分 | $f^{(k)}(x)$ | `iteratedDeriv k f x` |
| 第二階微分 | $f''(x)$ | `iteratedDeriv 2 f x` |
| 領域内の第 $k$ 階微分 | 領域内の微分を $k$ 回反復 | `iteratedDerivWithin k f s x` |

`iteratedDeriv` は反復した微分の値を表す関数であり、それだけで必要な階数の微分が存在するという命題ではない。

## 多変数の高階微分

$f:E\to F$ の第 $k$ 階全微分は、$k$ 個の方向ベクトルを受け取る連続多重線形写像である。

$$
D^k f(x)(v_0,\ldots,v_{k-1})\in F.
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 第 $k$ 階全微分 | $D^k f(x)$ | `iteratedFDeriv ℝ k f x` |
| 方向への適用 | $D^k f(x)(v_0,\ldots,v_{k-1})$ | `iteratedFDeriv ℝ k f x v`（`v : Fin k → E`） |
| 第二階全微分の適用 | $D^2f(x)(u,v)$ | `iteratedFDeriv ℝ 2 f x ![u, v]` |
| 領域内の第 $k$ 階全微分 | $D_s^k f(x)$ | `iteratedFDerivWithin ℝ k f s x` |

$D_s^k f(x)$ は説明上の記号。方向の組を `Fin k → E` で表すのは、[点の座標を関数で表す](spaces.md)のと同じ考え方である。

## Hessian 行列

実数値の $C^2$ 関数 $f:\mathbb{R}^n\to\mathbb{R}$ の Hessian は、二階微分を標準基底で表示した行列である。

$$
H_f(x)_{ij}=D^2f(x)(e_i,e_j)
=\frac{\partial^2 f}{\partial x_i\,\partial x_j}(x),
\qquad
D^2f(x)(u,v)=u^{\mathsf T}H_f(x)v.
$$

`f : (Fin n → ℝ) → ℝ` とすると、成分は `iteratedFDeriv ℝ 2 f x ![Pi.single i 1, Pi.single j 1]` で表せる。行列全体はその式を `fun i j => ...` で並べたもの。

例えば $f(x,y)=x^2+y^2$ なら、

$$
H_f(x,y)=\begin{pmatrix}2&0\\0&2\end{pmatrix}.
$$

二階微分の値を記述することと、その存在・連続性を主張することは別である。混合偏微分の交換や Hessian の対称性を使うときには、$C^2$ などの条件を確認する。

## 連続微分可能性

| 意味 | 数学 | Lean |
| --- | --- | --- |
| $k$ 階連続微分可能 | $f\in C^k(E,F)$ | `ContDiff ℝ k f` |
| 点の近くで $k$ 階連続微分可能 | 点 $x$ での $C^k$ 条件 | `ContDiffAt ℝ k f x` |
| 領域上で $k$ 階連続微分可能 | 領域 $s$ での $C^k$ 条件 | `ContDiffOn ℝ k f s` |
| 領域内の点で $k$ 階連続微分可能 | 領域内から見た $C^k$ 条件 | `ContDiffWithinAt ℝ k f s x` |
| 滑らか | $f\in C^\infty$ | `ContDiff ℝ ∞ f` |
| 解析的な正則性 | $C^\omega$ 条件 | `ContDiff ℝ ω f` |

最後の二つの記法には `ContDiff` スコープを使う。この固定バージョンでは、階数の型は `WithTop ℕ∞` で、すべての有限階を表す `∞` と、解析的な条件を表す `ω` を区別する。

`WithTop α` は、型 `α` に新しい最大元 `⊤` を一つ追加する仕組みである。`ℕ∞` は正式名 `ENat` で、自然数に最大元を追加した `WithTop ℕ` として定義される。さらに `WithTop ℕ∞` にすると、元からある最大元より大きい最大元がもう一つ加わる。

| 階数 | 型の中での位置 | `ContDiff` スコープの記法 |
| --- | --- | --- |
| 有限階 $k$ | 自然数を埋め込んだ `(k : WithTop ℕ∞)`（`k : ℕ`） | `k` |
| すべての有限階 | `ℕ∞` の最大元を埋め込んだ `((⊤ : ℕ∞) : WithTop ℕ∞)` | `∞` |
| 解析的な条件 | 外側で追加した `(⊤ : WithTop ℕ∞)` | `ω` |

したがって階数の順序は $0<1<\cdots<\infty<\omega$ となり、`WithTop ℕ∞` 全体の `⊤` は `∞` ではなく `ω` である。`ℕ∞` は自然数の拡張であり、測度に使う拡張非負実数 `ENNReal` とは別の型である。

解析性は、点の近傍で収束する冪級数展開を持つことをいう。`ContDiff 𝕜 ω f` は全空間の各点で `AnalyticAt 𝕜 f x` が成立することと同値である。一点での `ContDiffAt 𝕜 ω f x` と `AnalyticAt 𝕜 f x` の同値には、値域 `F` の完備性 `[CompleteSpace F]` を使う。冪級数での表現は[解析性](spaces.md#解析性)を参照。

一般の空間・領域での厳密な条件は `ContDiff` の定義に従い、単に各点で微分を反復できるという条件より強い。

## 点での連続微分可能性と近傍

有限階 `n : ℕ` について、`ContDiffAt 𝕜 n f x` は、ある $x$ の近傍で $f$ が $C^n$ であるという条件である。`ContDiffAt.contDiffOn` で近傍と領域上の条件を取り出せる。

```lean
import Mathlib.Analysis.Calculus.ContDiff.Defs

open scoped Topology

example {f : ℝ → ℝ} {x : ℝ} {n : ℕ}
    (h : ContDiffAt ℝ n f x) :
    ∃ u ∈ 𝓝 x, ContDiffOn ℝ n f u := by
  exact h.contDiffOn le_rfl (by simp)
```

階数 $0$ でも近傍での連続性を要求する。`contDiffAt_zero` により次の同値が成り立つ。

```lean
import Mathlib.Analysis.Calculus.ContDiff.Defs

open scoped Topology

example {f : ℝ → ℝ} {x : ℝ} :
    ContDiffAt ℝ 0 f x ↔ ∃ u ∈ 𝓝 x, ContinuousOn f u := by
  exact contDiffAt_zero
```

`ContDiffAt` の `At` は、近傍条件を含む局所的な版にも使われる。連続性・微分可能性と共通する命名パターンは、[解析系の `At` と点・近傍の条件](at_and_neighborhoods.md)を参照。

### 無限階での量化の順序

`ContDiffAt 𝕜 ∞ f x` は、各有限階について `ContDiffAt 𝕜 n f x` が成立するという意味である。

```lean
import Mathlib.Analysis.Calculus.ContDiff.Defs

open scoped ContDiff

example {f : ℝ → ℝ} {x : ℝ} :
    ContDiffAt ℝ ∞ f x ↔ ∀ n : ℕ, ContDiffAt ℝ n f x := by
  exact contDiffAt_infty
```

近傍を明示すると、量化の順序は

$$
\forall n\in\mathbb{N},\ \exists U_n\text{：$x$ の近傍},\ f\in C^n(U_n)
$$

となる。近傍 $U_n$ は階数に依存してよい。すべての階数に共通する近傍 $U$ で $f\in C^\infty(U)$ という条件は、これより強い。

`ContDiffAt.eventually` は、同じ階数で近傍の各点にも `ContDiffAt` を移す定理だが、仮定 `n ≠ ∞` が必要である。有限階や `ω` には使えても、`∞` にそのまま適用することはできない。

関連：[全微分](fderiv.md)、[勾配](partial_gradient.md)、[ヤコビアン](linear_maps.md)。

[mathlib の索引に戻る](README.md)
