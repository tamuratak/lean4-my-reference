# 有限台関数

無限個の添字を使っていても、各ベクトルの展開や多項式に現れる非零の係数は有限個でよい。このような「非零の値を取る添字が有限個の関数」を有限台関数という。

$$
\operatorname{supp}(c)=\{i\mid c_i\ne0\},\qquad
\operatorname{supp}(c)\text{ は有限}.
$$

## 関数と有限台関数の違い

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 通常の係数の関数 | $(c_i)_{i\in\iota}$ | `c : ι → ℝ` |
| 有限台の係数 | 非零係数が有限個 | `c : ι →₀ ℝ` または `Finsupp ι ℝ` |
| 第 $i$ 係数 | $c_i$ | `c i` |
| 台 | $\operatorname{supp}(c)$ | `c.support : Finset ι` |
| 通常の関数として見る | 添字から係数を返す | `(c : ι → ℝ)` |

`ι →₀ ℝ` の下付きの零は、値がすべて零という意味ではない。関数の値と、非零になる場所を正確に列挙した有限集合を持つ。一般の値域 `M` でも零があれば `Finsupp ι M` を作れる。

例えば $c_2=7$、それ以外は $0$ という係数は、添字が自然数全体でも有限台であり、台は $\{2\}$。自然数の定数列 $c_n=1$ は非零の添字が無限個なので、有限台関数にはならない。

## 一つの係数と有限和

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 一つの添字だけに係数を置く | $c_i=a$、他は $0$ | `Finsupp.single i a` |
| 有限台関数の和 | $(c+d)_i=c_i+d_i$ | `c + d` |
| 係数のスカラー倍 | $(ac)_i=ac_i$ | `a • c` |
| 台に沿う有限和 | $\sum_{i\in\operatorname{supp}(c)}H(i,c_i)$ | `c.sum (fun i a => H i a)` |

`Finsupp.single i 0` の台は空集合。和の台も、相殺があるため二つの台の和集合と必ず一致するわけではない。

```lean
import Mathlib.Data.Finsupp.Basic

variable (c : ℕ →₀ ℤ)

#check (c.sum (fun _ a => a) : ℤ)

example : (Finsupp.single (2 : ℕ) (7 : ℤ)) 2 = 7 := by
  simp

example : (Finsupp.single (2 : ℕ) (7 : ℤ)) 3 = 0 := by
  simp

example : (Finsupp.single (2 : ℕ) (7 : ℤ)).support = {2} := by
  simp
```

`c.sum H` は台の上の和なので、`H i 0` が零でない場合には、台の外の項を加えた別の有限和とは一致しない。ベクトルの線形結合なら `H i a = a • b i` であり、零係数の項は零になる。

## 基底の座標で使う理由

一般の代数的な基底 $b=(b_i)_{i\in\iota}$ について、ベクトル $x$ の展開は有限和である。

$$
x=\sum_{i\in\operatorname{supp}(c)}c_i b_i.
$$

| 意味 | Lean |
| --- | --- |
| 一般の基底 | `b : Module.Basis ι ℝ E` |
| ベクトルの座標 | `b.repr x : ι →₀ ℝ` |
| 座標のうち非零の添字 | `(b.repr x).support` |

これにより、基底の添字が無限でも `b.repr x` の展開に必要な項だけを有限和として扱える。無限級数で展開する Hilbert 空間の基底などとは、ここでいう代数的な基底の意味が異なる。

添字が `Fin n` の場合は、普通の座標関数も必ず有限台になる。ただし `Fin n → ℝ` と `Fin n →₀ ℝ` は別の型であり、同じ値を表せても自動的に型が一致するわけではない。

関連：[基底と座標](matrices_basis.md#基底と座標)、[有限和と級数](sequences_series.md)、[構造を持つ写像](structured_objects.md)。共通の構文：[公式リファレンス：関数](https://lean-lang.org/doc/reference/latest/The-Type-System/Functions/)。

[mathlib の索引に戻る](README.md)
