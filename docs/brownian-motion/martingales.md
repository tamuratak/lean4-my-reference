# 停止時刻とマルチンゲール

停止時刻は、それまでに得られた情報だけで到達を判断できるランダムな時刻である。Brownian Motion は、停止時刻での値と停止過程、任意抽出、局所化、マルチンゲールの可積分性と分解を扱う。

## フィルトレーションと停止値

| 数学の対象 | Lean | 提供元 |
| --- | --- | --- |
| 情報の増大族 $(\mathcal{F}_t)$ | `MeasureTheory.Filtration ι mΩ` | mathlib |
| 停止時刻 $\tau$ | `τ : Ω → WithTop ι` | mathlib |
| 停止時刻 $\tau$ | `MeasureTheory.IsStoppingTime 𝓕 τ` | mathlib |
| 停止値 $X_\tau$ | `MeasureTheory.stoppedValue X τ` | mathlib |
| 停止過程 $X_{t\wedge\tau}$ | `MeasureTheory.stoppedProcess X τ` | mathlib |
| 時刻の取り直し | `MeasureTheory.Filtration.indexComap` | `BrownianMotion.Auxiliary.Filtration` |
| 停止値の追加性質 | `Filtration.stoppedValue'` など | `BrownianMotion.Auxiliary.StoppedValue` |
| 停止過程の追加性質 | `stoppedProcess` の補題 | `BrownianMotion.Auxiliary.StoppedProcess` |

`WithTop ι` は通常の時刻に無限大を加えた型である。有限停止時刻では通常の停止値に対応するが、無限大を取る場合は `stoppedValue` の規約や、極限を用いる `Filtration.stoppedValue'` の定義を区別する必要がある。

## Début と可測選択

時間と標本点の集合 $A\subseteq T\times\Omega$ に対し、début は指定した開始時刻以降で初めて $A$ に入る時刻の下限である。到達時刻が停止時刻になることを示す際、集合の射影の可測性が必要になる。

| 内容 | 宣言名 | モジュール |
| --- | --- | --- |
| 集合族を使った解析集合 | `MeasureTheory.IsPavingAnalytic` | `BrownianMotion.Choquet.AnalyticSet` |
| 集合族を使った解析集合 | `MeasureTheory.IsMeasurableAnalytic` | `BrownianMotion.Choquet.AnalyticSet` |
| 容量と容量可能性 | `MeasureTheory.Capacity` | `BrownianMotion.Choquet.Capacity` |
| 容量と容量可能性 | `MeasureTheory.IsCapacitable` | `BrownianMotion.Choquet.Capacity` |
| 解析集合の容量可能性 | `MeasureTheory.IsPavingAnalytic.isCapacitable` | `BrownianMotion.Choquet.Capacity` |
| 可測集合の射影の完備化に関する可測性 | `MeasurableSet.nullMeasurableSet_fst` | `BrownianMotion.Choquet.Capacity` |
| 可測な切断の存在 | `MeasurableSet.exists_measurable_section_left_nnreal` など | `BrownianMotion.Choquet.MeasurableSection` |
| début | `MeasureTheory.debut` | `BrownianMotion.Choquet.Debut` |
| 発展的可測な集合 | `MeasureTheory.ProgMeasurableSet` | `BrownianMotion.Choquet.Debut` |
| début の停止時刻性 | `MeasureTheory.isStoppingTime_debut` | `BrownianMotion.Choquet.Debut` |
| 到達時刻の停止時刻性 | `MeasureTheory.isStoppingTime_hittingAfter'` | `BrownianMotion.Choquet.Debut` |
| 到達時刻の停止時刻性 | `MeasureTheory.isStoppingTime_leastGE` | `BrownianMotion.Choquet.Debut` |
| 到達時刻の停止時刻性 | `MeasureTheory.isStoppingTime_leastGT` | `BrownianMotion.Choquet.Debut` |

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

| 内容 | 宣言名・モジュール |
| --- | --- |
| 離散近似列の構造 | `MeasureTheory.DiscreteApproxSequence`：`BrownianMotion.StochasticIntegral.ApproxSeq` |
| 停止時刻を近似できる条件 | `MeasureTheory.Approximable`：`BrownianMotion.StochasticIntegral.ApproxSeq` |
| 非負実数時間の近似列 | `MeasureTheory.nnrealApproxSeq`：`BrownianMotion.StochasticIntegral.ApproxSeq` |
| 任意抽出の追加定理 | `MeasureTheory.Martingale.stoppedValue_min_ae_eq_condExp'`：`BrownianMotion.StochasticIntegral.OptionalSampling` |
| 任意抽出の追加定理 | `MeasureTheory.Martingale.stoppedValue_ae_eq_condExp_of_le_const'`：`BrownianMotion.StochasticIntegral.OptionalSampling` |
| 停止過程のマルチンゲール性 | `MeasureTheory.Martingale.stoppedProcess`：`BrownianMotion.StochasticIntegral.OptionalSampling` |
| 劣マルチンゲールの任意抽出不等式 | `MeasureTheory.Submartingale.stoppedValue_min_ae_le_condExp`：`BrownianMotion.StochasticIntegral.OptionalSampling`、直接 `sorry` |

有界性や一様可積分性などの条件は定理ごとに異なる。停止時刻であれば無条件に期待値を保存する、という主張ではない。

## 局所化と局所マルチンゲール

局所化は、無限大に近づく停止時刻の列で過程を止め、各停止過程に性質を要求する方法である。

| 内容 | 宣言名・モジュール |
| --- | --- |
| 局所化、停止に対する安定性の基本概念 | `ProbabilityTheory.Locally`：mathlib 由来 |
| 局所化、停止に対する安定性の基本概念 | `ProbabilityTheory.IsStable`：mathlib 由来 |
| 局所化、停止に対する安定性の基本概念 | `ProbabilityTheory.IsLocalizingSequence`：mathlib 由来 |
| 連続性や càdlàg 性の局所化 | `ProbabilityTheory.locally_continuous_iff`：`BrownianMotion.StochasticIntegral.Locally` |
| 連続性や càdlàg 性の局所化 | `ProbabilityTheory.locally_isCadlag_iff`：`BrownianMotion.StochasticIntegral.Locally` |
| 単調な局所化列の選択 | `ProbabilityTheory.IsStable.exists_monotone_localSeq`：`BrownianMotion.StochasticIntegral.LocalizingSequence` |
| ノルムの到達時刻による停止 | `ProbabilityTheory.stoppedAtNorm`：`BrownianMotion.StochasticIntegral.LocalizingLeastGE` |
| 局所マルチンゲール | `ProbabilityTheory.IsLocalMartingale`：`BrownianMotion.StochasticIntegral.LocalMartingale` |
| 局所劣マルチンゲール | `ProbabilityTheory.IsLocalSubmartingale`：`BrownianMotion.StochasticIntegral.LocalMartingale` |
| 局所化の圏論的な構造 | `ProbabilityTheory.StableCat`：`BrownianMotion.StochasticIntegral.LocalMonad` |
| 局所化の圏論的な構造 | `ProbabilityTheory.Local`：`BrownianMotion.StochasticIntegral.LocalMonad` |
| 局所化の圏論的な構造 | `ProbabilityTheory.StableMonad`：`BrownianMotion.StochasticIntegral.LocalMonad` |

このライブラリの `IsLocalMartingale` は、マルチンゲール性と全経路の càdlàg 性を併せた性質の局所化として定義される。`isStable_submartingale` には直接 `sorry` がある。

## 一様可積分性、class D、class DL

class D は有限停止時刻での値全体に一様可積分性を要求し、class DL は各有界時間範囲で同様の条件を要求する。対象版の定義には強発展的可測性も含まれる。

| 内容 | 宣言名・モジュール |
| --- | --- |
| 一様可積分性の裾評価による特徴付け | `MeasureTheory.uniformIntegrable_iff_tendsto_nnReal_iSup_setIntegral_norm`：`BrownianMotion.StochasticIntegral.UniformIntegrable` |
| 条件付き期待値を取った族の一様可積分性 | `MeasureTheory.UniformIntegrable.condExp`：`BrownianMotion.StochasticIntegral.UniformIntegrable` |
| class D・DL | `ProbabilityTheory.ClassD`：`BrownianMotion.StochasticIntegral.ClassD` |
| class D・DL | `ProbabilityTheory.ClassDL`：`BrownianMotion.StochasticIntegral.ClassD` |
| 時間区間ごとの上限の可積分性 | `ProbabilityTheory.HasIntegrableSup`：`BrownianMotion.StochasticIntegral.ClassD` |
| 時間区間ごとの上限の可積分性 | `ProbabilityTheory.HasLocallyIntegrableSup`：`BrownianMotion.StochasticIntegral.ClassD` |
| マルチンゲールの極限過程への収束 | `MeasureTheory.Martingale.ae_tendsto_limitProcess`：`BrownianMotion.StochasticIntegral.UniformIntegrable`、直接 `sorry` |
| 極限の条件付き期待値による過程の復元 | `MeasureTheory.Martingale.condExp_limitProcess_ae_eq`、同名末尾 `'` の版：`BrownianMotion.StochasticIntegral.UniformIntegrable`、直接 `sorry` |
| 最大不等式 | `ProbabilityTheory.maximal_ineq`：`BrownianMotion.StochasticIntegral.DoobLp` |
| 最大不等式 | `ProbabilityTheory.maximal_ineq_norm`：`BrownianMotion.StochasticIntegral.DoobLp` |
| Doob の $L^p$ 評価 | `ProbabilityTheory.integral_iSup_le_norm_rpow_le`：`BrownianMotion.StochasticIntegral.DoobLp`、直接 `sorry` |
| Doob の $L^p$ 評価 | `ProbabilityTheory.integral_iSup_norm_rpow_le`：`BrownianMotion.StochasticIntegral.DoobLp`、直接 `sorry` |

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

| 内容 | 宣言名・モジュール |
| --- | --- |
| 二乗可積分性、識別不能な代表による二乗可積分性 | `ProbabilityTheory.IsSquareIntegrable`：`BrownianMotion.StochasticIntegral.SquareIntegrable` |
| 二乗可積分性、識別不能な代表による二乗可積分性 | `ProbabilityTheory.IsAESquareIntegrable`：`BrownianMotion.StochasticIntegral.SquareIntegrable` |
| 識別不能性で同一視した空間 | `ProbabilityTheory.SquareIntegrable`：`BrownianMotion.StochasticIntegral.SquareIntegrable` |
| 終端極限を使う $L^2$ 空間への写像 | `ProbabilityTheory.SquareIntegrable.toL2`：`BrownianMotion.StochasticIntegral.SquareIntegrable` |
| 終端極限を使う $L^2$ 空間への写像 | `ProbabilityTheory.SquareIntegrable.toL2Isom`：`BrownianMotion.StochasticIntegral.SquareIntegrable` |
| 局所二乗可積分性 | `ProbabilityTheory.IsLocallySquareIntegrable`：`BrownianMotion.StochasticIntegral.SquareIntegrable` |
| 純不連続性 | `ProbabilityTheory.IsPurelyDiscontinuous`：`BrownianMotion.StochasticIntegral.SquareIntegrable` |
| 連続マルチンゲールの部分空間 | `ProbabilityTheory.continuousSquareIntegrable`：`BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable` |
| 連続部分と純不連続部分 | `ProbabilityTheory.continuousPart`：`BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable` |
| 連続部分と純不連続部分 | `ProbabilityTheory.discontinuousPart`：`BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable` |
| 分解の等式 | `ProbabilityTheory.continuousPart_add_discontinuousPart`：`BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable` |

純不連続性は、二乗可積分性と、すべての連続な二乗可積分マルチンゲールとの終端極限の $L^2$ 内積が零であることによって定義される。「すべての経路が不連続」という意味ではない。連続部分は Hilbert 空間での直交射影を使って得られる。

極限の $L^2$ 収束、極限ノルムの等式、修正からの識別不能性、停止に対する安定性などの補題に直接 `sorry` があるため、空間の構造や分解の結果も未証明部分への依存に注意が必要である。

[一覧](README.md)
