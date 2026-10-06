# 非負実数・拡張非負実数

測度や非負積分の値は、負にならず、無限大になる場合もある。mathlib は実数とは別に、非負実数 $[0,\infty)$ と拡張非負実数 $[0,\infty]$ の型を用意している。

## 三つの数の型

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 実数 | $\mathbb{R}$ | `ℝ` または `Real` |
| 非負実数 | $[0,\infty)$ | `ℝ≥0` または `NNReal` |
| 拡張非負実数 | $[0,\infty]$ | `ℝ≥0∞` または `ENNReal` |
| 拡張非負実数の無限大 | $\infty$ | `(∞ : ENNReal)` または `(⊤ : ENNReal)` |
| 測度の値 | $\mu(s)\in[0,\infty]$ | `μ s : ENNReal` |

`NNReal` は実数の値と非負性の証明をまとめた部分型。`ENNReal` は `NNReal` に最大値として無限大を加えた型であり、負の値や負の無限大は持たない。

有限の測度と無限の測度を同じ値域で扱えるので、測度を定義する段階では有限性を要求しなくてよい。集合の長さ・面積・体積を表す具体例は[`volume` の説明](measure_integrals.md#volume-と集合の長さ面積体積)を参照。

## 実数との変換

| 意味 | Lean | 条件・振る舞い |
| --- | --- | --- |
| 非負実数を実数として使う | `(a : ℝ)`（`a : NNReal`） | 非負の実数値を取り出す |
| 非負実数を拡張非負実数として使う | `(a : ENNReal)` | 無限大にはならない |
| 実数から拡張非負実数へ | `ENNReal.ofReal r` | 負の入力は $0$ になる |
| 拡張非負実数から実数へ | `a.toReal` | 無限大は $0$ になる |
| 実数から変換して戻す | `(ENNReal.ofReal r).toReal = r` | `0 ≤ r` が必要 |
| 拡張非負実数から変換して戻す | `ENNReal.ofReal a.toReal = a` | `a ≠ ∞` が必要 |

`toReal` は無限大を表現できないため、無限大に対して $0$ を返す。`a.toReal = 0` だけで `a = 0` と判断しない。測度や非負積分の値を実数に移して議論するときは、先に有限性を確認する。

```lean
import Mathlib.Basic.ENNReal.Basic

open scoped ENNReal

example : (∞ : ENNReal).toReal = 0 := ENNReal.toReal_top

example (a : ENNReal) (ha : a ≠ ∞) :
    ENNReal.ofReal a.toReal = a := ENNReal.ofReal_toReal ha

example (r : ℝ) (hr : 0 ≤ r) :
    (ENNReal.ofReal r).toReal = r := ENNReal.toReal_ofReal hr
```

## 演算と成立条件

`ENNReal` は実数の体ではない。無限大を含む加法・乗法に加え、非負の範囲に収める減法などを使う。

| 数学的な規約 | Lean の表現 |
| --- | --- |
| 有限の非負数と無限大の和は無限大 | `a + ∞ = ∞` |
| 零と無限大の積は零 | `(0 : ENNReal) * ∞ = 0` |
| 正の有限数と無限大の積は無限大 | `a * ∞ = ∞`（`a ≠ 0`） |
| 減法は負の値を作らない | `(2 : ENNReal) - 3 = 0` |

例えば無限大を含む和では、`a + c = b + c` から `a = b` と無条件に約分できない。実数で使う演算法則を、そのまま移して使わない。

`∫⁻ x, f x ∂μ` は `ENNReal` 値の非負積分、通常の `∫ x, f x ∂μ` は実数やベクトルの値を返す Bochner 積分。後者の可積分性には、ノルムの非負積分が有限であることが関係する。

関連：[測度と積分](measure_integrals.md)、[条件を持つ値と部分型](structured_objects.md)。部分型の仕組み：[部分型](../syntax/subtype.md)、[公式リファレンス：Subtypes](https://lean-lang.org/doc/reference/latest/Basic-Types/Subtypes/)。

[mathlib の索引に戻る](README.md)
