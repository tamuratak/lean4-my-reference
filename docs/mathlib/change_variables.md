# 変数変換とヤコビアンの行列式

座標変換 $\Phi:E\to E$ によって領域 $s$ を $\Phi(s)$ に移すと、体積の倍率は全微分の行列式の絶対値になる。

$$
\int_{\Phi(s)}g(y)\,dy
=\int_s\lvert\det D\Phi(x)\rvert\,g(\Phi(x))\,dx.
$$

ここでは $E$ は有限次元の実空間。Lean では変換を `phi`、各点の微分を `A`、被積分関数を `g` とする。

## 領域・微分・体積の倍率

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 変換する領域 | $s\subseteq E$ | `s : Set E` |
| 座標変換 | $\Phi:E\to E$ | `phi : E → E` |
| 変換後の領域 | $\Phi(s)$ | `phi '' s` または `Set.image phi s` |
| 各点で指定した全微分 | $A(x)=D\Phi(x)$ | `A x`（連続線形自己写像） |
| 領域内で全微分が $A(x)$ | $s$ 内の増分で微分が $A(x)$ | `HasFDerivWithinAt phi (A x) s x` |
| 行列式 | $\det A(x)$ | `(A x).det` |
| 体積の倍率 | $\lvert\det A(x)\rvert$ | `abs ((A x).det)` |
| 変換後の被積分関数 | $g(\Phi(x))$ | `g (phi x)` |
| 倍率を含む被積分関数 | $\lvert\det A(x)\rvert\,g(\Phi(x))$ | `abs ((A x).det) • g (phi x)` |

`.det` は連続線形自己写像の行列式であり、座標表示すればヤコビアン行列の行列式に対応する。入力と出力が同じ有限次元なので正方の行列になる。`•` はスカラー倍で、ベクトル値の被積分関数にも使える。

## 変数変換の条件

主要な定理は `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul`。次の条件を表現する。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 領域が可測 | $s$ は可測集合 | `MeasurableSet s` |
| 領域の各点で指定した微分を持つ | $\forall x\in s,\ D_s\Phi(x)=A(x)$ | `∀ x ∈ s, HasFDerivWithinAt phi (A x) s x` |
| 領域上で単射 | $\Phi(x)=\Phi(y)\Rightarrow x=y$（$x,y\in s$） | `Set.InjOn phi s` |

微分の条件には存在も含む。一般形では Borel 可測構造 `[MeasurableSpace E] [BorelSpace E]` と、測度 `μ : Measure E` に対する `[μ.IsAddHaarMeasure]` を仮定する。正式名は `MeasureTheory.Measure.IsAddHaarMeasure μ` である。

この加法 Haar 測度の条件は、平行移動で測度が変わらないこと、コンパクト集合の測度が有限であること、空でない開集合の測度が正であることをまとめている。例えば $s$ を $a$ だけ平行移動しても $\mu(a+s)=\mu(s)$ となる。有限次元の実空間で使う体積測度がこの条件に対応し、標準のユークリッド空間では `volume` がそのインスタンスを持つ。可測構造と `volume` の指定は[測度の型クラス](measure_integrals.md#可測構造と既定の測度)を参照。

結論の積分値の等式は、Lean の表現では次の形になる。

```text
(∫ y in phi '' s, g y ∂μ) =
  ∫ x in s, abs ((A x).det) • g (phi x) ∂μ
```

`μ` に `volume` を使うときは、両辺の `∂μ` を省略した表記になる。

この定理には可積分性の仮定が直接現れない。非可積分な場合にも積分が定義されるためである。有限な積分値の評価に使う場合は、可積分性を別に確認する。単射性は、領域を重複して数えないための条件である。

## 極座標との対応

平面の極座標変換は、

$$
\Phi(r,\theta)=(r\cos\theta,r\sin\theta),
\qquad
\det D\Phi(r,\theta)=r.
$$

| 意味 | 数学 | Lean の表現 |
| --- | --- | --- |
| 極座標の点 | $(r,\theta)$ | `p : ℝ × ℝ` |
| 平面の点へ変換 | $(r\cos\theta,r\sin\theta)$ | `(p.1 * Real.cos p.2, p.1 * Real.sin p.2)` |
| 体積要素（$r>0$） | $dx\,dy=r\,dr\,d\theta$ | 微分の行列式の絶対値が半径になる |

$r=0$ では角度によらず同じ点になる。また角度には周期がある。そのため、極座標を使う領域は半径と角度の範囲を決め、単射性を満たすように扱う必要がある。必要に応じて、境界や例外集合を除いても積分が変わらないことを使う。

関連：[全微分](fderiv.md)、[ヤコビアン](linear_maps.md)、[領域上の積分](measure_integrals.md)。

[mathlib の索引に戻る](README.md)
