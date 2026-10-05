# 空間と多変数関数の型

$n$ 次元の点

$$
x=(x_0,\ldots,x_{n-1})\in\mathbb{R}^n
$$

を Lean では `x : Fin n → ℝ` で表す。点を「座標番号を受け取って、その座標の値を返す関数」と考える。

## 点と関数

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 座標番号 | $i\in\{0,\ldots,n-1\}$ | `i : Fin n` |
| 点・ベクトル | $x\in\mathbb{R}^n$ | `x : Fin n → ℝ` |
| 第 $i$ 座標 | $x_i$ | `x i` |
| スカラー値関数 | $f:\mathbb{R}^n\to\mathbb{R}$ | `f : (Fin n → ℝ) → ℝ` |
| ベクトル値関数 | $f:\mathbb{R}^n\to\mathbb{R}^m$ | `f : (Fin n → ℝ) → (Fin m → ℝ)` |
| 出力の第 $j$ 成分 | $f_j(x)$ | `f x j` |
| ベクトルの和 | $x+y$ | `x + y` |
| 実数によるスカラー倍 | $cx$ | `c • x` |

`Fin n` は自然数のうち $n$ 未満の値を持つ型。座標番号は $0$ から始まる。ベクトルの和・スカラー倍は各座標で計算され、`(x + y) i` は `x i + y i` に対応する。

## 二変数のまとめ方

二次元では積型も使える。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 一つの点 | $p=(x,y)\in\mathbb{R}^2$ | `p : ℝ × ℝ` |
| 第一・第二座標 | $x,\ y$ | `p.1`、`p.2` |
| 点を一つ受け取る関数 | $f(x,y)$ | `f : (ℝ × ℝ) → ℝ` |
| 二つの引数を順に受け取る関数 | $g(x,y)$ | `g : ℝ → ℝ → ℝ` |
| 二つの引数を一つの点にまとめる | $f(x,y)=g(x,y)$ | `Function.uncurry g` |

`g x y` と `f (x, y)` は引数の受け取り方が違う。全微分では一つの入力空間を決めるので、複数の変数を一つの点にまとめる表現が基本になる。

## ユークリッド空間とノルム

標準のユークリッド内積を使う空間は `EuclideanSpace ℝ (Fin n)` で表す。

$$
\langle x,y\rangle=\sum_{i=0}^{n-1}x_i y_i,
\qquad
\lVert x\rVert_2=\sqrt{\sum_{i=0}^{n-1}x_i^2}.
$$

| Lean の型 | 標準のノルム | 用途 |
| --- | --- | --- |
| `Fin n → ℝ` | $\max_i\lvert x_i\rvert$（$n>0$） | 座標、偏微分、全微分 |
| `ℝ × ℝ` | $\max\{\lvert x\rvert,\lvert y\rvert\}$ | 二変数、積空間、積測度 |
| `EuclideanSpace ℝ (Fin n)` | $\lVert x\rVert_2$ | 内積、距離、勾配 |

有限次元ではこれらのノルムは同じ位相を与えるが、Lean の型やノルムの値が同じになるわけではない。特に勾配では内積が必要なので、単なる座標関数の型とユークリッド空間の型を区別する。

## 一般のノルム空間

mathlib の全微分は有限次元に限定されない。定理に出てくる一般の空間 $E$ は、主に次の型クラスで条件を表す。

| 数学の条件 | Lean |
| --- | --- |
| ノルムを持つ加法の空間 | `NormedAddCommGroup E` |
| 実ノルム空間 | 上の条件と `NormedSpace ℝ E` |
| 実内積空間 | 上の加法の条件と `InnerProductSpace ℝ E` |
| 完備な空間 | `CompleteSpace E` |

関連：[線形写像](linear_maps.md)、[偏微分と勾配](partial_gradient.md)。共通の構文：[公式リファレンス：型クラス](https://lean-lang.org/doc/reference/latest/Type-Classes/)。

[mathlib の索引に戻る](README.md)
