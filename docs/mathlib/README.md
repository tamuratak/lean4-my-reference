# mathlib の数学リファレンス

多変数・多次元の微分積分と、その基礎になる級数・線形代数・位相について、**数学の概念を mathlib でどのように表すか**をまとめる。数学の式から対応する型・関数・命題を探すための、自分用のリファレンスである。

各ページは [参照例](../../mathlib_deriv_example.md)に合わせ、「数学の対象」「数学と Lean の対応表」「表現の意味と条件」の順で説明する。証明コードやタクティクの使い方は、今後の別の課題として扱う。

記号の形や呼び名から調べる場合は、[mathlib の記号索引](symbols.md)を参照。線形写像の矢印、近傍、勾配、積分、有限和などをまとめている。

## 概念から探す

| 数学の概念 | ページ | 主な名前 |
| --- | --- | --- |
| 点、座標、スカラー値・ベクトル値関数 | [空間と関数の型](spaces.md) | `Fin n`、`EuclideanSpace` |
| ベクトルの長さ、内積、直交、作用素ノルム | [ノルム・内積・直交性](norms_inner_products.md) | `norm`、`inner`、`OrthonormalBasis` |
| 領域、近傍、極限、連続性 | [領域・極限・連続性](limits_continuity.md) | `Set`、`Tendsto`、`ContinuousOn` |
| 内部、閉包、境界、コンパクト性、最大値・最小値 | [開集合・閉集合・コンパクト性](topology_compactness.md) | `IsOpen`、`IsClosed`、`IsCompact` |
| 数列、部分和、無限和、級数の収束 | [数列・有限和・級数](sequences_series.md) | `Finset.sum`、`HasSum`、`Summable`、`tsum` |
| 行列積、基底、座標、核・像 | [行列・基底・線形代数](matrices_basis.md) | `Matrix`、`Module.Basis`、`LinearMap.toMatrix` |
| 線形写像、全微分の値、ヤコビアン行列 | [連続線形写像とヤコビアン](linear_maps.md) | `LinearMap`、`ContinuousLinearMap` |
| 一変数の微分、曲線の速度 | [一変数微分](deriv.md) | `deriv`、`HasDerivAt` |
| 全微分、領域内の微分、連鎖律 | [全微分と連鎖律](fderiv.md) | `fderiv`、`HasFDerivAt` |
| 偏微分、方向微分、勾配 | [偏微分・方向微分・勾配](partial_gradient.md) | `Function.update`、`gradient` |
| 高階微分、Hessian、滑らかさ | [高階微分と滑らかさ](higher_derivatives.md) | `iteratedFDeriv`、`ContDiff` |
| 向き付き区間積分、原始関数 | [区間積分と基本定理](interval_integrals.md) | `intervalIntegral`、`IntervalIntegrable` |
| 測度、可積分性、領域上の積分 | [測度と領域上の積分](measure_integrals.md) | `Measure`、`IntegrableOn` |
| 多重積分、累次積分、順序交換 | [多重積分と Fubini の定理](multiple_integrals.md) | `Measure.prod`、`integral_prod` |
| 変数変換、体積の倍率 | [変数変換とヤコビアンの行列式](change_variables.md) | `Set.InjOn`、`ContinuousLinearMap.det` |
| 各点収束、一様収束、積分と極限の交換 | [関数列と極限の交換](function_sequences.md) | `TendstoUniformlyOn`、`tendsto_integral_of_dominated_convergence` |

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
| 級数が無条件収束し、和が指定した値である | $\sum_n u_n=a$、かつ無条件収束 | `HasSum u a` |
| 無限和の値 | $\sum_n u_n$ | `tsum u` |

`deriv` や `fderiv` は微分不可能な点でも定義される。通常の積分も非可積分な関数に対して定義され、`tsum` も収束条件を満たさない場合に定義される。このため、**値の式が書けることと、数学的な存在条件が満たされることは別**である。各ページで、値と存在条件の対応を説明する。

## 記法の読み方

数学の説明には `$...$`・`$$...$$` による数式を使う。Lean 欄のインラインコードや `text` ブロックは、型・式・命題の表現を示す断片であり、完成したプログラムや証明ではない。

例えば数学の $\mathbb{R}$ は Lean では `ℝ` または `Real` と書く。数学の矢印と Lean の型の記法も区別する。線形写像の読みにくい下付き記法については、[正式名による表記](linear_maps.md#線形写像の型と正式名)も併記する。

このリファレンスは `lean-toolchain` と `lake-manifest.json` の固定バージョンを対象にする。mathlib の表現は固定した依存の宣言を確認して記載する。共通の Lean 構文については[公式リファレンス](https://lean-lang.org/doc/reference/latest/)を参照。mathlib 固有の数学の API を Lean 本体の資料で説明したことにはしない。

[リファレンスのトップに戻る](../../README.md)
