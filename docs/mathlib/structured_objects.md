# 構造を持つ集合・写像

数学では、部分空間も集合として扱い、線形写像も関数として適用する。mathlib では、集合や関数に必要な性質の証明をまとめた型を作り、用途に応じて集合・関数・要素の型として使う。

## 集合と部分空間と要素の型

実ベクトル空間 $E$ の部分空間 $S$ は、零・加法・実数のスカラー倍について閉じた部分集合である。以下では `[AddCommGroup E]`・`[Module ℝ E]` を持つ空間を考える。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 単なる部分集合 | $s\subseteq E$ | `s : Set E` |
| 部分空間の構造 | $S\subseteq E$、演算について閉じる | `S : Submodule ℝ E` |
| 部分空間の点の所属 | $x\in S$ | `x ∈ S` |
| 集合としての部分空間 | 閉性の構造を忘れて集合を見る | `(S : Set E)` |
| 部分空間に属する点の型 | $\{x\in E\mid x\in S\}$ | `↥S`（型が必要な場所では `S` とも書ける） |
| 部分空間の点を周囲の空間で使う | $x\in S$ を $E$ の点として見る | `(x : E)`（`x : S`） |

`S : Submodule ℝ E` は部分空間そのもの、`x : S` はその部分空間の点。`x : S` は値と所属の証明を持つ部分型であり、`x.property` で `(x : E) ∈ S` を得られる。

単なる集合 `s : Set E` からも要素の型 `↥s` を作れるが、一般の集合にはベクトル空間の演算があるとは限らない。`Submodule` では閉性の証明があるため、部分空間の点同士の和やスカラー倍をその型の中で扱える。

```lean
import Mathlib.Algebra.Module.Submodule.LinearMap
import Mathlib.Basic.Real.Basic

variable (S : Submodule ℝ ℝ) (x y : S)

#check (S : Set ℝ)
#check (x + y : S)
#check (x : ℝ)

example : (x : ℝ) ∈ S := x.property
```

## 関数と、性質を備えた写像

| 対象 | 数学の条件 | Lean の型 |
| --- | --- | --- |
| 関数 | 入力から出力を返す | `E → F` |
| 線形写像 | 加法とスカラー倍を保つ | `E →ₗ[ℝ] F` |
| 連続線形写像 | 線形かつ連続 | `E →L[ℝ] F` |
| 線形同値 | 線形な可逆写像 | `E ≃ₗ[ℝ] F` |
| 連続線形同値 | 線形同値で、写像と逆写像が連続 | `E ≃L[ℝ] F` |

例えば `A : E →ₗ[ℝ] F` に対して `A x` と書けるのは、関数として使う強制変換が用意されているため。`A` には関数だけでなく、線形性の証明も含まれる。

| 意味 | Lean |
| --- | --- |
| 普通の関数として見る | `(A : E → F)` |
| 加法を保つという証明 | `A.map_add x y` |
| 連続線形写像から線形写像を取り出す | `A.toLinearMap`（`A : E →L[ℝ] F`） |
| 線形同値の逆写像 | `e.symm`（`e : E ≃ₗ[ℝ] F`） |

「線形写像である」を命題として述べるだけの表現と違い、線形写像の値を受け取れば、その値に備わる証明を使える。逆に、普通の関数から線形写像を作るには、線形性を証明して構造を組み立てる必要がある。

```lean
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Basic.Real.Basic

example (A : ℝ →ₗ[ℝ] ℝ) (x y : ℝ) :
    A (x + y) = A x + A y := A.map_add x y
```

## 型クラスとの役割の違い

`[Module ℝ E]` は型 $E$ にベクトル空間の演算・法則を指定する。`A : E →ₗ[ℝ] F` は、その空間同士の特定の線形写像を表す。同様に、`S : Submodule ℝ E` は特定の部分空間であり、`E` に部分空間の型クラスを付けているわけではない。

mathlib の定理を読むときは、型全体の構造を指定する角括弧の引数と、特定の集合・写像を受け取る引数を分けて読むと理解しやすい。

関連：[行列と基底](matrices_basis.md)、[連続線形写像](linear_maps.md)。共通の仕組み：[部分型](../syntax/subtype.md)、[型クラス](../syntax/class.md)、[公式リファレンス：Coercions](https://lean-lang.org/doc/reference/latest/Coercions/)。

[mathlib の索引に戻る](README.md)
