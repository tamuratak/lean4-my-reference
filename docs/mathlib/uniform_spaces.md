# 一様空間と完備性

位相は「点の近く」を表す。一様構造はさらに、「二点が近い」という条件を空間全体で共通に扱う。距離空間では、距離が $\varepsilon$ 未満の点の組を使う。

$$
U_\varepsilon=\{(x,y)\mid\operatorname{dist}(x,y)<\varepsilon\},\qquad\varepsilon>0.
$$

## 位相・距離・一様構造

| 意味 | Lean | 主な用途 |
| --- | --- | --- |
| 位相を持つ空間 | `[TopologicalSpace E]` | 近傍、連続性、点への収束 |
| 距離を持つ空間 | `[MetricSpace E]` | 距離による評価 |
| 一様構造を持つ空間 | `[UniformSpace E]` | 一様連続、一様収束、Cauchy 性 |
| 近い点の組の条件を集めたフィルター | `uniformity E` または `𝓤 E` | `Filter (E × E)` の値 |

距離空間には標準の一様構造があり、一様構造から位相も得られる。一般の一様空間では、距離の数値を選ばなくても「十分近い二点」という条件を扱える。`𝓤` の記法には `open scoped Uniformity` を使う。

`U ∈ uniformity E` は、集合 `U : Set (E × E)` が「十分近い点の組」を含むという意味。一様構造では、対角線を含むこと、近さが対称であること、十分小さい近さを二段つないでも指定した近さに入ることを要求する。これらは個々の集合の形ではなく、フィルター全体の性質である。

## 一様連続と一様収束

| 数学の対象 | 数学 | Lean |
| --- | --- | --- |
| 一様連続 | 入力の近さを点によらず共通に選べる | `UniformContinuous f` |
| 領域上の一様連続 | $s$ の点同士について共通に選べる | `UniformContinuousOn f s` |
| 関数列の一様収束 | 誤差の条件を満たす添字を点によらず選べる | `TendstoUniformly F f Filter.atTop` |

距離空間での一様連続は、次の条件に対応する。

$$
\forall\varepsilon>0,\ \exists\delta>0,\ \forall x,y,
\quad\operatorname{dist}(x,y)<\delta
\ \Longrightarrow\ \operatorname{dist}(f(x),f(y))<\varepsilon.
$$

普通の点での連続性では $\delta$ がその点に依存してよい。一様連続では空間全体で同じ $\delta$ を使う。例えば $f(x)=x^2$ は実数上で連続だが、実数全体では一様連続ではない。

## Cauchy 性と完備性

数列 $(u_n)$ の Cauchy 性は、十分先の項同士が任意に近くなることであり、極限の候補を先に指定しない。

$$
\forall\varepsilon>0,\ \exists N,\ \forall m,n\ge N,
\quad\operatorname{dist}(u_m,u_n)<\varepsilon.
$$

| 意味 | Lean |
| --- | --- |
| 数列が Cauchy 列 | `CauchySeq u` |
| フィルターの Cauchy 性 | `Cauchy l` |
| 空間が完備 | `[CompleteSpace E]` |
| 部分集合が完備 | `IsComplete s` |
| 完備空間の Cauchy 列の収束 | `cauchySeq_tendsto_of_complete` |

mathlib の完備性は、すべての Cauchy フィルターがある点に収束することとして定義される。Cauchy フィルターの条件には `NeBot` も含み、空の条件からの収束を除いている。距離空間では、通常の「すべての Cauchy 列が収束する」という完備性に対応する。

実数は完備だが有理数は完備ではない。有理数の Cauchy 列が実数内で収束しても、その極限が有理数の空間内にあるとは限らない。

```lean
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.UniformSpace.Cauchy

open scoped Topology Uniformity

#check (𝓤 ℝ : Filter (ℝ × ℝ))

example (u : ℕ → ℝ) (hu : CauchySeq u) :
    ∃ a : ℝ, Filter.Tendsto u Filter.atTop (𝓝 a) := by
  exact cauchySeq_tendsto_of_complete hu
```

`[CompleteSpace E]` だけでは、極限の一意性まで要求しない。一般の一様空間で一意性を述べるには分離性も確認する。通常の距離空間はその条件を満たす。

関連：[フィルターと極限](filters.md)、[関数列と一様収束](function_sequences.md)、[開集合とコンパクト性](topology_compactness.md)。共通の構文：[公式リファレンス：型クラス](https://lean-lang.org/doc/reference/latest/Type-Classes/)。

[mathlib の索引に戻る](README.md)
