# mathlib の数学リファレンス

多変数・多次元の微分積分について、**数学の概念を mathlib でどのように表すか**をまとめる。数学の式から対応する型・関数・命題を探すための、自分用のリファレンスである。

各ページは [参照例](../../mathlib_deriv_example.md)に合わせ、「数学の対象」「数学と Lean の対応表」「表現の意味と条件」の順で説明する。証明コードやタクティクの使い方は、今後の別の課題として扱う。

## 概念から探す

| 数学の概念 | ページ | 主な名前 |
| --- | --- | --- |
| 点、座標、スカラー値・ベクトル値関数 | [空間と関数の型](spaces.md) | `Fin n`、`EuclideanSpace` |
| 領域、近傍、極限、連続性 | [領域・極限・連続性](limits_continuity.md) | `Set`、`Tendsto`、`ContinuousOn` |
| 線形写像、全微分の値、ヤコビアン行列 | [連続線形写像とヤコビアン](linear_maps.md) | `LinearMap`、`ContinuousLinearMap` |
| 一変数の微分、曲線の速度 | [一変数微分](deriv.md) | `deriv`、`HasDerivAt` |
| 全微分、領域内の微分、連鎖律 | [全微分と連鎖律](fderiv.md) | `fderiv`、`HasFDerivAt` |
| 偏微分、方向微分、勾配 | [偏微分・方向微分・勾配](partial_gradient.md) | `Function.update`、`gradient` |
| 高階微分、Hessian、滑らかさ | [高階微分と滑らかさ](higher_derivatives.md) | `iteratedFDeriv`、`ContDiff` |
| 向き付き区間積分、原始関数 | [区間積分と基本定理](interval_integrals.md) | `intervalIntegral`、`IntervalIntegrable` |
| 測度、可積分性、領域上の積分 | [測度と領域上の積分](measure_integrals.md) | `Measure`、`IntegrableOn` |
| 多重積分、累次積分、順序交換 | [多重積分と Fubini の定理](multiple_integrals.md) | `Measure.prod`、`integral_prod` |
| 変数変換、体積の倍率 | [変数変換とヤコビアンの行列式](change_variables.md) | `Set.InjOn`、`ContinuousLinearMap.det` |

## 値と命題を分けて読む

数学では「微分」と言うだけで、微分の値とその存在を同時に意識することが多い。mathlib では、それぞれ別の表現を使う。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 微分の値 | $f'(x)$ | `deriv f x` |
| 微分が存在し、その値が指定した値である | $f'(x)=a$、かつ微分可能 | `HasDerivAt f a x` |
| 全微分が存在する | $f$ は点 $x$ で全微分可能 | `DifferentiableAt ℝ f x` |
| 全微分の値 | $Df(x)$ | `fderiv ℝ f x` |
| 領域上で可積分である | $f\in L^1(s,\mu)$ | `MeasureTheory.IntegrableOn f s μ` |
| 領域上の積分の値 | $\int_s f\,d\mu$ | `∫ x in s, f x ∂μ` |

`deriv` や `fderiv` は微分不可能な点でも定義される。通常の積分も非可積分な関数に対して定義される。このため、**値の式が書けることと、数学的な存在条件が満たされることは別**である。各ページで、値と存在条件の対応を説明する。

## 記法の読み方

数学の説明には `$...$`・`$$...$$` による数式を使う。Lean 欄のインラインコードや `text` ブロックは、型・式・命題の表現を示す断片であり、完成したプログラムや証明ではない。

例えば数学の $\mathbb{R}$ は Lean では `ℝ` または `Real` と書く。数学の矢印と Lean の型の記法も区別する。線形写像の読みにくい下付き記法については、[正式名による表記](linear_maps.md#線形写像の型と正式名)も併記する。

このリファレンスは `lean-toolchain` と `lake-manifest.json` の固定バージョンを対象にする。mathlib の表現は固定した依存の宣言を確認して記載する。共通の Lean 構文については[公式リファレンス](https://lean-lang.org/doc/reference/latest/)を参照。mathlib 固有の数学の API を Lean 本体の資料で説明したことにはしない。

[リファレンスのトップに戻る](../../README.md)
