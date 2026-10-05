# 多重積分と Fubini の定理

二変数関数 $f:\mathbb{R}^2\to\mathbb{R}$ を `f : (ℝ × ℝ) → ℝ` で表す。二重積分は積空間上の積分であり、累次積分は一変数ずつ順に積分する表現である。

## 積測度と二重積分

測度 $\mu,\nu$ の積測度は $\mu\otimes\nu$。Lean では `μ.prod ν` で表す。以下の測度・可積分性・定理名は `MeasureTheory` 名前空間のもの。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 積測度 | $\mu\otimes\nu$ | `μ.prod ν` |
| 積空間の積分 | $\int_{\mathbb{R}^2}f\,d(\mu\otimes\nu)$ | `∫ p, f p ∂(μ.prod ν)` |
| 先に第二変数を積分 | $\int\left(\int f(x,y)\,d\nu(y)\right)d\mu(x)$ | `∫ x, ∫ y, f (x, y) ∂ν ∂μ` |
| 積空間で可積分 | $f\in L^1(\mu\otimes\nu)$ | `Integrable f (μ.prod ν)` |

内側の積分が第二変数、外側の積分が第一変数に対応する。積分の次数は出力の次元ではなく、入力の変数と領域に関係する。

## Fubini の定理

積測度で可積分なら、積空間の積分と累次積分が一致する。

$$
\int f\,d(\mu\otimes\nu)
=\int\left(\int f(x,y)\,d\nu(y)\right)d\mu(x).
$$

この対応を表す定理が `integral_prod`。この固定バージョンでは、測度の条件 `SFinite μ`・`SFinite ν` に加え、`Integrable f (μ.prod ν)` を使う。`SFinite` は有限測度の可算和として表せることを意味する。通常の $\sigma$ 有限測度はこの条件を満たし、実数上の Lebesgue 測度も該当する。

$f$ が `f : ℝ → ℝ → ℝ` のように二つの引数を順に受け取る場合、積空間上の可積分性は `Integrable (Function.uncurry f) (μ.prod ν)` で表す。

## 積分の順序交換

$$
\int\left(\int f(x,y)\,d\nu(y)\right)d\mu(x)
=\int\left(\int f(x,y)\,d\mu(x)\right)d\nu(y).
$$

| 意味 | Lean（`f : ℝ → ℝ → ℝ`） |
| --- | --- |
| 第二変数を先に積分 | `∫ x, ∫ y, f x y ∂ν ∂μ` |
| 第一変数を先に積分 | `∫ y, ∫ x, f x y ∂μ ∂ν` |
| 順序交換に使う可積分性 | `Integrable (Function.uncurry f) (μ.prod ν)` |
| 順序交換の定理名 | `integral_integral_swap` |

各断面について積分の値が書けることだけでは、積空間での可積分性を満たしたことにはならない。

## 領域上の多重積分

長方形の領域 $s\times t$ では、可測な領域について制限測度の積を使える。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 長方形の測度 | $(\mu\vert_s)\otimes(\nu\vert_t)$ | `(μ.restrict s).prod (ν.restrict t)` |
| 領域ごとの累次積分 | $\int_s\left(\int_t f(x,y)\,d\nu(y)\right)d\mu(x)$ | `∫ x in s, ∫ y in t, f (x, y) ∂ν ∂μ` |
| 有限区間の累次積分 | $\int_a^b\left(\int_c^d f(x,y)\,dy\right)dx$ | `∫ x in a..b, ∫ y in c..d, f (x, y)` |

一般の領域 $D$ では、断面

$$
D_x=\{y\mid(x,y)\in D\}
$$

が第一変数によって変わる。例えば三角形 $0\le y\le x\le1$ の積分は $\int_0^1\int_0^x f(x,y)\,dy\,dx$ であり、内側の上限が変わる。Lean の表現は `∫ x in (0 : ℝ)..1, ∫ y in (0 : ℝ)..x, f (x, y)` となる。

## 非負積分との違い

非負関数の `∫⁻` に対する Tonelli 型の定理では、無限大を許して積分を交換する。通常の `∫` に対する Fubini では可積分性を確認する。同じ二重積分に見えても、値域と前提が異なる。

関連：[測度と可積分性](measure_integrals.md)、[区間積分](interval_integrals.md)、[変数変換](change_variables.md)。

[mathlib の索引に戻る](README.md)
