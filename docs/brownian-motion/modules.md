# モジュール一覧

Brownian Motion のモジュールは、ガウス過程、連続な修正、可測選択、マルチンゲール・確率積分、共通補題に分かれる。

`BrownianMotion` は `BrownianMotion/` 配下のモジュールをまとめて公開する入口である。

## ガウス過程とブラウン運動

#### 提供モジュール：`BrownianMotion.Gaussian.BrownianMotion`

| 内容 | 宣言名の例 |
| --- | --- |
| ブラウン運動・Wiener 測度の構成 | `brownian` |
| ブラウン運動・Wiener 測度の構成 | `isBrownianReal_brownian` |
| ブラウン運動・Wiener 測度の構成 | `wienerMeasure` |

#### 提供モジュール：`BrownianMotion.Gaussian.CovMatrix`

| 内容 | 宣言名の例 |
| --- | --- |
| 共分散行列と半正定値性 | `covMatrix` |

#### 提供モジュール：`BrownianMotion.Gaussian.Gaussian`

| 内容 | 宣言名の例 |
| --- | --- |
| ガウス法則の特性関数 | `HasGaussianLaw.charFun_map_real` |

#### 提供モジュール：`BrownianMotion.Gaussian.GaussianProcess`

| 内容 | 宣言名の例 |
| --- | --- |
| ガウス過程の族の独立性 | `IsGaussianProcess.indepFun''` |
| ガウス過程の族の独立性 | `IsGaussianProcess.iIndepFun''` |

#### 提供モジュール：`BrownianMotion.Gaussian.IteratedLogarithm`

| 内容 | 宣言名の例 |
| --- | --- |
| 反射原理・裾評価・重複対数の法則。直接の `sorry` あり | `IsBrownianReal.reflection` |
| 反射原理・裾評価・重複対数の法則。直接の `sorry` あり | `IsStandardGaussian.tail` |

#### 提供モジュール：`BrownianMotion.Gaussian.Moment`

| 内容 | 宣言名の例 |
| --- | --- |
| 偶数次中心モーメント | `centralMoment_two_mul_gaussianReal` |
| 偶数次中心モーメント | `centralMoment_fun_two_mul_gaussianReal` |

#### 提供モジュール：`BrownianMotion.Gaussian.MultivariateGaussian`

| 内容 | 宣言名の例 |
| --- | --- |
| 多変量ガウスの成分分布と共分散 | `covMatrix_stdGaussian` |
| 多変量ガウスの成分分布と共分散 | `inner_toEuclideanCLM` |

#### 提供モジュール：`BrownianMotion.Gaussian.ProjectiveLimit`

| 内容 | 宣言名の例 |
| --- | --- |
| ガウス有限次元分布と射影極限 | `brownianCovMatrix` |
| ガウス有限次元分布と射影極限 | `gaussianProjectiveFamily` |
| ガウス有限次元分布と射影極限 | `gaussianLimit` |

#### 提供モジュール：`BrownianMotion.Gaussian.StochasticProcesses`

| 内容 | 宣言名の例 |
| --- | --- |
| 修正と識別不能性 | `modification_of_indistinguishable` |
| 修正と識別不能性 | `indistinguishable_of_modification` |

## 経路の連続性

#### 提供モジュール：`BrownianMotion.Continuity.Chaining`

| 内容 | 宣言名の例 |
| --- | --- |
| 有限被覆をつなぐ chaining と距離評価 | `nearestPt` |
| 有限被覆をつなぐ chaining と距離評価 | `chainingSequenceReverse` |
| 有限被覆をつなぐ chaining と距離評価 | `chainingSequence` |

#### 提供モジュール：`BrownianMotion.Continuity.CoveringNumber`

| 内容 | 宣言名の例 |
| --- | --- |
| 被覆数・充填数と体積の評価 | `TotallyBounded.coveringNumber_ne_top` |
| 被覆数・充填数と体積の評価 | `coveringNumber_Icc_zero_one_le_one_div` |

#### 提供モジュール：`BrownianMotion.Continuity.HasBoundedInternalCoveringNumber`

| 内容 | 宣言名の例 |
| --- | --- |
| 被覆数のべき上界と開被覆 | `HasBoundedCoveringNumber` |
| 被覆数のべき上界と開被覆 | `IsCoverWithBoundedCoveringNumber` |

#### 提供モジュール：`BrownianMotion.Continuity.IsKolmogorovProcess`

| 内容 | 宣言名の例 |
| --- | --- |
| 増分条件からの有限集合上の評価 | `finite_set_bound_of_edist_le` |

#### 提供モジュール：`BrownianMotion.Continuity.KolmogorovChentsov`

| 内容 | 宣言名の例 |
| --- | --- |
| Hölder 連続な修正の存在 | `holderModification` |
| Hölder 連続な修正の存在 | `exists_modification_holder` |
| Hölder 連続な修正の存在 | `exists_modification_holder_iSup` |

#### 提供モジュール：`BrownianMotion.Continuity.KolmogorovChentsovInequality`

| 内容 | 宣言名の例 |
| --- | --- |
| Kolmogorov–Chentsov 不等式 | `finite_kolmogorov_chentsov` |
| Kolmogorov–Chentsov 不等式 | `countable_kolmogorov_chentsov` |

#### 提供モジュール：`BrownianMotion.Continuity.LimitModification`

| 内容 | 宣言名の例 |
| --- | --- |
| 極限・指示過程による可測な修正 | `indicatorProcess` |
| 極限・指示過程による可測な修正 | `IsLimitOfIndicator` |

## 可測選択と到達時刻

#### 提供モジュール：`BrownianMotion.Choquet.AnalyticSet`

| 内容 | 宣言名の例 |
| --- | --- |
| 集合族による解析集合と射影 | `IsPavingAnalyticFor` |
| 集合族による解析集合と射影 | `IsPavingAnalytic` |
| 集合族による解析集合と射影 | `IsMeasurableAnalyticFor` |

#### 提供モジュール：`BrownianMotion.Choquet.Capacity`

| 内容 | 宣言名の例 |
| --- | --- |
| 容量可能性と射影の可測性 | `Capacity` |
| 容量可能性と射影の可測性 | `Measure.capacity` |
| 容量可能性と射影の可測性 | `Capacity.comp_fst` |

#### 提供モジュール：`BrownianMotion.Choquet.CompactSystem`

| 内容 | 宣言名の例 |
| --- | --- |
| コンパクト系と集合族の閉包。直接の `sorry` あり | `prodSigmaDelta` |

#### 提供モジュール：`BrownianMotion.Choquet.Debut`

| 内容 | 宣言名の例 |
| --- | --- |
| début と到達時刻の停止時刻性 | `debut` |
| début と到達時刻の停止時刻性 | `ProgMeasurableSet` |
| début と到達時刻の停止時刻性 | `leastGT` |

#### 提供モジュール：`BrownianMotion.Choquet.MeasurableSection`

| 内容 | 宣言名の例 |
| --- | --- |
| 可測切断の存在 | `MeasurableSet.exists_measurable_section_left_nnreal` |

## マルチンゲールと確率積分

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ApproxSeq`

| 内容 | 宣言名の例 |
| --- | --- |
| 停止時刻の離散近似と停止値の収束 | `DiscreteApproxSequence` |
| 停止時刻の離散近似と停止値の収束 | `Approximable` |
| 停止時刻の離散近似と停止値の収束 | `IsStoppingTime.discreteApproxSequence` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Cadlag`

| 内容 | 宣言名の例 |
| --- | --- |
| 右連続性・左極限・有界性 | `IsRightContinuous` |
| 右連続性・左極限・有界性 | `IsCadlag` |
| 右連続性・左極限・有界性 | `leftJumpSet` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ClassD`

| 内容 | 宣言名の例 |
| --- | --- |
| class D・DL と上限の可積分性。直接の `sorry` あり | `ClassD` |
| class D・DL と上限の可積分性。直接の `sorry` あり | `ClassDL` |
| class D・DL と上限の可積分性。直接の `sorry` あり | `HasLocallyIntegrableSup` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable`

| 内容 | 宣言名の例 |
| --- | --- |
| 連続部分と純不連続部分への直交分解 | `continuousSquareIntegrable` |
| 連続部分と純不連続部分への直交分解 | `continuousPart` |
| 連続部分と純不連続部分への直交分解 | `discontinuousPart` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ConvexWeights`

| 内容 | 宣言名の例 |
| --- | --- |
| 凸結合の反復とノルム評価 | `Convexity.iteratedComb` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.DoobLp`

| 内容 | 宣言名の例 |
| --- | --- |
| 最大不等式と Doob の Lp 評価。直接の `sorry` あり | `maximal_ineq'` |
| 最大不等式と Doob の Lp 評価。直接の `sorry` あり | `maximal_ineq_finset` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.DoobMeyer`

| 内容 | 宣言名の例 |
| --- | --- |
| class D の分解（`ClassD` 名前空間） | `ClassD.doob_meyer` |
| 局所版の分解（`IsLocalSubmartingale` 名前空間）。直接の `sorry` あり | `IsLocalSubmartingale.doob_meyer` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.DoobMeyerClassDL`

| 内容 | 宣言名の例 |
| --- | --- |
| class DL の分解 | `ClassDL.exists_doob_meyer_increment` |
| class DL の分解 | `ClassDL.doob_meyer` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Jump`

| 内容 | 宣言名の例 |
| --- | --- |
| 左極限との差としてのジャンプ | `Function.jump` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Komlos`

| 内容 | 宣言名の例 |
| --- | --- |
| 凸結合による Komlós 型収束。直接の `sorry` あり | `convexTail` |
| 凸結合による Komlós 型収束。直接の `sorry` あり | `komlosFormula` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.L2M`

| 内容 | 宣言名の例 |
| --- | --- |
| 積測度に関する予測可能過程の L2 空間 | `L2Predictable` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalMartingale`

| 内容 | 宣言名の例 |
| --- | --- |
| 局所マルチンゲール・局所劣マルチンゲール。直接の `sorry` あり | `IsLocalMartingale` |
| 局所マルチンゲール・局所劣マルチンゲール。直接の `sorry` あり | `IsLocalSubmartingale` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalMonad`

| 内容 | 宣言名の例 |
| --- | --- |
| 局所化の圏・関手・モナド | `StableCat` |
| 局所化の圏・関手・モナド | `Local` |
| 局所化の圏・関手・モナド | `LocalFunctor` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalizingLeastGE`

| 内容 | 宣言名の例 |
| --- | --- |
| ノルムの到達時刻による局所化 | `stoppedAtNorm` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalizingSequence`

| 内容 | 宣言名の例 |
| --- | --- |
| 局所化列の合成・単調化・帰納法 | `LocalizingSequenceOfProp` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Locally`

| 内容 | 宣言名の例 |
| --- | --- |
| 経路の正則性や適合性の局所化 | `locally_and_of_isStable` |
| 経路の正則性や適合性の局所化 | `locally_of_ae` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.MathlibImports`

| 内容 | 宣言名の例 |
| --- | --- |
| mathlib の確率過程モジュールの集約 | import・記法の設定 |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.MonotoneProcess`

| 内容 | 宣言名の例 |
| --- | --- |
| 単調過程の Stieltjes 測度核・ベクトル測度 | `StieltjesFunction.restrict` |
| 単調過程の Stieltjes 測度核・ベクトル測度 | `StieltjesFunction.rightContMono` |
| 単調過程の Stieltjes 測度核・ベクトル測度 | `StieltjesFunction.kernel` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.OptionalSampling`

| 内容 | 宣言名の例 |
| --- | --- |
| 任意抽出と停止過程。直接の `sorry` あり | `Martingale.condExp_stoppedValue_stopping_time_ae_eq_restrict_le_of_countable_range` |
| 任意抽出と停止過程。直接の `sorry` あり | `Martingale.stoppedValue_min_ae_eq_condExp_of_countable_range` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Predictable`

| 内容 | 宣言名の例 |
| --- | --- |
| 強予測可能性と生成集合 | `Filtration.IsComplete` |
| 強予測可能性と生成集合 | `Filtration.predictableRectangles` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.PredictableTime`

| 内容 | 宣言名の例 |
| --- | --- |
| 予測可能・到達可能・非到達可能な時刻 | `leftMeasurableSpace` |
| 予測可能・到達可能・非到達可能な時刻 | `IsPredictableTime` |
| 予測可能・到達可能・非到達可能な時刻 | `IsAccessibleTime` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.QuadraticVariation`

| 内容 | 宣言名の例 |
| --- | --- |
| 予測可能二次変分と二次共変分。直接の `sorry` あり | `predQuadVariation` |
| 予測可能二次変分と二次共変分。直接の `sorry` あり | `predQuadCovariation` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.Basic`

| 内容 | 宣言名の例 |
| --- | --- |
| 実数値準マルチンゲール | `IsRealQuasimartingale` |
| 実数値準マルチンゲール | `variationBound` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModification`

| 内容 | 宣言名の例 |
| --- | --- |
| 実数値準マルチンゲールの正則化 | `rightContModifReal` |
| 実数値準マルチンゲールの正則化 | `cadlagModifReal` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModificationBanach`

| 内容 | 宣言名の例 |
| --- | --- |
| Banach 空間値マルチンゲールの正則化 | `rightContModif` |
| Banach 空間値マルチンゲールの正則化 | `cadlagModif` |
| Banach 空間値マルチンゲールの正則化 | `Martingale.martingale_cadlagModif` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.MaximalInequality`

| 内容 | 宣言名の例 |
| --- | --- |
| 交差回数と最大不等式 | `finIdx` |
| 交差回数と最大不等式 | `elemPredSetOfSeq` |
| 交差回数と最大不等式 | `upcrossingWithinPredSet` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.SimpleProcess`

| 内容 | 宣言名の例 |
| --- | --- |
| 単純過程と有限和の積分 | `ElementaryPredictableSet` |
| 単純過程と有限和の積分 | `SimpleProcess` |
| 単純過程と有限和の積分 | `SimpleProcess.integral` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.SquareIntegrable`

| 内容 | 宣言名の例 |
| --- | --- |
| 二乗可積分マルチンゲールの空間。直接の `sorry` あり | `IsSquareIntegrable` |
| 二乗可積分マルチンゲールの空間。直接の `sorry` あり | `IsAESquareIntegrable` |
| 二乗可積分マルチンゲールの空間。直接の `sorry` あり | `IsAESquareIntegrable.toContinuous` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.StochasticIntegral`

| 内容 | 宣言名の例 |
| --- | --- |
| 一般の確率積分の公理的特徴付け | `IsRiemannStieltjesExtension` |
| 一般の確率積分の公理的特徴付け | `IsStochasticIntegral` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.StochasticInterval`

| 内容 | 宣言名の例 |
| --- | --- |
| 確率区間と時刻のグラフ | `stochIcc` |
| 確率区間と時刻のグラフ | `stochIco` |
| 確率区間と時刻のグラフ | `stochIoc` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.UniformIntegrable`

| 内容 | 宣言名の例 |
| --- | --- |
| 一様可積分性と極限過程。直接の `sorry` あり | `uniformIntegrable_iff'` |
| 一様可積分性と極限過程。直接の `sorry` あり | `uniformIntegrable_iff_tendsto_iSup_eLpNorm_indicator_norm` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.VariationProcess`

| 内容 | 宣言名の例 |
| --- | --- |
| 全変動の可測性・適合性 | `variationProcess` |

## 共通の補助理論

#### 提供モジュール：`BrownianMotion.Auxiliary.AEEq`

| 内容 | 宣言名の例 |
| --- | --- |
| 強適合過程の識別不能性による商 | `Measure.aeEqSetoid'` |
| 強適合過程の識別不能性による商 | `AEEqProcess` |
| 強適合過程の識別不能性による商 | `AEStronglyAdapted.mk` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Adapted`

| 内容 | 宣言名の例 |
| --- | --- |
| 強適合性と強発展的可測性 | `SimpleFunc.IndexedPartition` |
| 強適合性と強発展的可測性 | `AEStronglyAdapted` |
| 強適合性と強発展的可測性 | `AEStronglyAdapted.mk` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Algebra`

| 内容 | 宣言名の例 |
| --- | --- |
| 代数演算の補題 | `Set.indicator_apply_apply` |
| 代数演算の補題 | `Monotone.finset_sum` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Analysis`

| 内容 | 宣言名の例 |
| --- | --- |
| 解析の補助評価 | `convexOn_subsingleton` |
| 解析の補助評価 | `convexOn_rpow_norm` |

#### 提供モジュール：`BrownianMotion.Auxiliary.ContinuousBilinForm`

| 内容 | 宣言名の例 |
| --- | --- |
| 連続双線形形式 | `ContinuousBilinForm` |
| 連続双線形形式 | `ContinuousBilinForm.toBilinForm` |
| 連続双線形形式 | `ContinuousBilinForm.IsSymm` |

#### 提供モジュール：`BrownianMotion.Auxiliary.ConvergenceInMeasure`

| 内容 | 宣言名の例 |
| --- | --- |
| 測度収束と部分列 | `TendstoInMeasure.add` |

#### 提供モジュール：`BrownianMotion.Auxiliary.DenseCountable`

| 内容 | 宣言名の例 |
| --- | --- |
| 可算稠密集合 | `denseCountable` |

#### 提供モジュール：`BrownianMotion.Auxiliary.ENNReal`

| 内容 | 宣言名の例 |
| --- | --- |
| 拡張非負実数の演算 | `ENNReal.sum_geometric_two_le` |
| 拡張非負実数の演算 | `ENNReal.ofReal_one_div` |

#### 提供モジュール：`BrownianMotion.Auxiliary.EVariationOn`

| 内容 | 宣言名の例 |
| --- | --- |
| 全変動の補題 | `eVariationOn_eq_iSup_fin` |
| 全変動の補題 | `eVariationOn_eq_comp_val_of_dense` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Filtration`

| 内容 | 宣言名の例 |
| --- | --- |
| 時間の取り直しとフィルトレーション | `Filtration.indexComap` |

#### 提供モジュール：`BrownianMotion.Auxiliary.FiniteInf`

| 内容 | 宣言名の例 |
| --- | --- |
| 有限個の下限 | `Finset.Nonempty.sSup_eq_max'` |
| 有限個の下限 | `Finset.iSup_eq_max'_image` |

#### 提供モジュール：`BrownianMotion.Auxiliary.HasGaussianLaw`

| 内容 | 宣言名の例 |
| --- | --- |
| ガウス法則の補題 | `HasGaussianLaw.charFun_toLp_pi` |
| ガウス法則の補題 | `HasGaussianLaw.charFun_toLp_prodMk` |

#### 提供モジュール：`BrownianMotion.Auxiliary.HasLaw`

| 内容 | 宣言名の例 |
| --- | --- |
| 分布と押し出し測度 | `hasLaw_map` |
| 分布と押し出し測度 | `HasLaw.ae_eq_const_of_gaussianReal` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Indistinguishable`

| 内容 | 宣言名の例 |
| --- | --- |
| 識別不能性 | `Indistinguishable` |

#### 提供モジュール：`BrownianMotion.Auxiliary.IsStoppingTime`

| 内容 | 宣言名の例 |
| --- | --- |
| 停止時刻と局所化列 | `stoppedProcess_min_eq_stoppedProcess` |
| 停止時刻と局所化列 | `WithTop.biInf_le_coe_iff_of_nhdsGT_eq_bot` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Jensen`

| 内容 | 宣言名の例 |
| --- | --- |
| 条件付き期待値の Jensen 型不等式 | `norm_condExp_le` |
| 条件付き期待値の Jensen 型不等式 | `enorm_condExp_le` |

#### 提供モジュール：`BrownianMotion.Auxiliary.LeftLimWithin`

| 内容 | 宣言名の例 |
| --- | --- |
| 部分集合に沿った左極限 | `Function.leftLimWithin` |
| 部分集合に沿った左極限 | `Function.rightLimWithin` |

#### 提供モジュール：`BrownianMotion.Auxiliary.LimitProcess`

| 内容 | 宣言名の例 |
| --- | --- |
| 極限過程 | `Filtration.limitProcess_ae_eq` |
| 極限過程 | `Filtration.limitProcess_congr` |

#### 提供モジュール：`BrownianMotion.Auxiliary.LinearAlgebra`

| 内容 | 宣言名の例 |
| --- | --- |
| 行列・線形写像の補題 | `mkContinuous₂OfFiniteDimensional` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Martingale`

| 内容 | 宣言名の例 |
| --- | --- |
| マルチンゲール性の保存 | `Martingale.stronglyMeasurable'` |
| マルチンゲール性の保存 | `Martingale.indicator` |

#### 提供モジュール：`BrownianMotion.Auxiliary.MeanInequalities`

| 内容 | 宣言名の例 |
| --- | --- |
| 平均・積分の不等式 | `rpow_lintegral_le` |
| 平均・積分の不等式 | `ENNReal.lintegral_Lp_finsum_le` |

#### 提供モジュール：`BrownianMotion.Auxiliary.MeasureTheory`

| 内容 | 宣言名の例 |
| --- | --- |
| 測度・可測性・積分の補題 | `integrable_inner` |
| 測度・可測性・積分の補題 | `condExp_inner_of_aestronglyMeasurable_left` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Metric`

| 内容 | 宣言名の例 |
| --- | --- |
| 距離の補題 | `Metric.IsSeparated.disjoint_ball` |
| 距離の補題 | `Metric.IsSeparated.disjoint_closedBall` |

#### 提供モジュール：`BrownianMotion.Auxiliary.NNReal`

| 内容 | 宣言名の例 |
| --- | --- |
| 非負実数の補題 | `NNReal.add_sub_two_mul_min_eq_max` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Nat`

| 内容 | 宣言名の例 |
| --- | --- |
| 自然数の補助評価 | `pow_two_mul_abs` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Real`

| 内容 | 宣言名の例 |
| --- | --- |
| 実数の補助評価 | `Real.inv_rpow_logb` |

#### 提供モジュール：`BrownianMotion.Auxiliary.SeparableSpace`

| 内容 | 宣言名の例 |
| --- | --- |
| 可算稠密集合による上限 | `Dense.mem_of_isOpen_singleton` |
| 可算稠密集合による上限 | `exists_isOpen_ordConnected_mem_subset` |

#### 提供モジュール：`BrownianMotion.Auxiliary.SetAlgebra`

| 内容 | 宣言名の例 |
| --- | --- |
| 集合族の有限・可算閉包 | `MonotoneClass` |
| 集合族の有限・可算閉包 | `MonotoneClass.ofDynkinSystem` |
| 集合族の有限・可算閉包 | `MonotoneClass.ofMeasurableSpace` |

#### 提供モジュール：`BrownianMotion.Auxiliary.StandardBorel`

| 内容 | 宣言名の例 |
| --- | --- |
| 標準 Borel 空間の import | import の集約 |

#### 提供モジュール：`BrownianMotion.Auxiliary.StoppedProcess`

| 内容 | 宣言名の例 |
| --- | --- |
| 停止過程の可測性と経路の性質 | `stoppedProcess_of_eq_top` |
| 停止過程の可測性と経路の性質 | `stoppedProcess_of_eq_coe` |

#### 提供モジュール：`BrownianMotion.Auxiliary.StoppedValue`

| 内容 | 宣言名の例 |
| --- | --- |
| 停止値の可測性と極限による停止値 | `Filtration.stoppedValue'` |

#### 提供モジュール：`BrownianMotion.Auxiliary.StronglyMeasurablePath`

| 内容 | 宣言名の例 |
| --- | --- |
| 経路空間への写像の強可測性 | `SimpleFunc.coe_finset_sum` |
| 経路空間への写像の強可測性 | `nhdsWithin_inter_Ioi_neBot` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Topology`

| 内容 | 宣言名の例 |
| --- | --- |
| 片側極限などの位相補題 | `eventually_nhdsGT` |
| 片側極限などの位相補題 | `neBot_comap_nhds` |

#### 提供モジュール：`BrownianMotion.Auxiliary.Upcrossing`

| 内容 | 宣言名の例 |
| --- | --- |
| 上方交差回数 | `hittingBtwn_self` |
| 上方交差回数 | `hittingBtwn_congr` |

#### 提供モジュール：`BrownianMotion.Auxiliary.WithLp`

| 内容 | 宣言名の例 |
| --- | --- |
| 有限積空間とノルム付き空間 | `PiLp.coe_proj` |
| 有限積空間とノルム付き空間 | `EuclideanSpace.proj_apply` |

## 文書表示の補助

#### 提供モジュール：`BrownianMotion.Verso.Brownian`

| 内容 | 宣言名の例 |
| --- | --- |
| 文書表示用のブラウン運動の表現 | `Ω` |
| 文書表示用のブラウン運動の表現 | `B` |

#### 提供モジュール：`BrownianMotion.Verso.Processes`

| 内容 | 宣言名の例 |
| --- | --- |
| 文書表示用の確率過程の表現 | 文書用の例 |

## 未証明部分を含む宣言

次の宣言の本体には `sorry` がある。利用先の定理も未証明部分に依存し得るため、ファイル単位の表示だけで証明の完成を判断しない。

#### 提供モジュール：`BrownianMotion.Gaussian.IteratedLogarithm`

| 宣言名 |
| --- |
| `IsBrownianReal.reflection` |
| `IsStandardGaussian.tail` |

#### 提供モジュール：`BrownianMotion.Choquet.CompactSystem`

| 宣言名 |
| --- |
| `IsCompactSystem.pi` |
| `IsCompactSystem.image2_prod` |
| `IsCompactSystem.countableInfClosure` |
| `IsCompactSystem.supClosure` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.ClassD`

| 宣言名 |
| --- |
| `hasStronglyMeasurableSupProcess_const` |
| `hasIntegrableSup_const` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.DoobLp`

| 宣言名 |
| --- |
| `integral_iSup_le_norm_rpow_le` |
| `integral_iSup_norm_rpow_le` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.DoobMeyer`

| 宣言名 |
| --- |
| `IsLocalSubmartingale.doob_meyer` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Komlos`

| 宣言名 |
| --- |
| `komlos_convergence_L2` |
| `komlos_ennreal` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.LocalMartingale`

| 宣言名 |
| --- |
| `isStable_submartingale` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.OptionalSampling`

| 宣言名 |
| --- |
| `Submartingale.stoppedValue_min_ae_le_condExp` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.QuadraticVariation`

| 宣言名 |
| --- |
| `hasLocallyIntegrableSup_predQuadCovariation` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.SquareIntegrable`

| 宣言名 |
| --- |
| `tendsto_ae_condExp'` |
| `IsSquareIntegrable.tendsto_eLpNorm_two_limitProcess` |
| `IsSquareIntegrable.iSup_eLpNorm_eq_eLpNorm_limitProcess` |
| `indistinguishable_of_modification'` |
| `isStable_isSquareIntegrable` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.UniformIntegrable`

| 宣言名 |
| --- |
| `Submartingale.uniformIntegrable_stoppedValue` |
| `Martingale.ae_tendsto_limitProcess` |
| `Martingale.condExp_limitProcess_ae_eq` |
| `Martingale.condExp_limitProcess_ae_eq'` |

[一覧](README.md)
