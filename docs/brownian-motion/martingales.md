# 停止時刻とマルチンゲール

停止時刻は、それまでに得られた情報だけで到達を判断できるランダムな時刻である。Brownian Motion は、停止時刻での値と停止過程、任意抽出、局所化、マルチンゲールの可積分性と分解を扱う。

## フィルトレーションと停止値

#### 提供モジュール：mathlib

| 数学の対象 | Lean |
| --- | --- |
| 情報の増大族 $(\mathcal{F}_t)$ | `MeasureTheory.Filtration ι mΩ` |
| 停止時刻 $\tau$ | `τ : Ω → WithTop ι` |
| 停止時刻 $\tau$ | `MeasureTheory.IsStoppingTime 𝓕 τ` |
| 停止値 $X_\tau$ | `MeasureTheory.stoppedValue X τ` |
| 停止過程 $X_{t\wedge\tau}$ | `MeasureTheory.stoppedProcess X τ` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Filtration`

| 数学の対象 | Lean |
| --- | --- |
| 時刻の取り直し | `MeasureTheory.Filtration.indexComap` |

#### 提供モジュール：`BrownianMotion.Auxiliary.StoppedValue`

| 数学の対象 | Lean |
| --- | --- |
| 停止値の追加性質 | `Filtration.stoppedValue'` など |

#### 提供モジュール：`BrownianMotion.Auxiliary.StoppedProcess`

| 数学の対象 | Lean |
| --- | --- |
| 停止過程の追加性質 | `stoppedProcess` の補題 |

`WithTop ι` は通常の時刻に無限大を加えた型である。有限停止時刻では通常の停止値に対応するが、無限大を取る場合は `stoppedValue` の規約や、極限を用いる `Filtration.stoppedValue'` の定義を区別する必要がある。

## Début と可測選択

時間と標本点の集合 $A\subseteq T\times\Omega$ に対し、début は指定した開始時刻以降で初めて $A$ に入る時刻の下限である。到達時刻が停止時刻になることを示す際、集合の射影の可測性が必要になる。

#### 提供モジュール：`BrownianMotion.Choquet.AnalyticSet`

| 内容 | 宣言名 |
| --- | --- |
| 集合族を使った解析集合 | `MeasureTheory.IsPavingAnalytic` |
| 集合族を使った解析集合 | `MeasureTheory.IsMeasurableAnalytic` |

#### 提供モジュール：`BrownianMotion.Choquet.Capacity`

| 内容 | 宣言名 |
| --- | --- |
| 容量と容量可能性 | `MeasureTheory.Capacity` |
| 容量と容量可能性 | `MeasureTheory.IsCapacitable` |
| 解析集合の容量可能性 | `MeasureTheory.IsPavingAnalytic.isCapacitable` |
| 可測集合の射影の完備化に関する可測性 | `MeasurableSet.nullMeasurableSet_fst` |

#### 提供モジュール：`BrownianMotion.Choquet.MeasurableSection`

| 内容 | 宣言名 |
| --- | --- |
| 可測な切断の存在 | `MeasurableSet.exists_measurable_section_left_nnreal` など |

#### 提供モジュール：`BrownianMotion.Choquet.Debut`

| 内容 | 宣言名 |
| --- | --- |
| début | `MeasureTheory.debut` |
| 発展的可測な集合 | `MeasureTheory.ProgMeasurableSet` |
| début の停止時刻性 | `MeasureTheory.isStoppingTime_debut` |
| 到達時刻の停止時刻性 | `MeasureTheory.isStoppingTime_hittingAfter'` |
| 到達時刻の停止時刻性 | `MeasureTheory.isStoppingTime_leastGE` |
| 到達時刻の停止時刻性 | `MeasureTheory.isStoppingTime_leastGT` |

début の停止時刻性には、時間空間の位相条件、フィルトレーションの右連続性・測度に関する完備性などの仮定がある。`Choquet.CompactSystem` のコンパクト系に関する補題には直接 `sorry` があり、Choquet 理論を使う定理の証明依存にも注意が必要である。

## 予測可能な時刻と確率区間

確率区間は、端点をランダムな時刻に置き換えた時間と標本点の集合である。

| 数学 | Lean | 意味 |
| --- | --- | --- |
| $[\sigma,\tau]$ | `ProbabilityTheory.stochIcc σ τ` | 両端を含む |
| $[\sigma,\tau)$ | `ProbabilityTheory.stochIco σ τ` | 右端を除く |
| $(\sigma,\tau]$ | `ProbabilityTheory.stochIoc σ τ` | 左端を除く |
| $(\sigma,\tau)$ | `ProbabilityTheory.stochIoo σ τ` | 両端を除く |
| $\{(t,\omega):t=\sigma(\omega)\}$ | `ProbabilityTheory.stochGraph σ` | ランダム時刻のグラフ |

定義元は `BrownianMotion.StochasticIntegral.StochasticInterval` である。自然数時間では、上側の停止時刻が有界なら、`stochIoc.exists_elementaryPredictableSet` によって確率区間を有限個の基本予測可能集合で表せる。

`BrownianMotion.StochasticIntegral.PredictableTime` は次の概念を提供する。

| 概念・結果 | 宣言名 |
| --- | --- |
| 停止時刻の直前の情報 | `MeasureTheory.leftMeasurableSpace` |
| 予測可能な時刻 | `MeasureTheory.IsPredictableTime` |
| 予測可能な時刻の停止時刻性 | `MeasureTheory.IsPredictableTime.isStoppingTime` |
| 可算個の予測可能時刻で覆われる時刻 | `MeasureTheory.IsAccessibleTime` |
| 予測可能時刻と有限時刻で一致する確率が零の時刻 | `MeasureTheory.IsInacessibleTime` |
| 到達可能部分と非到達可能部分への分割 | `MeasureTheory.IsStoppingTime.decompositon` |

`IsInacessibleTime` と `decompositon` は対象版の宣言名の綴りである。`IsPredictableTime` の実際の定義は、確率区間 $[\tau,\infty)$ の予測可能性を使う。

## 任意抽出と停止時刻の近似

任意抽出定理は、停止時刻 $\sigma\le\tau$ に対して、適切な仮定の下で $\mathbb{E}[X_\tau\mid\mathcal{F}_\sigma]=X_\sigma$ を与える。連続時間では、停止時刻を可算値の停止時刻で近似し、可積分性と右連続性を使って極限へ移る。

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ApproxSeq`

| 内容 | 宣言名 |
| --- | --- |
| 離散近似列の構造 | `MeasureTheory.DiscreteApproxSequence` |
| 停止時刻を近似できる条件 | `MeasureTheory.Approximable` |
| 非負実数時間の近似列 | `MeasureTheory.nnrealApproxSeq` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.OptionalSampling`

| 内容 | 宣言名 |
| --- | --- |
| 任意抽出の追加定理 | `MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp'` |
| 任意抽出の追加定理 | `MeasureTheory.Martingale.stoppedValue_ae_eq_condExp_of_le_const'` |
| 停止過程のマルチンゲール性 | `MeasureTheory.Martingale.stoppedProcess` |
| 劣マルチンゲールの任意抽出不等式 | `MeasureTheory.Submartingale.stoppedValue_min_ae_le_condExp`、直接 `sorry` |

有界性や一様可積分性などの条件は定理ごとに異なる。停止時刻であれば無条件に期待値を保存する、という主張ではない。

## 局所化と局所マルチンゲール

局所化は、無限大に近づく停止時刻の列で過程を止め、各停止過程に性質を要求する方法である。

#### 提供モジュール：mathlib

| 内容 | 宣言名 |
| --- | --- |
| 局所化、停止に対する安定性の基本概念 | `ProbabilityTheory.Locally` |
| 局所化、停止に対する安定性の基本概念 | `ProbabilityTheory.IsStable` |
| 局所化、停止に対する安定性の基本概念 | `ProbabilityTheory.IsLocalizingSequence` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Locally`

| 内容 | 宣言名 |
| --- | --- |
| 連続性や càdlàg 性の局所化 | `ProbabilityTheory.locally_continuous_iff` |
| 連続性や càdlàg 性の局所化 | `ProbabilityTheory.locally_isCadlag_iff` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalizingSequence`

| 内容 | 宣言名 |
| --- | --- |
| 単調な局所化列の選択 | `ProbabilityTheory.IsStable.exists_monotone_localSeq` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalizingLeastGE`

| 内容 | 宣言名 |
| --- | --- |
| ノルムの到達時刻による停止 | `ProbabilityTheory.stoppedAtNorm` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalMartingale`

| 内容 | 宣言名 |
| --- | --- |
| 局所マルチンゲール | `ProbabilityTheory.IsLocalMartingale` |
| 局所劣マルチンゲール | `ProbabilityTheory.IsLocalSubmartingale` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalMonad`

| 内容 | 宣言名 |
| --- | --- |
| 局所化の圏論的な構造 | `ProbabilityTheory.StableCat` |
| 局所化の圏論的な構造 | `ProbabilityTheory.Local` |
| 局所化の圏論的な構造 | `ProbabilityTheory.StableMonad` |

このライブラリの `IsLocalMartingale` は、マルチンゲール性と全経路の càdlàg 性を併せた性質の局所化として定義される。`isStable_submartingale` には直接 `sorry` がある。

## 一様可積分性、class D、class DL

class D は有限停止時刻での値全体に一様可積分性を要求し、class DL は各有界時間範囲で同様の条件を要求する。対象版の定義には強発展的可測性も含まれる。

#### 提供モジュール：`BrownianMotion.StochasticIntegral.UniformIntegrable`

| 内容 | 宣言名 |
| --- | --- |
| 一様可積分性の裾評価による特徴付け | `MeasureTheory.uniformIntegrable_iff_tendsto_nnReal_iSup_setIntegral_norm` |
| 条件付き期待値を取った族の一様可積分性 | `MeasureTheory.UniformIntegrable.condExp` |
| マルチンゲールの極限過程への収束 | `MeasureTheory.Martingale.ae_tendsto_limitProcess`、直接 `sorry` |
| 極限の条件付き期待値による過程の復元 | `MeasureTheory.Martingale.condExp_limitProcess_ae_eq`、同名末尾 `'` の版、直接 `sorry` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ClassD`

| 内容 | 宣言名 |
| --- | --- |
| class D・DL | `ProbabilityTheory.ClassD` |
| class D・DL | `ProbabilityTheory.ClassDL` |
| 時間区間ごとの上限の可積分性 | `ProbabilityTheory.HasIntegrableSup` |
| 時間区間ごとの上限の可積分性 | `ProbabilityTheory.HasLocallyIntegrableSup` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.DoobLp`

| 内容 | 宣言名 |
| --- | --- |
| 最大不等式 | `ProbabilityTheory.maximal_ineq` |
| 最大不等式 | `ProbabilityTheory.maximal_ineq_norm` |
| Doob の $L^p$ 評価 | `ProbabilityTheory.integral_iSup_le_norm_rpow_le`、直接 `sorry` |
| Doob の $L^p$ 評価 | `ProbabilityTheory.integral_iSup_norm_rpow_le`、直接 `sorry` |

一様可積分性のファイルでも、劣マルチンゲールの停止値に関する `Submartingale.uniformIntegrable_stoppedValue` は未証明である。class D の補助理論にも、定数過程の上限に関する未証明補題がある。

## Doob–Meyer 分解

Doob–Meyer 分解は、適切な劣マルチンゲール $S$ を、マルチンゲール $M$ と予測可能な増加過程 $A$ の和 $S=M+A$ に表す。

| 適用対象 | 宣言名 | 得られる性質 |
| --- | --- | --- |
| 最大時刻を持つ時間領域上の class D | `ProbabilityTheory.ClassD.doob_meyer` | $M$ はマルチンゲール、$A$ は予測可能・増加・càdlàg、初期値零 |
| 有限区間ごとの class DL | `ProbabilityTheory.ClassDL.exists_doob_meyer_increment` | 切り詰めた時間区間の増分の分解 |
| 最大時刻を要求しない class DL | `ProbabilityTheory.ClassDL.doob_meyer` | 全時間領域上の分解、$A$ の初期値零 |
| 局所劣マルチンゲール | `ProbabilityTheory.IsLocalSubmartingale.doob_meyer` | 局所マルチンゲールと予測可能な増加過程への分解、直接 `sorry` |

class D 版は `BrownianMotion.StochasticIntegral.DoobMeyer`、class DL 版は `BrownianMotion.StochasticIntegral.DoobMeyerClassDL` にある。class D・DL 版は、有限測度、時間領域の順序・位相条件、フィルトレーションの右連続性と完備性、各経路の càdlàg 性などを仮定する。

class D・DL 版には証明コードがあるが、Choquet 理論や Komlós 型の収束など、基盤となる補題に未証明部分が残る。局所版から選択される `martingalePart`・`predictablePart` と、その性質を述べる定理は、未証明の局所版に依存する。

## 二乗可積分マルチンゲールと直交分解

`ProbabilityTheory.IsSquareIntegrable X 𝓕 P` は、マルチンゲール性、全経路の càdlàg 性、全時刻にわたる $L^2$ ノルムの一様有界性を要求する。

$$
\sup_t\|X_t\|_{L^2(P)}<\infty.
$$

各固定時刻で二乗可積分であることだけより強い条件である。

#### 提供モジュール：`BrownianMotion.StochasticIntegral.SquareIntegrable`

| 内容 | 宣言名 |
| --- | --- |
| 全経路の càdlàg 性を含む二乗可積分マルチンゲール性 | `ProbabilityTheory.IsSquareIntegrable` |
| 二乗可積分マルチンゲールと識別不能であること | `ProbabilityTheory.IsAESquareIntegrable` |
| 識別不能性で同一視した空間 | `ProbabilityTheory.SquareIntegrable` |
| 終端極限を使う $L^2$ 空間への写像 | `ProbabilityTheory.SquareIntegrable.toL2` |
| 終端極限を使う $L^2$ 空間への写像 | `ProbabilityTheory.SquareIntegrable.toL2Isom` |
| 局所二乗可積分性 | `ProbabilityTheory.IsLocallySquareIntegrable` |
| 純不連続性 | `ProbabilityTheory.IsPurelyDiscontinuous` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable`

| 内容 | 宣言名 |
| --- | --- |
| 連続マルチンゲールの部分空間 | `ProbabilityTheory.continuousSquareIntegrable` |
| 連続部分と純不連続部分 | `ProbabilityTheory.continuousPart` |
| 連続部分と純不連続部分 | `ProbabilityTheory.discontinuousPart` |
| 分解の等式 | `ProbabilityTheory.continuousPart_add_discontinuousPart` |

`IsPurelyDiscontinuous X 𝓕 P` は、`IsAESquareIntegrable X 𝓕 P` と直交性を要求する。`IsAESquareIntegrable` は、`IsSquareIntegrable` を満たす過程と識別不能であることを表し、`X` 自身の全経路の càdlàg 性を要求しない。直交性は、`IsAESquareIntegrable Y 𝓕 P` を満たし、ほとんど確実に連続な経路を持つすべての過程 `Y` に対し、`X` と `Y` の終端極限の $L^2$ 内積が零であるという条件である。

純不連続性は「すべての経路が不連続」という意味ではない。連続部分は Hilbert 空間での直交射影を使って得られる。

極限の $L^2$ 収束、極限ノルムの等式、修正からの識別不能性、停止に対する安定性などの補題に直接 `sorry` があるため、空間の構造や分解の結果も未証明部分への依存に注意が必要である。

[一覧](README.md)
