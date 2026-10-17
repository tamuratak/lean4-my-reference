# 確率積分と二次変分

確率積分は、時間に依存するランダムな被積分過程を、別の確率過程の増分に対して積分する操作である。Brownian Motion は、単純過程の積分、予測可能性、変動過程、予測可能二次変分と、一般の積分が満たす性質を表現する定義を提供する。

## 予測可能性と単純過程

予測可能性は、左連続な適合過程などを可測にする時間と標本点の上の可測構造によって表される。

#### 提供モジュール：mathlib

| 対象・性質 | 宣言名 |
| --- | --- |
| 予測可能な可測構造 | `MeasureTheory.Filtration.predictable` |
| 強予測可能な過程 | `MeasureTheory.IsStronglyPredictable` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Predictable`

| 対象・性質 | 宣言名 |
| --- | --- |
| 左連続な強適合過程の予測可能性 | `MeasureTheory.StronglyAdapted.isStronglyPredictable_of_leftContinuous` |
| 停止過程の予測可能性 | `MeasureTheory.IsStronglyPredictable.stoppedProcess` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.SimpleProcess`

| 対象・性質 | 宣言名 |
| --- | --- |
| 基本予測可能集合の有限和 | `ProbabilityTheory.ElementaryPredictableSet` |
| 単純過程 | `ProbabilityTheory.SimpleProcess` |

単純過程は、$\mathcal{F}_{s_k}$ 可測な有界確率変数 $\xi_k$ を係数とする

$$
H_t=\sum_k\xi_k\mathbf{1}_{(s_k,t_k]}(t)
$$

と、最小時刻での値を保持する。`SimpleProcess` は区間と係数の有限な表現を持つデータ型であり、同じ関数を表す異なる要素が存在する。

## 単純過程の積分

単純過程の積分は、各区間の係数と積分対象の増分の積を足すことで定義できる。実数値の場合の基本形は

$$
\int_0^u H\,dY=\sum_k\xi_k(Y_{t_k\wedge u}-Y_{s_k\wedge u})
$$

である。`SimpleProcess.integral` は連続双線形写像も扱う一般化された形を提供する。

| 内容 | 宣言名 |
| --- | --- |
| 積分過程 | `ProbabilityTheory.SimpleProcess.integral` |
| 連続線形写像の評価を使う積分過程 | `ProbabilityTheory.SimpleProcess.integralEval` |
| 自然数時間の実数値積分の和による公式 | `ProbabilityTheory.SimpleProcess.integral_real_ofNat_apply` |
| 停止と積分の関係 | `ProbabilityTheory.SimpleProcess.stoppedProcess_integral` |
| 積分の結合関係 | `ProbabilityTheory.SimpleProcess.integral_assoc` |
| 積分の結合関係 | `ProbabilityTheory.SimpleProcess.integralEval_assoc` |
| 基本予測可能集合の指示過程 | `ProbabilityTheory.ElementaryPredictableSet.indicator` |
| 単純過程の強予測可能性 | `ProbabilityTheory.SimpleProcess.isStronglyPredictable` |

モジュールは `BrownianMotion.StochasticIntegral.SimpleProcess` である。一般の被積分過程に対する極限構成を使わず、有限和としての積分を与える段階に当たる。

## 変動過程と単調過程

変動過程は各経路の区間上の全変動を時間の関数として並べたものである。単調な右連続過程からは、各標本点に対する Stieltjes 測度も得られる。

#### 提供モジュール：`BrownianMotion.StochasticIntegral.VariationProcess`

| 内容 | 宣言名 |
| --- | --- |
| 経路の変動過程 | `variationProcess` |
| 変動過程の非負性・単調性 | `variationProcess_nonneg` |
| 変動過程の非負性・単調性 | `monotone_variationProcess` |
| 連続・片側連続な経路の変動の可測性 | `measurable_eVariationOn_of_continuousWithinAt` と左右片側版 |
| 変動過程の適合性 | `MeasureTheory.StronglyAdapted.adapted_variationProcess_of_continuous` と片側版 |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.MonotoneProcess`

| 内容 | 宣言名 |
| --- | --- |
| 右連続な単調過程からの測度核 | `StieltjesFunction.kernelOfRightContAdaptedMono` |
| ベクトル測度の可測性 | `BoundedVariationOn.measurable_vectorMeasure_of_adapted` |
| ベクトル測度の可測性 | `BoundedVariationOn.measurable_vectorMeasure_of_stronglyAdapted` |

`variationProcess` は実数値で、拡張非負実数の変動を `toReal` に変換する。有限変動などの条件を外しても式は定義されるが、無限大の全変動を実数値としてそのまま表せるわけではない。

## 予測可能二次変分と共変分

局所二乗可積分マルチンゲール $M$ について、$\|M\|^2$ の Doob–Meyer 分解の予測可能部分を二次変分として選ぶ。これは予測可能ブラケット $\langle M\rangle$ に対応する。

| 数学 | Lean |
| --- | --- |
| 予測可能二次変分 $\langle M\rangle$ | `ProbabilityTheory.predQuadVariation M P 𝓕` |
| 予測可能二次共変分 $\langle M,N\rangle$ | `ProbabilityTheory.predQuadCovariation M N P 𝓕` |
| 二次変分の強予測可能性 | `ProbabilityTheory.isStronglyPredictable_predQuadVariation` |
| 二次変分の càdlàg 性 | `ProbabilityTheory.isCadlag_predQuadVariation` |
| 二次変分の単調性 | `ProbabilityTheory.monotone_predQuadVariation` |
| 二次共変分の強予測可能性・càdlàg 性 | `ProbabilityTheory.isStronglyPredictable_predQuadCovariation` |
| 二次共変分の強予測可能性・càdlàg 性 | `ProbabilityTheory.isCadlag_predQuadCovariation` |

モジュールは `BrownianMotion.StochasticIntegral.QuadraticVariation` である。共変分は

$$
\langle M,N\rangle
=\frac{\langle M+N\rangle-\langle M\rangle-\langle N\rangle}{2}
$$

で定義される。

`predQuadVariation` は、局所二乗可積分性と全経路の càdlàg 性が満たされない場合には零過程を返す。また、定義に使う局所 Doob–Meyer 定理は未証明であり、共変分の `hasLocallyIntegrableSup_predQuadCovariation` にも直接 `sorry` がある。分割に沿った増分の二乗和の極限としての二次変分 $[M]$ や、ブラウン運動の $[B]_t=t$ の定理が、この定義だけから提供されるわけではない。

## 予測可能過程の二乗可積分空間

`BrownianMotion.StochasticIntegral.L2M` の `ProbabilityTheory.L2Predictable` は、時間の測度 `μ` と標本空間の測度 `P` の積測度を、予測可能な可測構造に制限した $L^2$ 空間である。

```text
Lp E 2 ((μ.prod P).trim 𝓕.predictable_le_prod)
```

この版では一般の積測度による定義であり、マルチンゲールの二次変分を使う積分空間や Itô 等長性まで構成する宣言ではない。

## 一般の確率積分の特徴付け

`BrownianMotion.StochasticIntegral.StochasticIntegral` は、候補となる積分写像が満たす条件を命題として定義する。終端での積分を考え、入力を過程、出力を確率変数とする。

| 対象 | 宣言名 | 意味 |
| --- | --- | --- |
| 被積分過程の定義域 | `ProbabilityTheory.Domain` | 過程の集合 |
| 積分の候補 | `ProbabilityTheory.SIntegral` | 過程から確率変数への写像 |
| Riemann–Stieltjes 積分の拡張条件 | `ProbabilityTheory.IsRiemannStieltjesExtension` | 基本過程の積分、線形性、識別不能性、優収束など |
| 他の拡張との整合性を含む条件 | `ProbabilityTheory.IsStochasticIntegral` | 共通の定義域上で他の拡張とほとんど確実に一致 |

`IsRiemannStieltjesExtension` の優収束条件では、被積分過程の点ごとの収束と、定義域内の過程による支配を仮定し、積分値の測度収束を要求する。`IsStochasticIntegral` は定義域の最大性を要求しない。

両者は「与えられた写像が積分としての条件を満たす」という命題である。このファイルには、一般の半マルチンゲールに対して写像を構成して条件を証明する存在定理や、Itô の公式は含まれていない。

[一覧](README.md)
