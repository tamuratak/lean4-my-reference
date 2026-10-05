# ノルム・内積・直交性

実内積空間 $E$ では、内積から長さと距離を定める。

$$
\lVert x\rVert=\sqrt{\langle x,x\rangle},\qquad
\operatorname{dist}(x,y)=\lVert x-y\rVert.
$$

以下では `[NormedAddCommGroup E]`・`[InnerProductSpace ℝ E]` を持つ空間を考える。内積がない一般のノルム空間でも、ノルム・距離・作用素ノルムは扱える。

## ノルム・距離・内積

| 意味 | 数学 | Lean |
| --- | --- | --- |
| ノルム | $\lVert x\rVert$ | `‖x‖` または `norm x` |
| 距離 | $\operatorname{dist}(x,y)$ | `dist x y` |
| 実内積 | $\langle x,y\rangle$ | `inner ℝ x y` または `⟪x, y⟫_ℝ` |
| 直交 | $\langle x,y\rangle=0$ | `inner ℝ x y = 0` |
| 単位ベクトル | $\lVert x\rVert=1$ | `‖x‖ = 1` |

`norm x` と `dist x y` は非負の値だが、値の型は `ℝ`。実内積の値も `ℝ` であり、負になることがある。

例えばユークリッド平面で $x=(3,4)$ なら $\lVert x\rVert_2=5$。同じ成分を `Fin 2 → ℝ` に入れた場合、標準ノルムは $\max\{3,4\}=4$ になる。**内積の数式を使うときは `EuclideanSpace ℝ (Fin n)` など、意図した内積を持つ型を選ぶ。**

複素内積では `inner ℂ x y` は複素数であり、実内積と区別する。mathlib の複素内積は第一引数に共役線形、第二引数に線形である。

## 正規直交族と正規直交基底

$$
\langle v_i,v_j\rangle=\begin{cases}1&i=j,\\0&i\ne j.\end{cases}
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| ベクトル族 | $(v_i)_{i\in\iota}$ | `v : ι → E` |
| 正規直交族 | 各 $v_i$ のノルムが $1$、異なる項は直交 | `Orthonormal ℝ v` |
| 有限の正規直交基底 | 正規直交かつ全空間を生成 | `b : OrthonormalBasis ι ℝ E` |
| 基底ベクトル | $b_i$ | `b i` |
| 正規直交基底での座標 | $\langle b_i,x\rangle$ | `b.repr x i` |

正規直交族だけでは、全空間を生成するとは限らない。有限添字の `OrthonormalBasis` はその生成性も含み、各座標を内積で取り出せる。一般の基底の `Module.Basis.repr` と違い、その座標は `EuclideanSpace ℝ ι` に入る。

## 作用素ノルム

連続線形写像 $A:E\to F$ の作用素ノルムは、入力の長さに対して出力がどれだけ大きくなるかを表す。すべての $v$ について次の評価を満たす、最小の非負定数である。

$$
\lVert A(v)\rVert\le\lVert A\rVert\lVert v\rVert.
$$

| 意味 | Lean |
| --- | --- |
| 連続線形写像の型 | `A : E →L[ℝ] F` |
| 作用素ノルムの値 | `‖A‖` |
| 作用素ノルムによる評価 | `A.le_opNorm v` |
| 内積の Cauchy–Schwarz の評価 | `norm_inner_le_norm` |

`‖A‖` は写像全体のノルム、`‖A v‖` は特定の入力に対する出力のノルム。行列の成分を並べた型の標準ノルムを、作用素ノルムと同一視しない。

```lean
import Mathlib.Analysis.InnerProductSpace.PiL2

open scoped InnerProductSpace

variable (x y : EuclideanSpace ℝ (Fin 2))
variable (A : EuclideanSpace ℝ (Fin 2) →L[ℝ] ℝ)

#check (⟪x, y⟫_ℝ : ℝ)
#check (dist x y : ℝ)
#check (‖A‖ : ℝ)
#check A.le_opNorm x

variable (b : OrthonormalBasis (Fin 2) ℝ (EuclideanSpace ℝ (Fin 2)))
variable (v : Fin 2 → EuclideanSpace ℝ (Fin 2))

#check (Orthonormal ℝ v : Prop)
#check (b.repr x : EuclideanSpace ℝ (Fin 2))
#check (b.repr x 0 : ℝ)
```

関連：[空間と標準ノルム](spaces.md#ユークリッド空間とノルム)、[基底](matrices_basis.md#基底と座標)、[勾配](partial_gradient.md#勾配)。共通の構文：[公式リファレンス：型クラス](https://lean-lang.org/doc/reference/latest/Type-Classes/)。

[mathlib の索引に戻る](README.md)
