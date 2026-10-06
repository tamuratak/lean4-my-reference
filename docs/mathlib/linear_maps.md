# 連続線形写像とヤコビアン

$f:\mathbb{R}^n\to\mathbb{R}^m$ の全微分は、点の変化 $h$ を出力の一次の変化へ送る線形写像である。

$$
Df(x):\mathbb{R}^n\to\mathbb{R}^m.
$$

そのため `fderiv ℝ f x` の値は数や行列そのものではなく、連続線形写像になる。

## 線形写像の型と正式名

実線形写像 $A:E\to F$ は、

$$
A(u+v)=A(u)+A(v),\qquad A(cu)=cA(u)
\quad(c\in\mathbb{R})
$$

を満たす写像である。

| 意味 | Lean の型 | ASCII の正式名による表記 |
| --- | --- | --- |
| 通常の関数 | `E → F` | `E -> F` |
| 実線形写像 | `E →ₗ[ℝ] F` | `LinearMap (RingHom.id Real) E F` |
| 実連続線形写像 | `E →L[ℝ] F` | `ContinuousLinearMap (RingHom.id Real) E F` |

`LinearMap` は関数と線形性の証明をまとめた型。`ContinuousLinearMap` はさらに連続性も含む。`RingHom.id Real` はスカラーの実数をそのまま使う指定である。ここでは独自の略記を導入せず、この固定バージョンの正式名を併記している。

これらの値を普通の関数として適用できる理由と、備わる証明の使い方は[構造を持つ集合・写像](structured_objects.md#関数と性質を備えた写像)を参照。

有限次元の実ノルム空間では線形写像は連続だが、一般の無限次元空間では連続性を別に要求する。mathlib の全微分は一般のノルム空間にも適用できるため、連続線形写像を使う。

## 線形写像に対する操作

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 方向に適用する | $A(h)$ | `A h` |
| 写像の和 | $(A+B)(h)=A(h)+B(h)$ | `A + B` |
| 写像のスカラー倍 | $(cA)(h)=cA(h)$ | `c • A` |
| 写像の合成 | $(B\circ A)(h)=B(A(h))$ | `B.comp A` |
| 第 $j$ 標準基底ベクトル | $e_j$ | `Pi.single j 1`（座標関数の型） |

例えば $f(x,y)=xy$ の全微分は、

$$
Df(x,y)(u,v)=yu+xv.
$$

`fderiv ℝ f (x, y)` が写像全体、`fderiv ℝ f (x, y) (u, v)` がその方向への適用を表す。

## ヤコビアン行列

全微分可能な $f:\mathbb{R}^n\to\mathbb{R}^m$ のヤコビアンは、全微分を標準基底で表示した $m\times n$ 行列である。

$$
J_f(x)_{ij}
=\frac{\partial f_i}{\partial x_j}(x)
=\bigl(Df(x)(e_j)\bigr)_i.
$$

`f : (Fin n → ℝ) → (Fin m → ℝ)`、`x : Fin n → ℝ` とすると、次の対応になる。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 行列の型 | $\mathbb{R}^{m\times n}$ | `Matrix (Fin m) (Fin n) ℝ` |
| ヤコビアンの成分 | $J_f(x)_{ij}$ | `fderiv ℝ f x (Pi.single j 1) i` |
| ヤコビアンの全成分を並べる | $J_f(x)$ | `fun i j => fderiv ℝ f x (Pi.single j 1) i` |

行は出力の座標、列は入力の座標である。表の最後の式は成分を並べる表現であって、新しい mathlib の宣言名ではない。一般の基底で線形写像を行列表示する道具には `LinearMap.toMatrix` がある。

関連：[行列と基底](matrices_basis.md)、[作用素ノルム](norms_inner_products.md#作用素ノルム)、[全微分](fderiv.md)、[変数変換](change_variables.md)。共通の構文：[公式リファレンス：構造体](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

[mathlib の索引に戻る](README.md)
