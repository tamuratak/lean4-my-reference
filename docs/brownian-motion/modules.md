# モジュール一覧

Brownian Motion のモジュールは、ガウス過程、連続な修正、可測選択、マルチンゲール・確率積分、共通補題に分かれる。

`BrownianMotion` は `BrownianMotion/` 配下のモジュールをまとめて公開する入口である。

## ガウス過程とブラウン運動

| モジュール | 内容 | 宣言名の例 |
| --- | --- | --- |
| `BrownianMotion.Gaussian.BrownianMotion` | ブラウン運動・Wiener 測度の構成 | `brownian` |
| `BrownianMotion.Gaussian.BrownianMotion` | ブラウン運動・Wiener 測度の構成 | `isBrownianReal_brownian` |
| `BrownianMotion.Gaussian.BrownianMotion` | ブラウン運動・Wiener 測度の構成 | `wienerMeasure` |
| `BrownianMotion.Gaussian.CovMatrix` | 共分散行列と半正定値性 | `covMatrix` |
| `BrownianMotion.Gaussian.Gaussian` | ガウス法則の特性関数 | `HasGaussianLaw.charFun_map_real` |
| `BrownianMotion.Gaussian.GaussianProcess` | ガウス過程の族の独立性 | `IsGaussianProcess.indepFun''` |
| `BrownianMotion.Gaussian.GaussianProcess` | ガウス過程の族の独立性 | `IsGaussianProcess.iIndepFun''` |
| `BrownianMotion.Gaussian.IteratedLogarithm` | 反射原理・裾評価・重複対数の法則。直接の `sorry` あり | `IsBrownianReal.reflection` |
| `BrownianMotion.Gaussian.IteratedLogarithm` | 反射原理・裾評価・重複対数の法則。直接の `sorry` あり | `IsStandardGaussian.tail` |
| `BrownianMotion.Gaussian.Moment` | 偶数次中心モーメント | `centralMoment_two_mul_gaussianReal` |
| `BrownianMotion.Gaussian.Moment` | 偶数次中心モーメント | `centralMoment_fun_two_mul_gaussianReal` |
| `BrownianMotion.Gaussian.MultivariateGaussian` | 多変量ガウスの成分分布と共分散 | `covMatrix_stdGaussian` |
| `BrownianMotion.Gaussian.MultivariateGaussian` | 多変量ガウスの成分分布と共分散 | `inner_toEuclideanCLM` |
| `BrownianMotion.Gaussian.ProjectiveLimit` | ガウス有限次元分布と射影極限 | `brownianCovMatrix` |
| `BrownianMotion.Gaussian.ProjectiveLimit` | ガウス有限次元分布と射影極限 | `gaussianProjectiveFamily` |
| `BrownianMotion.Gaussian.ProjectiveLimit` | ガウス有限次元分布と射影極限 | `gaussianLimit` |
| `BrownianMotion.Gaussian.StochasticProcesses` | 修正と識別不能性 | `modification_of_indistinguishable` |
| `BrownianMotion.Gaussian.StochasticProcesses` | 修正と識別不能性 | `indistinguishable_of_modification` |

## 経路の連続性

| モジュール | 内容 | 宣言名の例 |
| --- | --- | --- |
| `BrownianMotion.Continuity.Chaining` | 有限被覆をつなぐ chaining と距離評価 | `nearestPt` |
| `BrownianMotion.Continuity.Chaining` | 有限被覆をつなぐ chaining と距離評価 | `chainingSequenceReverse` |
| `BrownianMotion.Continuity.Chaining` | 有限被覆をつなぐ chaining と距離評価 | `chainingSequence` |
| `BrownianMotion.Continuity.CoveringNumber` | 被覆数・充填数と体積の評価 | `TotallyBounded.coveringNumber_ne_top` |
| `BrownianMotion.Continuity.CoveringNumber` | 被覆数・充填数と体積の評価 | `coveringNumber_Icc_zero_one_le_one_div` |
| `BrownianMotion.Continuity.HasBoundedInternalCoveringNumber` | 被覆数のべき上界と開被覆 | `HasBoundedCoveringNumber` |
| `BrownianMotion.Continuity.HasBoundedInternalCoveringNumber` | 被覆数のべき上界と開被覆 | `IsCoverWithBoundedCoveringNumber` |
| `BrownianMotion.Continuity.IsKolmogorovProcess` | 増分条件からの有限集合上の評価 | `finite_set_bound_of_edist_le` |
| `BrownianMotion.Continuity.KolmogorovChentsov` | Hölder 連続な修正の存在 | `holderModification` |
| `BrownianMotion.Continuity.KolmogorovChentsov` | Hölder 連続な修正の存在 | `exists_modification_holder` |
| `BrownianMotion.Continuity.KolmogorovChentsov` | Hölder 連続な修正の存在 | `exists_modification_holder_iSup` |
| `BrownianMotion.Continuity.KolmogorovChentsovInequality` | Kolmogorov–Chentsov 不等式 | `finite_kolmogorov_chentsov` |
| `BrownianMotion.Continuity.KolmogorovChentsovInequality` | Kolmogorov–Chentsov 不等式 | `countable_kolmogorov_chentsov` |
| `BrownianMotion.Continuity.LimitModification` | 極限・指示過程による可測な修正 | `indicatorProcess` |
| `BrownianMotion.Continuity.LimitModification` | 極限・指示過程による可測な修正 | `IsLimitOfIndicator` |

## 可測選択と到達時刻

| モジュール | 内容 | 宣言名の例 |
| --- | --- | --- |
| `BrownianMotion.Choquet.AnalyticSet` | 集合族による解析集合と射影 | `IsPavingAnalyticFor` |
| `BrownianMotion.Choquet.AnalyticSet` | 集合族による解析集合と射影 | `IsPavingAnalytic` |
| `BrownianMotion.Choquet.AnalyticSet` | 集合族による解析集合と射影 | `IsMeasurableAnalyticFor` |
| `BrownianMotion.Choquet.Capacity` | 容量可能性と射影の可測性 | `Capacity` |
| `BrownianMotion.Choquet.Capacity` | 容量可能性と射影の可測性 | `Measure.capacity` |
| `BrownianMotion.Choquet.Capacity` | 容量可能性と射影の可測性 | `Capacity.comp_fst` |
| `BrownianMotion.Choquet.CompactSystem` | コンパクト系と集合族の閉包。直接の `sorry` あり | `prodSigmaDelta` |
| `BrownianMotion.Choquet.Debut` | début と到達時刻の停止時刻性 | `debut` |
| `BrownianMotion.Choquet.Debut` | début と到達時刻の停止時刻性 | `ProgMeasurableSet` |
| `BrownianMotion.Choquet.Debut` | début と到達時刻の停止時刻性 | `leastGT` |
| `BrownianMotion.Choquet.MeasurableSection` | 可測切断の存在 | `MeasurableSet.exists_measurable_section_left_nnreal` |

## マルチンゲールと確率積分

| モジュール | 内容 | 宣言名の例 |
| --- | --- | --- |
| `BrownianMotion.StochasticIntegral.ApproxSeq` | 停止時刻の離散近似と停止値の収束 | `DiscreteApproxSequence` |
| `BrownianMotion.StochasticIntegral.ApproxSeq` | 停止時刻の離散近似と停止値の収束 | `Approximable` |
| `BrownianMotion.StochasticIntegral.ApproxSeq` | 停止時刻の離散近似と停止値の収束 | `IsStoppingTime.discreteApproxSequence` |
| `BrownianMotion.StochasticIntegral.Cadlag` | 右連続性・左極限・有界性 | `IsRightContinuous` |
| `BrownianMotion.StochasticIntegral.Cadlag` | 右連続性・左極限・有界性 | `IsCadlag` |
| `BrownianMotion.StochasticIntegral.Cadlag` | 右連続性・左極限・有界性 | `leftJumpSet` |
| `BrownianMotion.StochasticIntegral.ClassD` | class D・DL と上限の可積分性。直接の `sorry` あり | `ClassD` |
| `BrownianMotion.StochasticIntegral.ClassD` | class D・DL と上限の可積分性。直接の `sorry` あり | `ClassDL` |
| `BrownianMotion.StochasticIntegral.ClassD` | class D・DL と上限の可積分性。直接の `sorry` あり | `HasLocallyIntegrableSup` |
| `BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable` | 連続部分と純不連続部分への直交分解 | `continuousSquareIntegrable` |
| `BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable` | 連続部分と純不連続部分への直交分解 | `continuousPart` |
| `BrownianMotion.StochasticIntegral.ContinuousSquareIntegrable` | 連続部分と純不連続部分への直交分解 | `discontinuousPart` |
| `BrownianMotion.StochasticIntegral.ConvexWeights` | 凸結合の反復とノルム評価 | `Convexity.iteratedComb` |
| `BrownianMotion.StochasticIntegral.DoobLp` | 最大不等式と Doob の Lp 評価。直接の `sorry` あり | `maximal_ineq'` |
| `BrownianMotion.StochasticIntegral.DoobLp` | 最大不等式と Doob の Lp 評価。直接の `sorry` あり | `maximal_ineq_finset` |
| `BrownianMotion.StochasticIntegral.DoobMeyer` | class D の分解（`ClassD` 名前空間） | `ClassD.doob_meyer` |
| `BrownianMotion.StochasticIntegral.DoobMeyer` | 局所版の分解（`IsLocalSubmartingale` 名前空間）。直接の `sorry` あり | `IsLocalSubmartingale.doob_meyer` |
| `BrownianMotion.StochasticIntegral.DoobMeyerClassDL` | class DL の分解 | `ClassDL.exists_doob_meyer_increment` |
| `BrownianMotion.StochasticIntegral.DoobMeyerClassDL` | class DL の分解 | `ClassDL.doob_meyer` |
| `BrownianMotion.StochasticIntegral.Jump` | 左極限との差としてのジャンプ | `Function.jump` |
| `BrownianMotion.StochasticIntegral.Komlos` | 凸結合による Komlós 型収束。直接の `sorry` あり | `convexTail` |
| `BrownianMotion.StochasticIntegral.Komlos` | 凸結合による Komlós 型収束。直接の `sorry` あり | `komlosFormula` |
| `BrownianMotion.StochasticIntegral.L2M` | 積測度に関する予測可能過程の L2 空間 | `L2Predictable` |
| `BrownianMotion.StochasticIntegral.LocalMartingale` | 局所マルチンゲール・局所劣マルチンゲール。直接の `sorry` あり | `IsLocalMartingale` |
| `BrownianMotion.StochasticIntegral.LocalMartingale` | 局所マルチンゲール・局所劣マルチンゲール。直接の `sorry` あり | `IsLocalSubmartingale` |
| `BrownianMotion.StochasticIntegral.LocalMonad` | 局所化の圏・関手・モナド | `StableCat` |
| `BrownianMotion.StochasticIntegral.LocalMonad` | 局所化の圏・関手・モナド | `Local` |
| `BrownianMotion.StochasticIntegral.LocalMonad` | 局所化の圏・関手・モナド | `LocalFunctor` |
| `BrownianMotion.StochasticIntegral.LocalizingLeastGE` | ノルムの到達時刻による局所化 | `stoppedAtNorm` |
| `BrownianMotion.StochasticIntegral.LocalizingSequence` | 局所化列の合成・単調化・帰納法 | `LocalizingSequenceOfProp` |
| `BrownianMotion.StochasticIntegral.Locally` | 経路の正則性や適合性の局所化 | `locally_and_of_isStable` |
| `BrownianMotion.StochasticIntegral.Locally` | 経路の正則性や適合性の局所化 | `locally_of_ae` |
| `BrownianMotion.StochasticIntegral.MathlibImports` | mathlib の確率過程モジュールの集約 | import・記法の設定 |
| `BrownianMotion.StochasticIntegral.MonotoneProcess` | 単調過程の Stieltjes 測度核・ベクトル測度 | `StieltjesFunction.restrict` |
| `BrownianMotion.StochasticIntegral.MonotoneProcess` | 単調過程の Stieltjes 測度核・ベクトル測度 | `StieltjesFunction.rightContMono` |
| `BrownianMotion.StochasticIntegral.MonotoneProcess` | 単調過程の Stieltjes 測度核・ベクトル測度 | `StieltjesFunction.kernel` |
| `BrownianMotion.StochasticIntegral.OptionalSampling` | 任意抽出と停止過程。直接の `sorry` あり | `Martingale.condExp_stoppedValue_stopping_time_ae_eq_restrict_le_of_countable_range` |
| `BrownianMotion.StochasticIntegral.OptionalSampling` | 任意抽出と停止過程。直接の `sorry` あり | `Martingale.stoppedValue_min_ae_eq_condExp_of_countable_range` |
| `BrownianMotion.StochasticIntegral.Predictable` | 強予測可能性と生成集合 | `Filtration.IsComplete` |
| `BrownianMotion.StochasticIntegral.Predictable` | 強予測可能性と生成集合 | `Filtration.predictableRectangles` |
| `BrownianMotion.StochasticIntegral.PredictableTime` | 予測可能・到達可能・非到達可能な時刻 | `leftMeasurableSpace` |
| `BrownianMotion.StochasticIntegral.PredictableTime` | 予測可能・到達可能・非到達可能な時刻 | `IsPredictableTime` |
| `BrownianMotion.StochasticIntegral.PredictableTime` | 予測可能・到達可能・非到達可能な時刻 | `IsAccessibleTime` |
| `BrownianMotion.StochasticIntegral.QuadraticVariation` | 予測可能二次変分と二次共変分。直接の `sorry` あり | `predQuadVariation` |
| `BrownianMotion.StochasticIntegral.QuadraticVariation` | 予測可能二次変分と二次共変分。直接の `sorry` あり | `predQuadCovariation` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.Basic` | 実数値準マルチンゲール | `IsRealQuasimartingale` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.Basic` | 実数値準マルチンゲール | `variationBound` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModification` | 実数値準マルチンゲールの正則化 | `rightContModifReal` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModification` | 実数値準マルチンゲールの正則化 | `cadlagModifReal` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModificationBanach` | Banach 空間値マルチンゲールの正則化 | `rightContModif` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModificationBanach` | Banach 空間値マルチンゲールの正則化 | `cadlagModif` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModificationBanach` | Banach 空間値マルチンゲールの正則化 | `Martingale.martingale_cadlagModif` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.MaximalInequality` | 交差回数と最大不等式 | `finIdx` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.MaximalInequality` | 交差回数と最大不等式 | `elemPredSetOfSeq` |
| `BrownianMotion.StochasticIntegral.Quasimartingale.MaximalInequality` | 交差回数と最大不等式 | `upcrossingWithinPredSet` |
| `BrownianMotion.StochasticIntegral.SimpleProcess` | 単純過程と有限和の積分 | `ElementaryPredictableSet` |
| `BrownianMotion.StochasticIntegral.SimpleProcess` | 単純過程と有限和の積分 | `SimpleProcess` |
| `BrownianMotion.StochasticIntegral.SimpleProcess` | 単純過程と有限和の積分 | `SimpleProcess.integral` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | 二乗可積分マルチンゲールの空間。直接の `sorry` あり | `IsSquareIntegrable` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | 二乗可積分マルチンゲールの空間。直接の `sorry` あり | `IsAESquareIntegrable` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | 二乗可積分マルチンゲールの空間。直接の `sorry` あり | `IsAESquareIntegrable.toContinuous` |
| `BrownianMotion.StochasticIntegral.StochasticIntegral` | 一般の確率積分の公理的特徴付け | `IsRiemannStieltjesExtension` |
| `BrownianMotion.StochasticIntegral.StochasticIntegral` | 一般の確率積分の公理的特徴付け | `IsStochasticIntegral` |
| `BrownianMotion.StochasticIntegral.StochasticInterval` | 確率区間と時刻のグラフ | `stochIcc` |
| `BrownianMotion.StochasticIntegral.StochasticInterval` | 確率区間と時刻のグラフ | `stochIco` |
| `BrownianMotion.StochasticIntegral.StochasticInterval` | 確率区間と時刻のグラフ | `stochIoc` |
| `BrownianMotion.StochasticIntegral.UniformIntegrable` | 一様可積分性と極限過程。直接の `sorry` あり | `uniformIntegrable_iff'` |
| `BrownianMotion.StochasticIntegral.UniformIntegrable` | 一様可積分性と極限過程。直接の `sorry` あり | `uniformIntegrable_iff_tendsto_iSup_eLpNorm_indicator_norm` |
| `BrownianMotion.StochasticIntegral.VariationProcess` | 全変動の可測性・適合性 | `variationProcess` |

## 共通の補助理論

| モジュール | 内容 | 宣言名の例 |
| --- | --- | --- |
| `BrownianMotion.Auxiliary.AEEq` | 強適合過程の識別不能性による商 | `Measure.aeEqSetoid'` |
| `BrownianMotion.Auxiliary.AEEq` | 強適合過程の識別不能性による商 | `AEEqProcess` |
| `BrownianMotion.Auxiliary.AEEq` | 強適合過程の識別不能性による商 | `AEStronglyAdapted.mk` |
| `BrownianMotion.Auxiliary.Adapted` | 強適合性と強発展的可測性 | `SimpleFunc.IndexedPartition` |
| `BrownianMotion.Auxiliary.Adapted` | 強適合性と強発展的可測性 | `AEStronglyAdapted` |
| `BrownianMotion.Auxiliary.Adapted` | 強適合性と強発展的可測性 | `AEStronglyAdapted.mk` |
| `BrownianMotion.Auxiliary.Algebra` | 代数演算の補題 | `Set.indicator_apply_apply` |
| `BrownianMotion.Auxiliary.Algebra` | 代数演算の補題 | `Monotone.finset_sum` |
| `BrownianMotion.Auxiliary.Analysis` | 解析の補助評価 | `convexOn_subsingleton` |
| `BrownianMotion.Auxiliary.Analysis` | 解析の補助評価 | `convexOn_rpow_norm` |
| `BrownianMotion.Auxiliary.ContinuousBilinForm` | 連続双線形形式 | `ContinuousBilinForm` |
| `BrownianMotion.Auxiliary.ContinuousBilinForm` | 連続双線形形式 | `ContinuousBilinForm.toBilinForm` |
| `BrownianMotion.Auxiliary.ContinuousBilinForm` | 連続双線形形式 | `ContinuousBilinForm.IsSymm` |
| `BrownianMotion.Auxiliary.ConvergenceInMeasure` | 測度収束と部分列 | `TendstoInMeasure.add` |
| `BrownianMotion.Auxiliary.DenseCountable` | 可算稠密集合 | `denseCountable` |
| `BrownianMotion.Auxiliary.ENNReal` | 拡張非負実数の演算 | `ENNReal.sum_geometric_two_le` |
| `BrownianMotion.Auxiliary.ENNReal` | 拡張非負実数の演算 | `ENNReal.ofReal_one_div` |
| `BrownianMotion.Auxiliary.EVariationOn` | 全変動の補題 | `eVariationOn_eq_iSup_fin` |
| `BrownianMotion.Auxiliary.EVariationOn` | 全変動の補題 | `eVariationOn_eq_comp_val_of_dense` |
| `BrownianMotion.Auxiliary.Filtration` | 時間の取り直しとフィルトレーション | `Filtration.indexComap` |
| `BrownianMotion.Auxiliary.FiniteInf` | 有限個の下限 | `Finset.Nonempty.sSup_eq_max'` |
| `BrownianMotion.Auxiliary.FiniteInf` | 有限個の下限 | `Finset.iSup_eq_max'_image` |
| `BrownianMotion.Auxiliary.HasGaussianLaw` | ガウス法則の補題 | `HasGaussianLaw.charFun_toLp_pi` |
| `BrownianMotion.Auxiliary.HasGaussianLaw` | ガウス法則の補題 | `HasGaussianLaw.charFun_toLp_prodMk` |
| `BrownianMotion.Auxiliary.HasLaw` | 分布と押し出し測度 | `hasLaw_map` |
| `BrownianMotion.Auxiliary.HasLaw` | 分布と押し出し測度 | `HasLaw.ae_eq_const_of_gaussianReal` |
| `BrownianMotion.Auxiliary.Indistinguishable` | 識別不能性 | `Indistinguishable` |
| `BrownianMotion.Auxiliary.IsStoppingTime` | 停止時刻と局所化列 | `stoppedProcess_min_eq_stoppedProcess` |
| `BrownianMotion.Auxiliary.IsStoppingTime` | 停止時刻と局所化列 | `WithTop.biInf_le_coe_iff_of_nhdsGT_eq_bot` |
| `BrownianMotion.Auxiliary.Jensen` | 条件付き期待値の Jensen 型不等式 | `norm_condExp_le` |
| `BrownianMotion.Auxiliary.Jensen` | 条件付き期待値の Jensen 型不等式 | `enorm_condExp_le` |
| `BrownianMotion.Auxiliary.LeftLimWithin` | 部分集合に沿った左極限 | `Function.leftLimWithin` |
| `BrownianMotion.Auxiliary.LeftLimWithin` | 部分集合に沿った左極限 | `Function.rightLimWithin` |
| `BrownianMotion.Auxiliary.LimitProcess` | 極限過程 | `Filtration.limitProcess_ae_eq` |
| `BrownianMotion.Auxiliary.LimitProcess` | 極限過程 | `Filtration.limitProcess_congr` |
| `BrownianMotion.Auxiliary.LinearAlgebra` | 行列・線形写像の補題 | `mkContinuous₂OfFiniteDimensional` |
| `BrownianMotion.Auxiliary.Martingale` | マルチンゲール性の保存 | `Martingale.stronglyMeasurable'` |
| `BrownianMotion.Auxiliary.Martingale` | マルチンゲール性の保存 | `Martingale.indicator` |
| `BrownianMotion.Auxiliary.MeanInequalities` | 平均・積分の不等式 | `rpow_lintegral_le` |
| `BrownianMotion.Auxiliary.MeanInequalities` | 平均・積分の不等式 | `ENNReal.lintegral_Lp_finsum_le` |
| `BrownianMotion.Auxiliary.MeasureTheory` | 測度・可測性・積分の補題 | `integrable_inner` |
| `BrownianMotion.Auxiliary.MeasureTheory` | 測度・可測性・積分の補題 | `condExp_inner_of_aestronglyMeasurable_left` |
| `BrownianMotion.Auxiliary.Metric` | 距離の補題 | `Metric.IsSeparated.disjoint_ball` |
| `BrownianMotion.Auxiliary.Metric` | 距離の補題 | `Metric.IsSeparated.disjoint_closedBall` |
| `BrownianMotion.Auxiliary.NNReal` | 非負実数の補題 | `NNReal.add_sub_two_mul_min_eq_max` |
| `BrownianMotion.Auxiliary.Nat` | 自然数の補助評価 | `pow_two_mul_abs` |
| `BrownianMotion.Auxiliary.Real` | 実数の補助評価 | `Real.inv_rpow_logb` |
| `BrownianMotion.Auxiliary.SeparableSpace` | 可算稠密集合による上限 | `Dense.mem_of_isOpen_singleton` |
| `BrownianMotion.Auxiliary.SeparableSpace` | 可算稠密集合による上限 | `exists_isOpen_ordConnected_mem_subset` |
| `BrownianMotion.Auxiliary.SetAlgebra` | 集合族の有限・可算閉包 | `MonotoneClass` |
| `BrownianMotion.Auxiliary.SetAlgebra` | 集合族の有限・可算閉包 | `MonotoneClass.ofDynkinSystem` |
| `BrownianMotion.Auxiliary.SetAlgebra` | 集合族の有限・可算閉包 | `MonotoneClass.ofMeasurableSpace` |
| `BrownianMotion.Auxiliary.StandardBorel` | 標準 Borel 空間の import | import の集約 |
| `BrownianMotion.Auxiliary.StoppedProcess` | 停止過程の可測性と経路の性質 | `stoppedProcess_of_eq_top` |
| `BrownianMotion.Auxiliary.StoppedProcess` | 停止過程の可測性と経路の性質 | `stoppedProcess_of_eq_coe` |
| `BrownianMotion.Auxiliary.StoppedValue` | 停止値の可測性と極限による停止値 | `Filtration.stoppedValue'` |
| `BrownianMotion.Auxiliary.StronglyMeasurablePath` | 経路空間への写像の強可測性 | `SimpleFunc.coe_finset_sum` |
| `BrownianMotion.Auxiliary.StronglyMeasurablePath` | 経路空間への写像の強可測性 | `nhdsWithin_inter_Ioi_neBot` |
| `BrownianMotion.Auxiliary.Topology` | 片側極限などの位相補題 | `eventually_nhdsGT` |
| `BrownianMotion.Auxiliary.Topology` | 片側極限などの位相補題 | `neBot_comap_nhds` |
| `BrownianMotion.Auxiliary.Upcrossing` | 上方交差回数 | `hittingBtwn_self` |
| `BrownianMotion.Auxiliary.Upcrossing` | 上方交差回数 | `hittingBtwn_congr` |
| `BrownianMotion.Auxiliary.WithLp` | 有限積空間とノルム付き空間 | `PiLp.coe_proj` |
| `BrownianMotion.Auxiliary.WithLp` | 有限積空間とノルム付き空間 | `EuclideanSpace.proj_apply` |

## 文書表示の補助

| モジュール | 内容 | 宣言名の例 |
| --- | --- | --- |
| `BrownianMotion.Verso.Brownian` | 文書表示用のブラウン運動の表現 | `Ω` |
| `BrownianMotion.Verso.Brownian` | 文書表示用のブラウン運動の表現 | `B` |
| `BrownianMotion.Verso.Processes` | 文書表示用の確率過程の表現 | 文書用の例 |

## 未証明部分を含む宣言

次の宣言の本体には `sorry` がある。利用先の定理も未証明部分に依存し得るため、ファイル単位の表示だけで証明の完成を判断しない。

| モジュール | 宣言名 |
| --- | --- |
| `BrownianMotion.Gaussian.IteratedLogarithm` | `IsBrownianReal.reflection` |
| `BrownianMotion.Gaussian.IteratedLogarithm` | `IsStandardGaussian.tail` |
| `BrownianMotion.Choquet.CompactSystem` | `IsCompactSystem.pi` |
| `BrownianMotion.Choquet.CompactSystem` | `IsCompactSystem.image2_prod` |
| `BrownianMotion.Choquet.CompactSystem` | `IsCompactSystem.countableInfClosure` |
| `BrownianMotion.Choquet.CompactSystem` | `IsCompactSystem.supClosure` |
| `BrownianMotion.StochasticIntegral.ClassD` | `hasStronglyMeasurableSupProcess_const` |
| `BrownianMotion.StochasticIntegral.ClassD` | `hasIntegrableSup_const` |
| `BrownianMotion.StochasticIntegral.DoobLp` | `integral_iSup_le_norm_rpow_le` |
| `BrownianMotion.StochasticIntegral.DoobLp` | `integral_iSup_norm_rpow_le` |
| `BrownianMotion.StochasticIntegral.DoobMeyer` | `IsLocalSubmartingale.doob_meyer` |
| `BrownianMotion.StochasticIntegral.Komlos` | `komlos_convergence_L2` |
| `BrownianMotion.StochasticIntegral.Komlos` | `komlos_ennreal` |
| `BrownianMotion.StochasticIntegral.LocalMartingale` | `isStable_submartingale` |
| `BrownianMotion.StochasticIntegral.OptionalSampling` | `Submartingale.stoppedValue_min_ae_le_condExp` |
| `BrownianMotion.StochasticIntegral.QuadraticVariation` | `hasLocallyIntegrableSup_predQuadCovariation` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | `tendsto_ae_condExp'` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | `IsSquareIntegrable.tendsto_eLpNorm_two_limitProcess` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | `IsSquareIntegrable.iSup_eLpNorm_eq_eLpNorm_limitProcess` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | `indistinguishable_of_modification'` |
| `BrownianMotion.StochasticIntegral.SquareIntegrable` | `isStable_isSquareIntegrable` |
| `BrownianMotion.StochasticIntegral.UniformIntegrable` | `Submartingale.uniformIntegrable_stoppedValue` |
| `BrownianMotion.StochasticIntegral.UniformIntegrable` | `Martingale.ae_tendsto_limitProcess` |
| `BrownianMotion.StochasticIntegral.UniformIntegrable` | `Martingale.condExp_limitProcess_ae_eq` |
| `BrownianMotion.StochasticIntegral.UniformIntegrable` | `Martingale.condExp_limitProcess_ae_eq'` |

[一覧](README.md)
