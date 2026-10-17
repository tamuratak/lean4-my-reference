# 確率過程の連続性と修正

確率過程の修正は、各時刻の確率変数をほとんど確実に変えずに、経路の連続性などを改善した過程である。Brownian Motion は、モーメント評価から Hölder 連続な修正を構成する理論と、マルチンゲールの右連続・左極限を持つ修正の理論を提供する。

## 修正と識別不能性

| 関係 | 数学 | Lean |
| --- | --- | --- |
| 各時刻でほとんど確実に一致する修正 | $\forall t,\ P(X_t=Y_t)=1$ | `∀ t, X t =ᵐ[P] Y t` |
| 識別不能 | $P(\forall t,\ X_t=Y_t)=1$ | `ProbabilityTheory.Indistinguishable P X Y` |
| 識別不能 | $P(\forall t,\ X_t=Y_t)=1$ | `X ≡ᵐ[P] Y` |

識別不能性では、時間によらない共通の零集合の外で経路全体が一致する。時刻集合が非可算の場合、各時刻の例外集合を単にまとめても零集合になるとは限らない。

`BrownianMotion.Auxiliary.Indistinguishable` は識別不能性の定義と、各時刻の一致や停止値の一致を扱う補題を提供する。`BrownianMotion.Gaussian.StochasticProcesses` の `indistinguishable_of_modification` は、時間空間の可分性、値域の Hausdorff 性、両過程のほとんど確実な経路連続性の下で、修正から識別不能性を導く。

`MeasureTheory.AEEqProcess` は、ほとんど確実に強適合な過程を識別不能性で同一視する商型である。定義元は `BrownianMotion.Auxiliary.AEEq` であり、二乗可積分マルチンゲールの空間の基礎になる。

## 被覆数と増分のモーメント条件

Kolmogorov–Chentsov の定理は、時間空間の大きさと増分のモーメントを比較して経路の正則性を得る。被覆数を $N(U,\varepsilon)$ とすると、典型的な仮定は

$$
N(U,\varepsilon)\le c\varepsilon^{-d},\qquad
\mathbb{E}[d(X_s,X_t)^p]\le M d(s,t)^q
$$

である。$d<q$ のとき、指数 $0<\beta<(q-d)/p$ の Hölder 連続な修正が得られる。被覆数の指数 $d$ と距離記号 $d(\cdot,\cdot)$ は役割が異なる。

#### 提供モジュール：`BrownianMotion.Continuity.HasBoundedInternalCoveringNumber`

| 条件・結果 | 宣言名 |
| --- | --- |
| 有限直径と被覆数のべき上界 | `HasBoundedCoveringNumber` |
| 開集合による被覆と被覆数の条件 | `IsCoverWithBoundedCoveringNumber` |
| 非負実数時間への被覆条件の適用 | `isCoverWithBoundedCoveringNumber_Ico_nnreal` |

#### 提供モジュール：mathlib

| 条件・結果 | 宣言名 |
| --- | --- |
| 増分のモーメント条件 | `ProbabilityTheory.IsKolmogorovProcess` |
| 増分のモーメント条件 | `ProbabilityTheory.IsAEKolmogorovProcess` |

#### 提供モジュール：`BrownianMotion.Continuity.KolmogorovChentsovInequality`

| 条件・結果 | 宣言名 |
| --- | --- |
| 有限集合・可算集合上の Hölder 商の評価 | `ProbabilityTheory.finite_kolmogorov_chentsov` |
| 有限集合・可算集合上の Hölder 商の評価 | `ProbabilityTheory.countable_kolmogorov_chentsov` |
| Hölder 商のほとんど確実な有限性 | `ProbabilityTheory.IsKolmogorovProcess.ae_iSup_rpow_edist_div_lt_top` |

#### 提供モジュール：`BrownianMotion.Continuity.Chaining`

| 条件・結果 | 宣言名 |
| --- | --- |
| 有限被覆間の chaining | `chainingSequence` |

`BrownianMotion.Continuity.IsKolmogorovProcess` は、既存のモーメント条件から有限集合上の評価を導く追加補題をまとめる。ファイル名と、そのファイルが基本定義を新設しているかどうかは別である。

## Hölder 連続な修正の存在

`BrownianMotion.Continuity.KolmogorovChentsov` の `ProbabilityTheory.exists_modification_holder` は、開集合 `U` 上の被覆数条件とモーメント条件から、各時刻で可測で、`U` 上で元の過程の修正となり、指定範囲の指数に対して各経路が Hölder 連続な過程を与える。値域には完備距離空間などの仮定がある。

#### 提供モジュール：`BrownianMotion.Continuity.KolmogorovChentsov`

| 用途 | 宣言名 |
| --- | --- |
| 一つの開集合上の修正 | `ProbabilityTheory.exists_modification_holder` |
| 開集合の被覆を使った局所的な修正 | `ProbabilityTheory.exists_modification_holder'` |
| モーメント指数の列から得られる正則性 | `ProbabilityTheory.exists_modification_holder_iSup` |

#### 提供モジュール：`BrownianMotion.Continuity.LimitModification`

| 用途 | 宣言名 |
| --- | --- |
| 修正を極限として構成する可測性の補助理論 | `ProbabilityTheory.IsLimitOfIndicator` など |

ブラウン運動では $p=2n$、$q=n$、時間空間の被覆数指数 $d=1$ を使うため、$\beta<(n-1)/(2n)$ が得られる。$n$ を大きくすることで、任意の $0<\beta<1/2$ に対応する。適用結果が `ProbabilityTheory.memHolder_brownian` である。

## 右連続性と càdlàg 経路

càdlàg は、経路が右連続で、左極限を持つという性質である。ジャンプを許すため、一般のマルチンゲールを扱う際の基本的な経路条件になる。

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Cadlag`

| 対象・性質 | 宣言名 |
| --- | --- |
| 右連続な関数 | `IsRightContinuous` |
| càdlàg な関数 | `IsCadlag` |
| コンパクト集合上の有界性 | `isBounded_image_of_isCadlag_of_isCompact` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Jump`

| 対象・性質 | 宣言名 |
| --- | --- |
| ジャンプの大きさ | `Function.jump` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.Basic`

| 対象・性質 | 宣言名 |
| --- | --- |
| 実数値準マルチンゲール | `ProbabilityTheory.IsRealQuasimartingale` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.MaximalInequality`

| 対象・性質 | 宣言名 |
| --- | --- |
| 交差回数・最大値の評価 | `ProbabilityTheory.measure_all_infiniteAlt` |
| 交差回数・最大値の評価 | `ProbabilityTheory.measure_exists_abs_gt_le` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModification`

| 対象・性質 | 宣言名 |
| --- | --- |
| 実数値の右連続・càdlàg 修正 | `ProbabilityTheory.rightContModifReal` |
| 実数値の右連続・càdlàg 修正 | `ProbabilityTheory.cadlagModifReal` |

#### 提供モジュール：`BrownianMotion.StochasticIntegral.Quasimartingale.CadlagModificationBanach`

| 対象・性質 | 宣言名 |
| --- | --- |
| Banach 空間値の右連続・càdlàg 修正 | `ProbabilityTheory.rightContModif` |
| Banach 空間値の右連続・càdlàg 修正 | `ProbabilityTheory.cadlagModif` |
| 修正後のマルチンゲール性 | `MeasureTheory.Martingale.martingale_cadlagModif` |

修正を関数として定義できることと、各時刻で元の過程にほとんど確実に一致することは別の主張である。後者にはフィルトレーションの右連続性や、測度収束・可積分性など、対応する定理の仮定が必要になる。

[一覧](README.md)
