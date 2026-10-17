# Brownian Motion の確率過程・確率解析リファレンス

Brownian Motion は、実数値ブラウン運動の構成と、確率積分に必要なマルチンゲール理論を提供する Lean ライブラリである。ガウス有限次元分布から連続なブラウン運動を構成する部分に加え、停止時刻、予測可能性、局所化、Doob–Meyer 分解、予測可能二次変分を扱う。

## 数学の対象と記事の対応

| 数学の対象 | 記事 | 主な宣言・内容 |
| --- | --- | --- |
| ガウス分布、有限次元分布、ブラウン運動、Wiener 測度 | [ガウス過程とブラウン運動](brownian_motion.md) | `gaussianLimit` |
| ガウス分布、有限次元分布、ブラウン運動、Wiener 測度 | [ガウス過程とブラウン運動](brownian_motion.md) | `brownian` |
| ガウス分布、有限次元分布、ブラウン運動、Wiener 測度 | [ガウス過程とブラウン運動](brownian_motion.md) | `isBrownianReal_brownian` |
| ガウス分布、有限次元分布、ブラウン運動、Wiener 測度 | [ガウス過程とブラウン運動](brownian_motion.md) | `wienerMeasure` |
| 修正、識別不能性、Hölder 連続性、経路の正則化 | [確率過程の連続性と修正](regularity.md) | `Indistinguishable` |
| 修正、識別不能性、Hölder 連続性、経路の正則化 | [確率過程の連続性と修正](regularity.md) | `exists_modification_holder` |
| 修正、識別不能性、Hölder 連続性、経路の正則化 | [確率過程の連続性と修正](regularity.md) | `cadlagModif` |
| 停止時刻、任意抽出、局所マルチンゲール、分解 | [停止時刻とマルチンゲール](martingales.md) | `debut` |
| 停止時刻、任意抽出、局所マルチンゲール、分解 | [停止時刻とマルチンゲール](martingales.md) | `ClassD` |
| 停止時刻、任意抽出、局所マルチンゲール、分解 | [停止時刻とマルチンゲール](martingales.md) | `IsLocalMartingale` |
| 停止時刻、任意抽出、局所マルチンゲール、分解 | [停止時刻とマルチンゲール](martingales.md) | `ClassDL.doob_meyer` |
| 単純過程の積分、二次変分、積分の公理的特徴付け | [確率積分と二次変分](stochastic_integral.md) | `SimpleProcess.integral` |
| 単純過程の積分、二次変分、積分の公理的特徴付け | [確率積分と二次変分](stochastic_integral.md) | `predQuadVariation` |
| 単純過程の積分、二次変分、積分の公理的特徴付け | [確率積分と二次変分](stochastic_integral.md) | `IsStochasticIntegral` |
| 各モジュールの担当範囲、補助定理 | [モジュール一覧](modules.md) | `BrownianMotion/` 配下の全 Lean モジュール |

## 形式化の到達点

| 対象 | 提供される内容 | 証明上の注意 |
| --- | --- | --- |
| ブラウン運動の存在 | 非負実数時間の実数値ブラウン運動、各経路の連続性、局所 Hölder 連続性 | 構成の主要ファイルに直接の `sorry` はない |
| Kolmogorov–Chentsov の定理 | 被覆数の条件と増分のモーメント評価から Hölder 連続な修正の存在 | 対応する `Continuity/` のファイルに直接の `sorry` はない |
| 反射原理、重複対数の法則 | 反射原理の命題と重複対数の法則の証明コード | 反射原理とガウス裾評価に `sorry` があり、後続の法則も依存する |
| Doob–Meyer 分解 | class D・class DL の分解定理、局所版の宣言 | class D・DL 版に証明コードがあるが、補助理論に未証明箇所がある。局所版は直接 `sorry` |
| 二乗可積分マルチンゲール | 商空間、内積、連続部分・純不連続部分への分解 | 極限や安定性などの基礎補題に `sorry` がある |
| 予測可能二次変分 | Doob–Meyer 分解による定義と性質 | 未証明の局所 Doob–Meyer 定理に依存する |
| 確率積分 | 単純過程の積分、一般の積分が満たす性質の定義 | 一般の積分の存在を構成する定理とは区別が必要 |
| Itô の公式 | この版の `BrownianMotion/` 内に対応する定理は見当たらない | リポジトリの開発目標 |

宣言自身の証明に `sorry` がなくても、利用する補題が未証明なら結果も未証明部分に依存する。表の「直接の `sorry` はない」は、依存先を含む無公理性やビルド成功を意味しない。

## 対象版と利用環境

対象は外部ワークスペース `/Users/tamura/src/github/brownian-motion` のコミット `a7ad7af662044313bc80a7c0756360fb3745f931` である。対象版の Lean は `v4.33.0-rc1`、依存する mathlib のリビジョンは `0434c03386d3e7f7fd3ed95754543eabe4ab251b` である。ライブラリの定理名や証明の完成状況は版によって変わる。

`BrownianMotion.Gaussian.BrownianMotion` などは外部ライブラリのモジュール名である。この日本語リファレンスの Lake 設定は Brownian Motion を依存関係として含まず、Lean の固定版も異なるため、Brownian Motion の宣言を使う場合は対象ライブラリ側のプロジェクトが必要になる。

## mathlib と外部ライブラリの境界

`IsPreBrownianReal`、`IsBrownianReal`、`IsGaussianProcess`、`HasIndepIncrements` などの基本概念は、対象版では mathlib からインポートされている。Brownian Motion 側は、それらを使った具体的な構成や追加定理を提供する。Kolmogorov 拡張定理は別の依存ライブラリ `kolmogorov_extension4` を利用する。

記事の Lean 欄は、名前や型・命題の読み方を示す。`ProbabilityTheory` の宣言が多いが、停止時刻やフィルトレーションには `MeasureTheory`、ジャンプには `Function` の宣言もある。`IsCadlag` など、名前空間に入っていない宣言もある。

[リファレンスのトップ](../../README.md)
