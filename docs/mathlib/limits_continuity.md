# 領域・極限・連続性

関数 $f:E\to F$ の極限や微分を表すには、点 $x$ だけでなく、「どの領域から近づくか」を指定する。

## 領域

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 領域 | $s\subseteq E$ | `s : Set E` |
| 点が領域に属する | $x\in s$ | `x ∈ s` |
| 閉区間 | $[a,b]$ | `Set.Icc a b` |
| 開区間 | $(a,b)$ | `Set.Ioo a b` |
| 半開区間 | $(a,b]$ | `Set.Ioc a b` |
| 端点の順序によらない閉区間 | $[\min(a,b),\max(a,b)]$ | `Set.uIcc a b` |
| 長方形・積領域 | $s\times t$ | `s ×ˢ t` または `Set.prod s t` |
| 開球 | $\{y\mid\operatorname{dist}(y,x)<r\}$ | `Metric.ball x r` |
| 閉球 | $\{y\mid\operatorname{dist}(y,x)\le r\}$ | `Metric.closedBall x r` |

`Set E` は要素の型ではなく、部分集合の型である。例えば点は `x : E`、領域は `s : Set E`、所属条件は命題 `x ∈ s` となる。

## 極限と近傍

$$
\lim_{z\to x}f(z)=y
$$

は `Filter.Tendsto f (nhds x) (nhds y)` で表す。`nhds x` は点 $x$ の近傍フィルターであり、「$x$ に近づく」という条件をまとめたもの。

フィルター自体の意味と、`Tendsto` の入力側・出力側の読み方は[フィルターと極限](filters.md)を参照。上の表現では点 $x$ 自身も含むため、点を除く通常の関数の極限には、下の穴あき近傍を使う。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 点への極限 | $\lim_{z\to x}f(z)=y$ | `Filter.Tendsto f (nhds x) (nhds y)` |
| 列の極限 | $\lim_{k\to\infty}u_k=y$ | `Filter.Tendsto u Filter.atTop (nhds y)` |
| 領域内から近づく | $z\to x,\ z\in s$ | `nhdsWithin x s` |
| 点自身を除いて近づく | $z\to x,\ z\ne x$ | `nhdsWithin x {x}ᶜ` |

近傍の記法 `𝓝 x`、`𝓝[s] x` は、それぞれ正式名 `nhds x`、`nhdsWithin x s` に対応する。通常の極限と穴あき近傍での極限は区別する。微分の差商では点自身を除く。

## 連続性

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 点で連続 | $\lim_{z\to x}f(z)=f(x)$ | `ContinuousAt f x` |
| 領域内から見て連続 | $\lim_{z\to x,\ z\in s}f(z)=f(x)$ | `ContinuousWithinAt f s x` |
| 領域上で連続 | $s$ の各点で領域内から見て連続 | `ContinuousOn f s` |
| 全空間で連続 | すべての点で連続 | `Continuous f` |

`ContinuousOn f s` は、$x\in s$ の各点で `ContinuousWithinAt f s x` が成り立つという命題。境界では領域の内側からの連続性を表し、領域外の振る舞いは要求しない。

例えば $s=[0,\infty)$ なら、境界 $x=0$ では右側からの連続性を調べる。開領域の内部なら、領域内の近傍と通常の近傍が一致し、通常の点での連続性と対応する。

関連：[開集合・閉集合・コンパクト性](topology_compactness.md)、[数列と級数](sequences_series.md)、[関数列の収束](function_sequences.md)、[領域内の全微分](fderiv.md)、[可測性と積分](measure_integrals.md)。共通の構文：[公式リファレンス：関数](https://lean-lang.org/doc/reference/latest/The-Type-System/Functions/)。

[mathlib の索引に戻る](README.md)
