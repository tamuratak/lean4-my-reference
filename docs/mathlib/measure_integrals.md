# 測度・可積分性・領域上の積分

領域 $s\subseteq E$ 上の関数を積分するときは、領域と測度を指定する。

$$
\int_s f(x)\,d\mu(x).
$$

領域は `s : Set E`、測度は `μ : MeasureTheory.Measure E`。mathlib の通常の積分は Bochner 積分であり、実数値とベクトル値を扱う。

## 測度と積分の表現

以下の `Measure`、`Integrable` などは `MeasureTheory` 名前空間の宣言である。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 測度 | $\mu$ | `μ : Measure E` |
| 標準の体積測度 | Lebesgue 測度・体積測度 | `volume` |
| 全空間の積分 | $\int_E f\,d\mu$ | `∫ x, f x ∂μ` |
| 領域上の積分 | $\int_s f\,d\mu$ | `∫ x in s, f x ∂μ` |
| 標準の体積測度による領域上の積分 | $\int_s f(x)\,dx$ | `∫ x in s, f x` |
| 測度を領域に制限 | $\mu\vert_s$ | `μ.restrict s` |

`volume` は型に応じた既定の測度。実数では Lebesgue 測度、標準のユークリッド空間では体積測度になる。型に対応する測度の構造が必要であり、任意の型に体積測度が自動で存在するわけではない。

領域上の積分は、制限した測度による全空間の積分である。

$$
\int_s f\,d\mu=\int_E f\,d(\mu\vert_s).
$$

したがって `∫ x in s, f x ∂μ` は `∫ x, f x ∂(μ.restrict s)` に対応する。

## 可測性と可積分性

Bochner 可積分性では、必要な可測性に加え、

$$
\int_E\lVert f(x)\rVert\,d\mu(x)<\infty
$$

を要求する。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 領域が可測 | $s$ は可測集合 | `MeasurableSet s` |
| 関数が可測 | $f$ は可測関数 | `Measurable f` |
| 積分に必要な可測性 | $\mu$ に関してほとんど至る所で強可測 | `AEStronglyMeasurable f μ` |
| 全空間で可積分 | $f\in L^1(E,\mu)$ | `Integrable f μ` |
| 領域上で可積分 | $f\in L^1(s,\mu)$ | `IntegrableOn f s μ` |

ここで $f\in L^1$ は可積分性の条件を表す数学上の略記であり、Lean の関数型を `MeasureTheory.Lp` の型に変更したという意味ではない。`IntegrableOn f s μ` は `Integrable f (μ.restrict s)` と同じ条件である。

可測性だけでは可積分性は得られない。連続関数も、無限の領域では可積分とは限らない。例えば実数全体の定数関数 $f(x)=1$ は連続だが Lebesgue 可積分ではない。

## 積分値と存在条件

`∫ x, f x ∂μ` は値の式、`Integrable f μ` は可積分性の命題。通常の積分は非可積分の場合も定義され、その場合は零を返す。積分値が零であることだけで、可積分性を結論しない。

例えば可積分な $f,g$ についての線形性

$$
\int_E(f+g)\,d\mu=\int_E f\,d\mu+\int_E g\,d\mu
$$

にはそれぞれの可積分性が必要で、対応する定理が `MeasureTheory.integral_add` である。

## 非負関数の積分

非負関数の積分では無限大を許す値域 $[0,\infty]$ を使う。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 拡張非負実数の型 | $[0,\infty]$ | `ENNReal` |
| 非負積分 | $\int_E f\,d\mu\in[0,\infty]$ | `∫⁻ x, f x ∂μ` |

これは実数・ベクトル値の通常の積分 `∫` と区別する。無限大を許す非負積分と、ノルムの積分の有限性を要求する Bochner 積分では、積分の順序交換の前提も異なる。

関連：[区間積分](interval_integrals.md)、[多重積分](multiple_integrals.md)、[変数変換](change_variables.md)。共通の構文：[公式リファレンス：命題と証明](https://lean-lang.org/doc/reference/latest/The-Type-System/Propositions/)。

[mathlib の索引に戻る](README.md)
