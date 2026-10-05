# 全微分と連鎖律

$n$ 変数のベクトル値関数 $f:\mathbb{R}^n\to\mathbb{R}^m$ を `f : (Fin n → ℝ) → (Fin m → ℝ)` で表す。点は `x : Fin n → ℝ` である。

## Fréchet 微分

全微分 $Df(x)$ は、点 $x$ の近くでの一次近似を与える連続線形写像である。

$$
f(x+h)=f(x)+Df(x)(h)+o(\lVert h\rVert).
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 全微分の値 | $Df(x)$ | `fderiv ℝ f x` |
| 全微分を増分に適用 | $Df(x)(h)$ | `fderiv ℝ f x h` |
| 全微分が存在し、その値が $A$ | $Df(x)=A$、かつ全微分可能 | `HasFDerivAt f A x` |
| 点で全微分可能 | $f$ は点 $x$ で全微分可能 | `DifferentiableAt ℝ f x` |
| 全空間で全微分可能 | すべての点で全微分可能 | `Differentiable ℝ f` |

`fderiv ℝ f x` の型は、入力空間から出力空間への実連続線形写像。[正式名による表記](linear_maps.md#線形写像の型と正式名)も参照。

`HasFDerivAt f A x` が表す条件は、

$$
\frac{\lVert f(x+h)-f(x)-A(h)\rVert}{\lVert h\rVert}
\longrightarrow 0
\qquad(h\to 0,\ h\ne 0).
$$

すべての方向の増分に対してこの近似が成り立つ。偏微分が個別に存在することだけでは、全微分可能とは限らない。

`fderiv` は全微分不可能な点では零写像を返す。したがって `fderiv ℝ f x = 0` だけでは、全微分が存在して零写像であることまで主張できない。

## 領域内の全微分

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 領域内で選ばれた全微分 | $D_s f(x)$ | `fderivWithin ℝ f s x` |
| 領域内の全微分が $A$ | $s$ 内の増分で一次近似が成立 | `HasFDerivWithinAt f A s x` |
| 領域内で全微分可能 | $x$ で $s$ 内の全微分が存在 | `DifferentiableWithinAt ℝ f s x` |
| 領域上で全微分可能 | $s$ の各点で領域内の全微分が存在 | `DifferentiableOn ℝ f s` |
| 領域内の微分の一意性を保証する条件 | 許された増分で線形写像を一意に決められる | `UniqueDiffWithinAt ℝ s x` |

$D_s f(x)$ はこのページで使う説明上の記号である。領域内では $x+h\in s$ を満たす増分だけで一次近似を調べる。例えば領域が点一つだけだと、周囲の変化から微分を決めることができない。

このため `HasFDerivWithinAt f A s x` から選ばれた値 `fderivWithin ℝ f s x` が $A$ と等しいと読むには、一意性の条件も必要になる。開領域の内部、境界、低次元の領域は区別する。

## 連鎖律

$f:E\to F$ と $g:F\to G$ の合成では、

$$
D(g\circ f)(x)=Dg(f(x))\circ Df(x).
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 合成関数 | $g\circ f$ | `fun x => g (f x)` |
| 内側の全微分 | $Df(x)$ | `fderiv ℝ f x` |
| 外側の全微分 | $Dg(f(x))$ | `fderiv ℝ g (f x)` |
| 微分写像の合成 | $B\circ A$ | `B.comp A` |

内側と外側がそれぞれ微分可能な場合に、この対応を結び付ける定理が `HasFDerivAt.comp` である。基底を選んだ有限次元の表示では、写像の合成がヤコビアン行列の積になる。

関連：[連続線形写像](linear_maps.md)、[偏微分と勾配](partial_gradient.md)、[高階微分](higher_derivatives.md)。

[mathlib の索引に戻る](README.md)
