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

最後の二つの記法には `ContDiff` スコープを使う。この固定バージョンでは、階数の型は `WithTop ℕ∞` で、すべての有限階を表す `∞` と、解析的な条件を表す `ω` を区別する。一般の空間・領域での厳密な条件は `ContDiff` の定義に従い、単に各点で微分を反復できるという条件より強い。

関連：[全微分](fderiv.md)、[勾配](partial_gradient.md)、[ヤコビアン](linear_maps.md)。

[mathlib の索引に戻る](README.md)
