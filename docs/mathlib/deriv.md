# 一変数微分と曲線の速度

一変数実数値関数 $f:\mathbb{R}\to\mathbb{R}$ を `f : ℝ → ℝ`、微分する点 $x$ を `x : ℝ` で表す。

$$
f'(x)=\lim_{h\to 0,\ h\ne 0}\frac{f(x+h)-f(x)}{h}.
$$

## 微分の値と微分可能性

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 微分の値 | $f'(x)$ | `deriv f x` |
| 微分が存在し、その値が $a$ | $f'(x)=a$、かつ微分可能 | `HasDerivAt f a x` |
| 点で微分可能 | $f$ は点 $x$ で微分可能 | `DifferentiableAt ℝ f x` |
| 全体で微分可能 | すべての点で微分可能 | `Differentiable ℝ f` |
| 領域内での微分の値 | $s$ 内から見た微分 | `derivWithin f s x` |
| 領域内で微分が存在し、その値が $a$ | $s$ 内から見た微分が $a$ | `HasDerivWithinAt f a s x` |
| 領域上で微分可能 | $s$ の各点で領域内の微分が存在 | `DifferentiableOn ℝ f s` |

`deriv f x` は値を表す。`HasDerivAt f a x` は、その微分が存在し、その値が $a$ であるという命題を表す。例えば $f(t)=t^2$ について、数学の $f'(x)=2x$ は次の二つの表現に分かれる。

| 意味 | Lean |
| --- | --- |
| 微分値の等式 | `deriv (fun t : ℝ => t ^ 2) x = 2 * x` |
| 存在を含む微分の主張 | `HasDerivAt (fun t : ℝ => t ^ 2) (2 * x) x` |

`deriv` は微分不可能な点では $0$ を返す。そのため微分値が $0$ という等式だけでは、微分可能な停留点であるとは言えない。`derivWithin` でも、選ばれた値と存在・一意性の条件を区別する。

`HasDerivAt f a x` と `DifferentiableAt ℝ f x` は、点 $x$ での微分を要求する。近傍のすべての点での微分可能性を使うには、別にその条件が必要である。連続微分可能性・解析性などの範囲の違いは、[解析系の `At` と点・近傍の条件](at_and_neighborhoods.md)を参照。

## ベクトル値の一変数関数

曲線 $\gamma:\mathbb{R}\to\mathbb{R}^m$ は `gamma : ℝ → (Fin m → ℝ)` で表す。その微分 $\gamma'(t)$ は速度ベクトルである。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 速度ベクトル | $\gamma'(t)\in\mathbb{R}^m$ | `deriv gamma t` |
| 速度が $v$ である | $\gamma'(t)=v$、かつ微分可能 | `HasDerivAt gamma v t` |

`HasDerivAt` は入力が一つのスカラーである場合の微分であり、出力はベクトルでもよい。出力が多次元だから全微分の記法に変える、という区別ではない。

## 積と合成の微分

$$
(fg)'(x)=f'(x)g(x)+f(x)g'(x),
\qquad
(g\circ f)'(x)=g'(f(x))f'(x).
$$

対応する微分命題を結び付ける定理は `HasDerivAt.mul` と `HasDerivAt.comp`。合成では、内側の関数は点 $x$、外側の関数は点 $f(x)$ で微分する。

関連：[全微分](fderiv.md)、[偏微分](partial_gradient.md)、[区間積分](interval_integrals.md)。共通の構文：[公式リファレンス：関数](https://lean-lang.org/doc/reference/latest/The-Type-System/Functions/)。

[mathlib の索引に戻る](README.md)
