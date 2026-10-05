# 数列・有限和・級数

実数列 $u_0,u_1,\ldots$ は `u : ℕ → ℝ` で表す。数列自体の極限と、その項を足した部分和の極限は別の対象である。

## 数列と部分和

$$
u_n\longrightarrow a,\qquad S_N=\sum_{n=0}^{N-1}u_n.
$$

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 実数列 | $(u_n)_{n\in\mathbb{N}}$ | `u : ℕ → ℝ` |
| 第 $n$ 項 | $u_n$ | `u n` |
| 数列の収束 | $u_n\to a$ | `Filter.Tendsto u Filter.atTop (nhds a)` |
| 最初の $N$ 項の添字 | $\{0,\ldots,N-1\}$ | `Finset.range N` |
| 部分和 | $S_N$ | `∑ n ∈ Finset.range N, u n` |
| 部分和の収束 | $S_N\to a$ | `Filter.Tendsto (fun N => ∑ n ∈ Finset.range N, u n) Filter.atTop (nhds a)` |

`Finset.range N` は $N$ を含まない。$N=0$ の部分和は空の和なので $0$ になる。`Finset` は有限集合のデータであり、一般の部分集合 `Set` とは異なる。

例えば $u_n=n$、$N=4$ の部分和は $0+1+2+3=6$。次の例では計算可能な自然数の有限和を使う。

```lean
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

open scoped BigOperators

#eval ∑ n ∈ Finset.range 4, n
```

## 無限和の値と収束条件

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 無限和の値 | $\sum_{n=0}^{\infty}u_n$ | `∑' n, u n` または `tsum u` |
| 和が存在し、値が $a$ | $\sum_n u_n=a$、かつ無条件収束 | `HasSum u a` |
| 和が存在する | 無条件収束する | `Summable u` |
| 絶対収束の条件 | $\sum_n\lvert u_n\rvert<\infty$ | `Summable (fun n => ‖u n‖)` |

`Summable u` は、ある `a` について `HasSum u a` が成り立つという命題。実数値では通常の絶対収束と対応する。`tsum u` は収束条件を満たさない場合も定義され、その場合は $0$ になる。したがって、`tsum u = 0` だけでは収束を主張できない。

例えば $u_n=r^n$、$\lvert r\rvert<1$ の幾何級数では、数学的には和が $1/(1-r)$ である。この値と収束をまとめた表現は `HasSum (fun n : ℕ => r ^ n) (1 / (1 - r))` になる。

## 項の順序を固定した収束

**既定の `HasSum` は、最初の $N$ 項だけでなく、すべての有限部分集合に沿う和の収束を表す。** 実数の条件収束級数は、部分和が収束しても既定の `Summable` を満たさない。

この固定バージョンでは、和を取る方法を `SummationFilter` で指定できる。

| 意味 | Lean |
| --- | --- |
| 自然数の順に足した部分和が $a$ に収束 | `HasSum u a (SummationFilter.conditional ℕ)` |
| その順序で和が存在 | `Summable u (SummationFilter.conditional ℕ)` |
| その順序での和の値 | `∑'[SummationFilter.conditional ℕ] n, u n` |

例えば交代調和級数 $\sum_{n=0}^{\infty}(-1)^n/(n+1)$ は、自然数の順では収束するが絶対収束しない。この区別には、上の指定または部分和の `Tendsto` を使う。

```lean
import Mathlib.Topology.Algebra.InfiniteSum.Defs
import Mathlib.Topology.Instances.Real.Lemmas

open scoped Topology BigOperators

variable (u : ℕ → ℝ) (a : ℝ)

#check (HasSum u a : Prop)
#check (Summable u : Prop)
#check (tsum u : ℝ)
#check (HasSum u a (SummationFilter.conditional ℕ) : Prop)
#check (∑'[SummationFilter.conditional ℕ] n, u n : ℝ)
```

関連：[極限と近傍](limits_continuity.md#極限と近傍)、[関数列と極限の交換](function_sequences.md)。共通の構文：[公式リファレンス：関数](https://lean-lang.org/doc/reference/latest/The-Type-System/Functions/)。

[mathlib の索引に戻る](README.md)
