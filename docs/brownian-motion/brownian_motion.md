# ガウス過程とブラウン運動

ブラウン運動は、独立なガウス増分と連続な経路を持つ確率過程である。Brownian Motion では、時間を非負実数、値を実数とし、有限次元分布の構成、過程全体の分布の構成、連続な修正の構成という段階を経て、具体的なブラウン運動を与える。

## 確率過程と分布の表現

| 数学の対象 | Lean の表現 | 意味 |
| --- | --- | --- |
| 確率過程 $(X_t)_{t\in T}$ | `X : T → Ω → E` | 時刻と標本点から値を返す関数 |
| 固定時刻の確率変数 $X_t$ | `X t` | `Ω → E` 型の関数 |
| 固定標本点の経路 $t\mapsto X_t(\omega)$ | `fun t ↦ X t ω` | `T → E` 型の関数 |
| $X$ の法則が $\nu$ | `ProbabilityTheory.HasLaw X ν P` | ほとんど至る所での可測性 `AEMeasurable X P` と押し出し測度の等式 |
| 有限個の時刻での同時分布 | `fun ω ↦ I.restrict (X · ω)` | `I : Finset T` への制限 |
| 実数値前ブラウン運動 | `ProbabilityTheory.IsPreBrownianReal X P` | ブラウン運動に対応する有限次元分布 |
| 実数値ブラウン運動 | `ProbabilityTheory.IsBrownianReal X P` | 前ブラウン運動に連続性を加えた性質 |

`IsPreBrownianReal` と `IsBrownianReal` は mathlib 由来である。外部ライブラリの中心は、それらの性質を満たす過程の構成と追加の性質にある。

## ガウス分布と共分散

ガウス過程は、有限個の時刻での値が同時にガウス分布に従う過程である。ガウス族では、共分散の消滅から独立性を導けるため、ブラウン運動の独立増分の証明に利用できる。

#### 提供モジュール：`BrownianMotion.Gaussian.CovMatrix`

| 内容 | 宣言名 |
| --- | --- |
| 共分散双線形形式の行列表現 | `ProbabilityTheory.covMatrix` |
| 共分散行列の半正定値性 | `ProbabilityTheory.posSemidef_covMatrix` |

#### 提供モジュール：`BrownianMotion.Gaussian.MultivariateGaussian`

| 内容 | 宣言名 |
| --- | --- |
| 標準ガウス分布の共分散行列 | `ProbabilityTheory.covMatrix_stdGaussian` |
| 多変量ガウス分布の一成分の法則 | `ProbabilityTheory.hasLaw_eval_multivariateGaussian` |

#### 提供モジュール：`BrownianMotion.Gaussian.Gaussian`

| 内容 | 宣言名 |
| --- | --- |
| ガウス確率変数の特性関数 | `ProbabilityTheory.HasGaussianLaw.charFun_map_real` |

#### 提供モジュール：`BrownianMotion.Gaussian.Moment`

| 内容 | 宣言名 |
| --- | --- |
| ガウス分布の偶数次中心モーメント | `ProbabilityTheory.centralMoment_two_mul_gaussianReal` |
| ガウス分布の偶数次中心モーメント | `ProbabilityTheory.centralMoment_fun_two_mul_gaussianReal` |

#### 提供モジュール：`BrownianMotion.Gaussian.GaussianProcess`

| 内容 | 宣言名 |
| --- | --- |
| ガウス過程の族の独立性 | `ProbabilityTheory.IsGaussianProcess.indepFun''` |
| ガウス過程の族の独立性 | `ProbabilityTheory.IsGaussianProcess.iIndepFun''` |

独立性の定理は、対象となる過程の組がガウス過程であること、交差する共分散が零であることなどを仮定する。一般の確率変数では無相関だけから独立性は導けない。

## 有限次元分布と射影極限

ブラウン運動の共分散は $\operatorname{Cov}(B_s,B_t)=\min(s,t)$ である。有限時刻集合 $I$ に対して、この共分散行列を持つ平均零のガウス分布を用意する。

| 数学の対象・性質 | 宣言名 |
| --- | --- |
| 成分が $\min(s,t)$ の行列 | `ProbabilityTheory.brownianCovMatrix` |
| 共分散行列の半正定値性 | `ProbabilityTheory.posSemidef_brownianCovMatrix` |
| 有限時刻集合上のガウス分布 | `ProbabilityTheory.gaussianProjectiveFamily` |
| 部分集合への制限と分布の整合性 | `ProbabilityTheory.isProjectiveMeasureFamily_gaussianProjectiveFamily` |
| 全時刻の関数空間上の測度 | `ProbabilityTheory.gaussianLimit` |
| 射影極限としての性質 | `ProbabilityTheory.isProjectiveLimit_gaussianLimit` |
| 有限次元周辺分布 | `ProbabilityTheory.hasLaw_restrict_gaussianLimit` |
| 一時刻の分布、二時刻の共分散 | `ProbabilityTheory.hasLaw_eval_gaussianLimit` |
| 一時刻の分布、二時刻の共分散 | `ProbabilityTheory.covariance_eval_gaussianLimit` |

対応するモジュールは `BrownianMotion.Gaussian.ProjectiveLimit` である。`gaussianLimit` は経路の集合 `ℝ≥0 → ℝ` 上の測度であり、連続関数だけを要素とする空間上の測度とは型が異なる。

## 連続なブラウン運動の構成

`preBrownian t ω = ω t` は、関数空間の要素を時刻で評価する座標過程である。測度を `gaussianLimit` に取ると前ブラウン運動になる。増分の偶数次モーメントを評価し、Kolmogorov–Chentsov の定理で連続な修正を選んだものが `brownian` である。

| 対象・性質 | 宣言名 |
| --- | --- |
| 座標過程 | `ProbabilityTheory.preBrownian` |
| 前ブラウン運動であること | `ProbabilityTheory.isPreBrownianReal_preBrownian` |
| 一般の前ブラウン運動の連続な修正 | `ProbabilityTheory.IsPreBrownianReal.mk` |
| 元の過程との各時刻でのほとんど確実な一致 | `ProbabilityTheory.IsPreBrownianReal.mk_ae_eq` |
| 具体的な連続過程 | `ProbabilityTheory.brownian` |
| ブラウン運動であること | `ProbabilityTheory.isBrownianReal_brownian` |
| 各経路の連続性 | `ProbabilityTheory.continuous_brownian` |
| 各時刻の可測性、時間と標本点の同時可測性 | `ProbabilityTheory.measurable_brownian` |
| 各時刻の可測性、時間と標本点の同時可測性 | `ProbabilityTheory.measurable_brownian_uncurry` |
| 独立増分 | `ProbabilityTheory.hasIndepIncrements_brownian` |
| 共分散 $\min(s,t)$ | `ProbabilityTheory.covariance_brownian` |
| $B_t\sim N(0,t)$ | `ProbabilityTheory.hasLaw_brownian_eval` |
| $B_s-B_t\sim N(0,\lvert s-t\rvert)$ | `ProbabilityTheory.hasLaw_brownian_sub` |
| 任意の $0<\beta<1/2$ に対する局所 Hölder 連続性 | `ProbabilityTheory.memHolder_brownian` |

対応するモジュールは `BrownianMotion.Gaussian.BrownianMotion` である。`gaussianReal 0 t` の第2引数は分散を表す。`brownian` は `ℝ≥0 → (ℝ≥0 → ℝ) → ℝ` 型で、確率空間には測度 `gaussianLimit` を使う。

`BrownianMotion.Gaussian.BrownianMotion` をインポートし、`t : ℝ≥0` が与えられているとき、固定時刻の分布の証明は次の式で得られる。

```text
ProbabilityTheory.hasLaw_brownian_eval (t := t)
```

得られる証明の型は次の命題である。

```text
ProbabilityTheory.HasLaw (ProbabilityTheory.brownian t)
  (ProbabilityTheory.gaussianReal 0 t) ProbabilityTheory.gaussianLimit
```

数学では $B_t\sim N(0,t)$ に対応する。時刻は暗黙引数なので、`(t := t)` と名前を指定して渡せる。例えば `(t := 1)` とすれば、時刻 $1$ の値が平均 $0$、分散 $1$ の標準正規分布に従うという命題の証明になる。

## フィルトレーションと追加の性質

`ProbabilityTheory.IsFilteredPreBrownian X 𝓕 P` は、前ブラウン運動の性質に、`𝓕` への強適合性と、時刻 $s$ 以後の増分の $\mathcal{F}_s$ からの独立性を加える。

| 内容 | 宣言名 |
| --- | --- |
| 自然フィルトレーションに関する filtered 性 | `ProbabilityTheory.IsPreBrownianReal.isFilteredPreBrownian` |
| filtered な前ブラウン運動のマルチンゲール性 | `ProbabilityTheory.IsPreBrownianReal.isMartingale` |
| 時間反転によるブラウン運動 | `ProbabilityTheory.IsBrownianReal.inv` |
| $B_t/t\to0$ のほとんど確実な成立 | `ProbabilityTheory.IsBrownianReal.tendsto_div_id_atTop` |
| 初期情報に対する Blumenthal の零一法則 | `ProbabilityTheory.IsBrownianReal.indep_zero` |
| 連続経路空間上の Wiener 測度 | `ProbabilityTheory.wienerMeasure` |

`wienerMeasure` の型は `Measure C(ℝ≥0, ℝ)` である。`brownian` の経路を連続関数としてまとめ、その分布を取る。

`indep_zero` は、自然フィルトレーションの $\bigcap_{s>0}\mathcal{F}_s$ に属する事象の確率が $0$ または $1$ であることを述べる。各時刻の可測性と全経路の連続性を仮定する。

マルチンゲール性には、指定したフィルトレーションとの適合性・独立性が必要である。ブラウン運動であることだけから、任意のフィルトレーションに関するマルチンゲール性が得られるわけではない。

## 反射原理と重複対数の法則の未証明部分

`BrownianMotion.Gaussian.IteratedLogarithm` には、次の宣言がある。

| 内容 | 宣言名 | 状態 |
| --- | --- | --- |
| 反射原理 | `ProbabilityTheory.IsBrownianReal.reflection` | 直接 `sorry` |
| 標準正規分布の裾の漸近評価 | `ProbabilityTheory.IsStandardGaussian.tail` | 直接 `sorry` |
| 重複対数の法則 | `ProbabilityTheory.IsBrownianReal.ae_limsup_div_sqrt_log_log_eq_one` | 上記の未証明部分に依存 |

重複対数の法則の定理文に現れる正規化は $\sqrt{2t\log\log t}$ であり、$t\to\infty$ における $B_t/\sqrt{2t\log\log t}$ の上極限がほとんど確実に $1$ となる形である。ファイル冒頭の説明文では分母の $t$ が落ちているため、定理文との区別が必要である。

裾評価の現行の宣言では、漸近比較の右辺が $x^{-1}\exp(-x^2/2)$ となっており、標準正規分布の通常の漸近同値に必要な係数 $1/\sqrt{2\pi}$ が含まれていない。未証明という点に加え、命題そのものにも注意が必要である。

[一覧](README.md)
