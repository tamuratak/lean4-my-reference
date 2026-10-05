# フィルターと極限

数列の極限では「添字が十分大きいとき」、関数の極限では「入力がある点に十分近いとき」を考える。**フィルターは、どの集合を「その状況で十分に広い集合」とみなすかをまとめたもの**である。

例えば自然数の上では、ある $N$ 以降の添字をすべて含む集合を使う。実数の点 $a$ の近くでは、ある $\delta>0$ について区間 $(a-\delta,a+\delta)$ を含む集合を使う。集合の大きさは要素数ではなく、このような条件で判断する。

## フィルターは集合の集まり

型 $E$ の上のフィルター $l$ は、$E$ の部分集合の集まりである。Lean では `l : Filter E` と書く。

| 意味 | 数学 | Lean |
| --- | --- | --- |
| 点 | $x\in E$ | `x : E` |
| 部分集合 | $s\subseteq E$ | `s : Set E` |
| フィルター | $l$ は部分集合の集まり | `l : Filter E` |
| 集合がフィルターに属する | $s\in l$ | `s ∈ l` |
| 所属する集合の集まり | $\{s\subseteq E\mid s\in l\}$ | `l.sets : Set (Set E)` |

`x ∈ s` は点の所属、`s ∈ l` は集合の所属。フィルターは一つの領域 `Set E` でも、要素を選別する `List.filter` でもない。

mathlib のフィルターは、次の3条件を持つ。

1. 全空間 $E$ が属する。
2. $s$ が属し、$s\subseteq t$ なら、$t$ も属する。
3. $s$ と $t$ が属するなら、$s\cap t$ も属する。

例えば「ある添字以降をすべて含む」集合を二つ取ると、共通部分も大きい方の添字以降をすべて含む。このため、十分先で成立する二つの条件を同時に扱える。

## 十分先・十分近くで成立する：Eventually

条件 $P$ がフィルター $l$ に沿って eventually 成立するとは、$P$ を満たす点の集合が $l$ に属することである。

$$
\{x\in E\mid P(x)\}\in l.
$$

| 意味 | Lean |
| --- | --- |
| $l$ に沿って eventually $P$ が成立 | `Filter.Eventually P l` |
| 上と同じ命題の記法 | `∀ᶠ x in l, P x` |
| 上と同じ集合の所属条件 | `{x \| P x} ∈ l` |
| eventually 二つの関数が等しい | `f =ᶠ[l] g` または `Filter.EventuallyEq l f g` |

`∀ᶠ` はすべての点で成立する `∀` とは違う。どの範囲を調べるかは `l` によって決まる。

| フィルター | 数学的な読み方 | `∀ᶠ` の意味 |
| --- | --- | --- |
| `(Filter.atTop : Filter ℕ)` | 添字が限りなく大きくなる | ある $N$ 以降、すべての添字で成立 |
| `nhds a` または `𝓝 a` | 点 $a$ の近傍 | ある近傍のすべての点で成立 |
| `nhdsWithin a s` または `𝓝[s] a` | 領域 $s$ 内で点 $a$ に近づく | ある近傍と $s$ の共通部分で成立 |
| `Filter.principal s` または `𝓟 s` | 固定した集合 $s$ | $s$ のすべての点で成立 |

`nhds`・`nhdsWithin` には空間の位相が必要であり、一般には `[TopologicalSpace E]` で指定する。`Filter E` 自体を使うために位相が必要なわけではない。

自然数の `atTop` の場合は、

$$
\text{eventually }P(n)\quad\Longleftrightarrow\quad
\exists N,\ \forall n\ge N,\ P(n).
$$

例えば「十分大きい自然数は $3$ 以上」は次のように書ける。最初の $0,1,2$ で成立する必要はない。

```lean
import Mathlib.Order.Filter.AtTopBot.Basic

example : ∀ᶠ n : ℕ in Filter.atTop, 3 ≤ n := by
  exact Filter.eventually_atTop.mpr ⟨3, fun _ hn => hn⟩
```

実数の `nhds a` なら、「ある $\delta>0$ について、$\lvert x-a\rvert<\delta$ のすべての $x$ で成立」と読む。例えば $a=0$ での条件 $\lvert x\rvert<1$ は eventually 成立する。近傍は点 $a$ 自身も含むので、`∀ᶠ x in nhds a, P x` なら `P a` も成立する。

## Tendsto の二つのフィルター

`Filter.Tendsto f l₁ l₂` は、**入力を `l₁` に沿って動かすと、出力が `l₂` に沿う**という命題である。

| 対象 | Lean の型・役割 |
| --- | --- |
| 関数 | `f : E → F` |
| 入力側のフィルター | `l₁ : Filter E` |
| 出力側のフィルター | `l₂ : Filter F` |
| 収束・極限の条件 | `Filter.Tendsto f l₁ l₂ : Prop` |

具体的には、出力側の集合 $t\in l_2$ をどれでも選ぶと、その逆像 $f^{-1}(t)$ が入力側の $l_1$ に属することである。

$$
\forall t\in l_2,\quad f^{-1}(t)\in l_1.
$$

ここで逆像とは $\{x\mid f(x)\in t\}$。出力に要求した条件を、入力が十分先・十分近くになったときに満たす、という意味になる。

| 数学の対象 | 数学 | Lean |
| --- | --- | --- |
| 数列の収束 | $u_n\to b$ | `Filter.Tendsto u Filter.atTop (nhds b)` |
| 点を含む近傍での極限 | $x\to a$ のとき $f(x)\to b$ | `Filter.Tendsto f (nhds a) (nhds b)` |
| 点を除く通常の関数の極限 | $\lim_{x\to a,\ x\ne a}f(x)=b$ | `Filter.Tendsto f (nhdsWithin a {a}ᶜ) (nhds b)` |
| 領域内からの極限 | $x\to a,\ x\in s$ のとき $f(x)\to b$ | `Filter.Tendsto f (nhdsWithin a s) (nhds b)` |

例えば `u : ℕ → ℝ` の収束 `Filter.Tendsto u Filter.atTop (nhds b)` は、通常の次の条件になる。

$$
\forall\varepsilon>0,\ \exists N,\ \forall n\ge N,
\quad\lvert u_n-b\rvert<\varepsilon.
$$

出力側の近傍は「$b$ からの誤差が $\varepsilon$ 未満」、入力側の `atTop` は「$N$ 以降」を受け持つ。同じ `Tendsto` で数列と関数の極限を扱えるのは、近づき方をフィルターに分けて指定しているためである。

```lean
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Order.Filter.AtTopBot.Basic

open scoped Topology

example : Filter.Tendsto (fun _ : ℕ => (2 : ℝ))
    Filter.atTop (𝓝 2) := by
  exact tendsto_const_nhds
```

この例は、定数列 $u_n=2$ が $2$ に収束することを表す。`Tendsto` は極限値を計算する関数ではなく、指定した極限の条件が成立するという命題である。

## 点を含む近傍と穴あき近傍

`nhds a` は $a$ 自身を含む。一方、`nhdsWithin a {a}ᶜ` は $a$ を除いた場所から近づく条件であり、記法は `𝓝[≠] a` である。

例えば $f(0)=1$、$x\ne0$ では $f(x)=0$ とする。穴あき近傍からなら $0$ に収束するが、`nhds 0` から $0$ に収束するとは言えない。後者は点 $0$ での値も条件に含むためである。連続性は `Tendsto f (nhds a) (nhds (f a))`、微分の差商の極限では穴あき近傍を使う。

また、`nhdsWithin a s` は $a\in s$ を要求しない。例えば $s=(0,\infty)$ から $a=0$ に近づくことも表せる。

## フィルターの順序と空の条件

mathlib では `l₁ ≤ l₂` を「`l₂` に属する集合はすべて `l₁` にも属する」と定める。集合の集まりとしては包含が逆向きになる。より多くの集合を十分な集合とみなす `l₁` は、近づき方をより限定している。

例えば `nhdsWithin a s ≤ nhds a`。通常の近傍からの極限が成り立つなら、入力をさらに $s$ 内に限定しても同じ極限が成り立つ。

`Filter.map f l₁` は $f$ によって入力側のフィルターを出力側へ移したもの。集合 $t$ がこれに属する条件は `f ⁻¹' t ∈ l₁` であり、`Tendsto f l₁ l₂` の定義は `Filter.map f l₁ ≤ l₂` である。

フィルターの3条件は空集合の所属を禁止していない。空集合が属すると、すべての集合が属するフィルター `⊥` になる。

| 意味 | Lean |
| --- | --- |
| 空集合も含むフィルター | `(⊥ : Filter E)` |
| 空集合を含まない、退化していないフィルター | `Filter.NeBot l` |

`∀ᶠ x in (⊥ : Filter E), P x` は任意の `P` で成立し、`Tendsto f ⊥ l₂` も成立する。例えば `nhdsWithin a ∅ = ⊥` なので、空の領域からの極限はどの値に対しても成立する。極限の一意性などで `NeBot` が必要になるのは、この空の条件を除くためである。極限値の一意性には、さらに出力空間の分離性なども必要になる。

## 測度と級数で現れるフィルター

測度 $\mu$ の `MeasureTheory.ae μ` もフィルターであり、補集合の測度が $0$ になる集合を集める。

| 意味 | Lean |
| --- | --- |
| 零測度の例外を除いて成立 | `∀ᵐ x ∂μ, P x` |
| 上と同じフィルターによる表現 | `∀ᶠ x in MeasureTheory.ae μ, P x` |

この場合の eventually は「十分大きい添字」ではなく「ほとんど至る所」を意味する。どちらも、条件を満たす集合が指定したフィルターに属するという同じ仕組みで表される。

級数の `SummationFilter ℕ` は、`Filter ℕ` そのものではない。どの有限部分集合に沿って和を取るかを指定する構造であり、その `.filter` の型は `Filter (Finset ℕ)`。入力が自然数の点ではなく、部分和の添字となる有限集合であることに注意する。

関連：[領域・極限・連続性](limits_continuity.md)、[数列と級数](sequences_series.md)、[関数列の収束](function_sequences.md)、[測度と積分](measure_integrals.md)。共通の構文：[公式リファレンス：型クラス](https://lean-lang.org/doc/reference/latest/Type-Classes/)、[記法の定義](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/)。

[mathlib の索引に戻る](README.md)
