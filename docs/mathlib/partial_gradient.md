# 偏微分・方向微分・勾配

$n$ 変数実数値関数

$$
f(x_0,\ldots,x_{n-1})
$$

を `f : (Fin n → ℝ) → ℝ` で表す。点は `x : Fin n → ℝ`、座標番号は `i : Fin n` である。

## 偏微分

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 第 $i$ 変数についての偏微分 | $\displaystyle\frac{\partial f}{\partial x_i}(x)$ | `deriv (fun t => f (Function.update x i t)) (x i)` |
| 第 $i$ 偏微分が存在し、その値が $a$ | $\displaystyle\frac{\partial f}{\partial x_i}(x)=a$、かつ微分可能 | `HasDerivAt (fun t => f (Function.update x i t)) a (x i)` |
| 第 $i$ 変数の断面が微分可能 | $t\mapsto f(x_0,\ldots,t,\ldots,x_{n-1})$ は $t=x_i$ で微分可能 | `DifferentiableAt ℝ (fun t => f (Function.update x i t)) (x i)` |

`Function.update x i t` は、点 $x$ の第 $i$ 成分だけを $t$ に置き換えた点

$$
(x_0,\ldots,x_{i-1},t,x_{i+1},\ldots,x_{n-1})
$$

を表す。したがって `fun t => f (Function.update x i t)` は、他の変数を固定した一変数関数である。その関数を元の座標値 `x i` で微分することで偏微分を表す。

`deriv` は値、`HasDerivAt` は存在と指定した値を含む命題。すべての偏微分が存在するだけでは、全微分が存在するとは限らない。

## 方向微分

方向 $v\in\mathbb{R}^n$ に沿う微分は、直線 $t\mapsto x+tv$ に関数を制限した微分である。

$$
D_v f(x)=\left.\frac{d}{dt}f(x+tv)\right|_{t=0}.
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 方向微分の値 | $D_v f(x)$ | `deriv (fun t : ℝ => f (x + t • v)) 0` |
| 方向微分が存在し、その値が $a$ | $D_v f(x)=a$、かつ微分可能 | `HasDerivAt (fun t : ℝ => f (x + t • v)) a 0` |
| 全微分を方向に適用 | $Df(x)(v)$ | `fderiv ℝ f x v` |
| 全微分を第 $i$ 座標方向に適用 | $Df(x)(e_i)$ | `fderiv ℝ f x (Pi.single i 1)` |

全微分可能なら、

$$
D_v f(x)=Df(x)(v),\qquad
\frac{\partial f}{\partial x_i}(x)=Df(x)(e_i).
$$

`Pi.single i 1` は第 $i$ 成分だけが $1$ のベクトル。方向微分は特定の直線上の微分、全微分はすべての増分に対する一つの線形近似であり、同じ存在条件ではない。

## 曲線に沿う微分

曲線 $\gamma:\mathbb{R}\to E$ に沿って関数 $f:E\to\mathbb{R}$ を微分すると、

$$
\frac{d}{dt}f(\gamma(t))=Df(\gamma(t))(\gamma'(t)).
$$

| 意味 | Lean |
| --- | --- |
| 曲線に沿う一変数関数 | `fun t => f (gamma t)` |
| その微分の値 | `deriv (fun t => f (gamma t)) t` |
| 全微分を速度に適用 | `fderiv ℝ f (gamma t) (deriv gamma t)` |

この式は $f$ と曲線が対応する点で微分可能な場合の連鎖律である。対応する定理名は `HasFDerivAt.comp_hasDerivAt`。

## 勾配

勾配には内積が必要なので、ここでは点を `x : EuclideanSpace ℝ (Fin n)`、関数を `f : EuclideanSpace ℝ (Fin n) → ℝ` とする。

$$
Df(x)(v)=\langle\nabla f(x),v\rangle.
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 勾配の値 | $\nabla f(x)$ | `gradient f x` |
| 勾配が存在し、その値が $g$ | $\nabla f(x)=g$、かつ全微分可能 | `HasGradientAt f g x` |
| 勾配を線形汎関数にする | $v\mapsto\langle g,v\rangle$ | `InnerProductSpace.toDual ℝ _ g` |
| 領域内で選ばれた勾配 | $\nabla_s f(x)$ | `gradientWithin f s x` |
| 領域内の勾配が $g$ | 領域内の全微分を $g$ との内積で表す | `HasGradientWithinAt f g s x` |

$\nabla_s f(x)$ は説明上の記号である。`gradient` の値は入力と同じ空間のベクトルであり、`fderiv` の値は連続線形写像。この二つは内積を通じて対応する。`gradient` も全微分不可能な点では零ベクトルを返す。

例えばユークリッド空間で $f(x,y)=x^2+y^2$ なら、

$$
\nabla f(x,y)=(2x,2y),\qquad
D_{(u,v)}f(x,y)=2xu+2yv.
$$

関連：[一変数微分](deriv.md)、[全微分](fderiv.md)、[高階微分](higher_derivatives.md)。

[mathlib の索引に戻る](README.md)
