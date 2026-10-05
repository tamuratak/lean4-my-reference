# 区間積分と微積分の基本定理

一変数関数 $f:\mathbb{R}\to\mathbb{R}$ の向き付き区間積分

$$
\int_a^b f(x)\,dx
$$

を `∫ x in a..b, f x` で表す。端点は `a b : ℝ` とする。

## 区間積分の値と可積分性

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 向き付き区間積分 | $\int_a^b f(x)\,dx$ | `∫ x in a..b, f x` |
| 指定した測度での区間積分 | $\int_a^b f(x)\,d\mu(x)$ | `∫ x in a..b, f x ∂μ` |
| 向きを付けずに区間で可積分 | 端点間の区間でノルムの積分が有限 | `IntervalIntegrable f volume a b` |
| 原始関数の微分が被積分関数 | $F'(x)=f(x)$、かつ微分可能 | `HasDerivAt F (f x) x` |

区間積分は向きを持ち、

$$
\int_b^a f(x)\,dx=-\int_a^b f(x)\,dx.
$$

一方、`IntervalIntegrable` は端点の順序によらない。これは `MeasureTheory.IntegrableOn f (Set.uIoc a b) volume` と対応する条件である。`Set.uIoc a b` は $(\min(a,b),\max(a,b)]$ を表す。

## 領域上の積分との違い

$a\le b$ の場合、Lebesgue 測度では、

$$
\int_a^b f(x)\,dx=\int_{(a,b]}f(x)\,dx.
$$

`∫ x in Set.Icc a b, f x` は集合上の積分で、向きを持たない。$a>b$ なら集合は空になる。Lebesgue 測度では端点の違いは積分に影響しないが、点に質量を持つ一般の測度では端点の扱いにも注意する。

## 微積分の基本定理

原始関数 $F$ と被積分関数 $f$ について、

$$
F'(x)=f(x)
\quad\Longrightarrow\quad
\int_a^b f(x)\,dx=F(b)-F(a)
$$

という対応を使う。mathlib の `intervalIntegral.integral_eq_sub_of_hasDerivAt` では、次の条件を表す。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 端点間の閉区間で原始関数の微分が $f$ | $\forall x\in[\min(a,b),\max(a,b)],\ F'(x)=f(x)$ | `∀ x ∈ Set.uIcc a b, HasDerivAt F (f x) x` |
| 被積分関数が区間で可積分 | $f$ は端点間で可積分 | `IntervalIntegrable f volume a b` |
| 積分値の等式 | $\int_a^b f=F(b)-F(a)$ | `(∫ x in a..b, f x) = F b - F a` |

微分の条件には存在も含む。この定理は端点も含む点での `HasDerivAt` を使う。領域の内側からの微分だけを仮定する場合は、その条件に対応した基本定理と区別する。

区間積分は、完備なノルム空間へのベクトル値関数にも使える。その場合は積分値も出力空間のベクトルになる。

関連：[一変数微分](deriv.md)、[領域上の積分](measure_integrals.md)、[多重積分](multiple_integrals.md)。共通の記法：[公式リファレンス：構文とマクロ](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/)。

[mathlib の索引に戻る](README.md)
