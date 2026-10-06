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

同じ成分を別のノルムで扱う仕組みは[WithLp](with_lp.md)、距離から得られる一様構造と完備性は[一様空間と完備性](uniform_spaces.md)を参照。

## 係数体を表す変数名

ベクトル空間のスカラーとして使う体を、数学では $\mathbb{k}$ や $K$ と書く。mathlib の解析では、この**係数体を表す変数名として `𝕜` がよく使われる**。

`𝕜` は命名の慣習であり、特定の体を表すライブラリの定数や専用の記法ではない。`K` などの名前でも同じ役割を表せる。`ℝ` が定義済みの型 `Real`、`ℂ` が `Complex` を指すのに対し、`𝕜` はその箇所で宣言された変数を指す。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 係数体として使う型を宣言する | $\mathbb{k}$ | `𝕜 : Type*` |
| 体の構造を仮定する | $\mathbb{k}$ は体 | `[Field 𝕜]` |
| 非自明なノルムを持つ体 | ノルム体 $\mathbb{k}$、ある元のノルムが $1$ を超える | `[NontriviallyNormedField 𝕜]` |
| 係数体の完備性 | $\mathbb{k}$ は完備 | `[CompleteSpace 𝕜]` |
| 係数体の標数 | $\operatorname{char}(\mathbb{k})=0$ | `[CharZero 𝕜]` |
| その体上のノルム空間 | $E$ は $\mathbb{k}$ 上のノルム空間 | `[NormedAddCommGroup E] [NormedSpace 𝕜 E]` |

**名前ではなく、型クラスの仮定から体の条件を読む**。`𝕜 : Type*` だけでは体であることさえ仮定していない。例えば、解析の定理の前に次の宣言があれば、非自明なノルムを持つ完備な標数ゼロの体を扱う。

```text
variable {𝕜 : Type*} [NontriviallyNormedField 𝕜]
  [CompleteSpace 𝕜] [CharZero 𝕜]
```

実数体 $\mathbb{R}$ と複素数体 $\mathbb{C}$ はこの条件を満たす代表例だが、この仮定は二つの体に限定していない。宣言は定理の直前だけでなく、ファイルや `section` の前の方に置かれていることもある。

係数体を明示する式も、この変数名を使って読む。

| 数学の意味 | Lean |
| --- | --- |
| $\mathbb{k}$ 上の全微分 | `fderiv 𝕜 f x` |
| $\mathbb{k}$ をスカラーとする点 $x$ での解析性 | `AnalyticAt 𝕜 f x` |

ここで最初の引数は、微分や解析性をどの体上で考えるかを指定する。具体的に実数を指定する `fderiv ℝ f x` も同じ形であり、`𝕜` と書いたこと自体が新たな数学の操作を表すわけではない。

共通の構文：[公式リファレンス：識別子](https://lean-lang.org/doc/reference/latest/Terms/Identifiers/)、[型クラス](https://lean-lang.org/doc/reference/latest/Type-Classes/)。これらは変数名と仮定の仕組みの説明であり、mathlib の命名慣習や数学の API の説明とは区別する。

## 解析性

`AnalyticAt 𝕜 f x` は、関数 `f : E → F` が点 $x$ の近傍で、$\mathbb{k}$ 上の収束する冪級数展開を持つという命題である。一変数のスカラー値関数なら、ある正の半径の範囲で

$$
f(x+h)=\sum_{k=0}^{\infty}a_k h^k
$$

と表せることに対応する。一般のノルム空間では、係数を連続多重線形写像の列 `p : FormalMultilinearSeries 𝕜 E F` として持ち、第 $k$ 項は `p k (fun _ : Fin k => h)` となる。

`HasFPowerSeriesAt f p x` は指定した級数 `p` が近傍で `f` に収束する条件、`AnalyticAt 𝕜 f x` はそのような `p` の存在を表す。すべての有限階で微分可能というだけでは、元の関数に収束する冪級数展開を持つとは限らない。`ContDiff … ω …` との対応と、一点での同値に必要な値域の完備性は[高階微分と滑らかさ](higher_derivatives.md#連続微分可能性)を参照。

## 一般のノルム空間

mathlib の全微分は有限次元に限定されない。定理に出てくる一般の空間 $E$ は、主に次の型クラスで条件を表す。

| 数学の条件 | Lean |
| --- | --- |
| ノルムを持つ加法の空間 | `NormedAddCommGroup E` |
| 実ノルム空間 | 上の条件と `NormedSpace ℝ E` |
| 実内積空間 | 上の加法の条件と `InnerProductSpace ℝ E` |
| 完備な空間 | `CompleteSpace E` |

関連：[ノルム・内積・直交性](norms_inner_products.md)、[行列と基底](matrices_basis.md)、[線形写像](linear_maps.md)、[偏微分と勾配](partial_gradient.md)。共通の構文：[公式リファレンス：型クラス](https://lean-lang.org/doc/reference/latest/Type-Classes/)。

[mathlib の索引に戻る](README.md)
