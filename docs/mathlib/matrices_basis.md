# 行列・基底・線形代数

行列 $M\in\mathbb{R}^{m\times n}$ は、行と列の番号から成分を返す関数 `Matrix (Fin m) (Fin n) ℝ` で表す。線形写像を行列で表示するには、入力・出力の基底を決める。

## 行列とベクトルの積

$$
(Mx)_i=\sum_{j=0}^{n-1}M_{ij}x_j,\qquad
(MN)_{ik}=\sum_{j=0}^{n-1}M_{ij}N_{jk}.
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 行列 | $M\in\mathbb{R}^{m\times n}$ | `M : Matrix (Fin m) (Fin n) ℝ` |
| 成分 | $M_{ij}$ | `M i j` |
| 列ベクトルとの積 | $Mx$ | `M *ᵥ x` または `Matrix.mulVec M x` |
| 行列積 | $MN$ | `M * N` |
| 転置 | $M^{\mathsf T}$ | `Mᵀ` または `Matrix.transpose M` |
| 単位行列 | $I_n$ | `(1 : Matrix (Fin n) (Fin n) ℝ)` |
| 行列式 | $\det M$（正方行列） | `Matrix.det M` |

行列積には内側の添字の型が一致することと、その型が有限であることが必要。`M * N` は成分ごとの積ではない。`Matrix` 自体は関数の型の別名だが、積は行列の演算として定義される。

例えば $M=\begin{pmatrix}1&2\\3&4\end{pmatrix}$、$x=(5,6)$ なら $Mx=(17,39)$。次の例では整数の行列を計算する。

```lean
import Mathlib.LinearAlgebra.Matrix.Notation

open scoped Matrix

def M : Matrix (Fin 2) (Fin 2) ℤ := !![1, 2; 3, 4]
def x : Fin 2 → ℤ := ![5, 6]

#eval M *ᵥ x
```

## 基底と座標

基底 $b=(b_i)$ を使うと、ベクトルを $x=\sum_i c_i b_i$ と表せる。以下では、`E` は `[AddCommGroup E]`・`[Module ℝ E]` を持つ実ベクトル空間とする。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 添字 $\iota$ を持つ基底 | $(b_i)_{i\in\iota}$ | `b : Module.Basis ι ℝ E` |
| 基底ベクトル | $b_i$ | `b i` |
| 基底 $b$ に関する座標 | $(c_i)$ | `b.repr x` |
| 第 $i$ 座標 | $c_i$ | `b.repr x i` |
| 座標空間の標準基底 | $e_j$ | `Pi.basisFun ℝ (Fin n)` |
| ベクトル族の線形独立性 | $(v_i)$ は線形独立 | `LinearIndependent ℝ v` |
| ベクトル集合の線形包 | $\operatorname{span}(s)$ | `Submodule.span ℝ s` |

`b.repr x` の値は有限台関数 `ι →₀ ℝ`。一般の基底では添字が無限でも、各ベクトルの展開に現れる非零の係数は有限個になる。単にベクトル族を与える `v : ι → E` と、独立性・生成性を備えた基底は区別する。

有限台の意味と係数の操作は[有限台関数](finitely_supported.md)を参照。

## 行列と線形写像の対応

入力の基底を `bE`、出力の基底を `bF` とすると、行列の第 $j$ 列は $A(bE_j)$ の出力座標になる。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 行列から座標上の線形写像 | $x\mapsto Mx$ | `M.mulVecLin` |
| 基底を指定した行列表示 | $[A]_{bF\leftarrow bE}$ | `LinearMap.toMatrix bE bF A` |
| 行列から基底を指定した写像 | $A$ を復元 | `Matrix.toLin bE bF M` |
| 核 | $\{x\mid A(x)=0\}$ | `LinearMap.ker A` |
| 像 | $\{A(x)\mid x\in E\}$ | `LinearMap.range A` |

`LinearMap.ker A` と `LinearMap.range A` は `Submodule`、つまり部分空間の構造を持つ。普通の集合としての像 `A '' s` とは型が異なる。行列表示は基底によって変わるが、写像そのものは変わらない。

部分空間を集合や要素の型として使う仕組みは[構造を持つ集合・写像](structured_objects.md)を参照。

```lean
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.Basic.Real.Basic

variable (M : Matrix (Fin 2) (Fin 2) ℝ)

#check (M.mulVecLin : (Fin 2 → ℝ) →ₗ[ℝ] (Fin 2 → ℝ))
#check LinearMap.toMatrix (Pi.basisFun ℝ (Fin 2))
  (Pi.basisFun ℝ (Fin 2)) M.mulVecLin
#check LinearMap.ker M.mulVecLin
#check LinearMap.range M.mulVecLin
#check Matrix.toLin (Pi.basisFun ℝ (Fin 2))
  (Pi.basisFun ℝ (Fin 2)) M

variable (b : Module.Basis (Fin 2) ℝ (Fin 2 → ℝ))
variable (x : Fin 2 → ℝ)

#check (b.repr x : Fin 2 →₀ ℝ)
#check (b.repr x 0 : ℝ)
```

関連：[連続線形写像とヤコビアン](linear_maps.md)、[高階微分と Hessian](higher_derivatives.md)、[ノルムと内積](norms_inner_products.md)。共通の構文：[公式リファレンス：構造体](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

[mathlib の索引に戻る](README.md)
