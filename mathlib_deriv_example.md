Lean では $n$ 変数実数値関数

$$
f(x_0,\dots,x_{n-1})
$$

を `f : (Fin n → ℝ) → ℝ` で表す。また点 $x=(x_0,\dots,x_{n-1})$ は `x : Fin n → ℝ` である。

| 意味 | 数学 | Lean |
|---|---|---|
| 第 $i$ 変数についての偏微分 | $\displaystyle \frac{\partial f}{\partial x_i}(x)$ | `deriv (fun t => f (Function.update x i t)) (x i)` |
| 第 $i$ 偏微分が $a$ である | $\displaystyle \frac{\partial f}{\partial x_i}(x)=a$ | `HasDerivAt (fun t => f (Function.update x i t)) a (x i)` |
| $f$ の Fréchet 微分 | $\displaystyle Df(x)$ | `fderiv ℝ f x` |

ここで `Function.update x i t` は、$x$ の第 $i$ 成分だけを $t$ に置き換えた点

$$
(x_0,\dots,x_{i-1},t,x_{i+1},\dots,x_{n-1})
$$

を表す。したがって

`deriv (fun t => f (Function.update x i t)) (x i)`

は、第 $i$ 変数に関する偏微分

$$
\frac{\partial f}{\partial x_i}(x)
$$

である。

`deriv` は偏微分の値を表す。`HasDerivAt ... a ...` は、その偏微分が存在し、その値が $a$ であるという命題を表す。

`fderiv ℝ f x` は、$x$ における Fréchet 微分

$$
Df(x):\mathbb R^n\to\mathbb R
$$

を表す。これは $x$ の近傍における $f$ の一次近似を与える連続線形写像であり、

$$
f(x+h)=f(x)+Df(x)\,h+o(\|h\|)
$$

である。
