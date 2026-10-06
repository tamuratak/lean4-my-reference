# mathlib の記号索引

**mathlib を使う数学の式に出てきた記号から、意味と関連する概念を探すための索引**。ページ内検索で、記号そのものや「線形写像」「近傍」「積分」「ほとんど至る所」などの呼び名を検索できる。

現在は多変数・多次元の微分積分と、その基礎になる級数・線形代数・位相の記法を中心に扱う。数学の意味は LaTeX で示し、Lean の記号はコードとして示す。使用形は型・式・命題の断片であり、完成したプログラムや証明ではない。

通常の関数の矢印、量化、括弧などは [Lean 全般の記号索引](../symbols.md)を参照。ここでは mathlib の数学での使い方を整理するため、Lean 本体と共有する記号も必要な範囲で載せる。

## 数の型・無限大

| 記号・形 | 呼び名・数学の意味 | 正式名・読み方 | 詳細 |
| --- | --- | --- | --- |
| `ℕ` | 自然数 $\mathbb{N}$ | `Nat` | [自然数](../basic-types/nat.md) |
| `ℤ` | 整数 $\mathbb{Z}$ | `Int` | [整数](../basic-types/int.md) |
| `ℚ` | 有理数 $\mathbb{Q}$ | `Rat` | [有理数](../basic-types/rat.md) |
| `ℝ` | 実数 $\mathbb{R}$ | `Real` | [空間と関数の型](spaces.md) |
| `ℂ` | 複素数 $\mathbb{C}$ | `Complex` | 実数上の微分と複素数上の微分は区別する |
| `ℝ≥0` | 非負実数 $[0,\infty)$ | `NNReal` | [非負実数](extended_nonnegative.md) |
| `ℝ≥0∞` | 拡張非負実数 $[0,\infty]$ | `ENNReal` | [拡張非負実数](extended_nonnegative.md) |
| `∞`（`ENNReal` の値） | 無限大 | その型の最大の値 `⊤` | [変換と演算の条件](extended_nonnegative.md) |
| `a.toReal`（`a : ENNReal`） | 実数への変換 | 無限大は $0$ に変換される | [実数との変換](extended_nonnegative.md#実数との変換) |
| `∞`（`ContDiff` の階数） | すべての有限階、$C^\infty$ | `ContDiff ℝ ∞ f` | [滑らかさ](higher_derivatives.md#連続微分可能性) |
| `ω`（`ContDiff` の階数） | 解析的な正則性、$C^\omega$ | `ContDiff ℝ ω f` | [滑らかさ](higher_derivatives.md#連続微分可能性) |

`∞` は型やスコープによって意味が変わる。この固定バージョンの `ContDiff` では、`∞` と `ω` は別の階数であり、`⊤` は後者に対応する。非負積分の無限大と混同しない。

## 係数体の変数名

| 記号・形 | 呼び名・数学の意味 | 読み方 | 詳細 |
| --- | --- | --- | --- |
| `𝕜` | 係数体 $\mathbb{k}$ によく使う変数名 | 宣言された型を指す。体の条件は `[Field 𝕜]` などの仮定で決まる | [係数体を表す変数名](spaces.md#係数体を表す変数名) |

`𝕜` は命名の慣習であり、定義済みの型を指す `ℝ`・`ℂ` とは異なる。実数・複素数に限定されるかどうかも、名前だけでは決まらない。

## 集合・領域

| 記号・形 | 呼び名・数学の意味 | 使用形・正式名 | 詳細 |
| --- | --- | --- | --- |
| `∈`・`∉` | 所属・非所属、$x\in s$・$x\notin s$ | `x ∈ s`、`x ∉ s` | [領域](limits_continuity.md#領域) |
| `⊆` | 包含、$s\subseteq t$ | `s ⊆ t`、`Set.Subset s t` | [領域](limits_continuity.md#領域) |
| `∅` | 空集合 $\varnothing$ | `(∅ : Set E)`、`EmptyCollection.emptyCollection` | [領域](limits_continuity.md#領域) |
| `∪`・`∩` | 和集合・共通部分、$s\cup t$・$s\cap t$ | `s ∪ t`、`s ∩ t` | [領域](limits_continuity.md#領域) |
| `sᶜ` | 補集合 $s^c$ | `sᶜ`、`Set.compl s` | [近傍と極限](limits_continuity.md#極限と近傍) |
| `s \ t` | 差集合 $s\setminus t$ | `s \ t` | [領域](limits_continuity.md#領域) |
| `{x \| P x}` | 集合の内包表記、$\{x\mid P(x)\}$ | `{x : E \| P x}` | 条件を満たす点の集合。部分型 `{x : E // P x}` とは異なる |
| `×ˢ` | 集合の直積 $s\times t$ | `s ×ˢ t`、`Set.prod s t` | [領域](limits_continuity.md#領域) |
| `f '' s` | 像 $f(s)$。二つのアポストロフィ | `f '' s`、`Set.image f s` | [変数変換](change_variables.md#領域微分体積の倍率) |
| `f ⁻¹' t` | 逆像 $f^{-1}(t)$ | `f ⁻¹' t`、`Set.preimage f t` | $f$ に逆関数があることは要求しない |
| `Set.Icc a b` | 閉区間 $[a,b]$ | `Icc` は両端を含む区間 | [領域](limits_continuity.md#領域) |
| `Set.Ioo a b` | 開区間 $(a,b)$ | `Ioo` は両端を含まない区間 | [領域](limits_continuity.md#領域) |
| `Set.uIcc a b`・`Set.uIoc a b` | 端点の大小によらない区間 | $[\min(a,b),\max(a,b)]$、$(\min(a,b),\max(a,b)]$ | [区間積分](interval_integrals.md) |
| 数学の $\operatorname{int}(s)$・$\overline{s}$・$\partial s$ | 内部・閉包・境界 | `interior s`、`closure s`、`frontier s` | [開集合・閉集合](topology_compactness.md#開集合閉集合と境界) |
| `IsCompact s` | 集合のコンパクト性 | 開被覆から有限部分被覆を取れるという命題 | [コンパクト性](topology_compactness.md#コンパクト性と有界性) |

`×` は二つの型から積型を作る記号、`×ˢ` は二つの集合から積集合を作る記号。`ℝ × ℝ` は点の型、`s ×ˢ t` は領域を表す。

## 構造を持つ集合・写像

| 記号・形 | 呼び名・数学の意味 | 使用形・正式名 | 詳細 |
| --- | --- | --- | --- |
| `↥S` | 集合や部分空間の要素の型 | `x : S` は所属の証明も持つ | [集合と要素の型](structured_objects.md#集合と部分空間と要素の型) |
| `(S : Set E)` | 部分空間を集合として見る | `S : Submodule ℝ E` の強制変換 | [部分空間](structured_objects.md#集合と部分空間と要素の型) |
| `(x : E)`（`x : S`） | 部分空間の点を周囲の空間で使う | 部分型の値を取り出す | [部分空間の点](structured_objects.md#集合と部分空間と要素の型) |
| `(A : E → F)` | 性質を備えた写像を関数として使う | 線形写像などの強制変換 | [性質を備えた写像](structured_objects.md#関数と性質を備えた写像) |

## ベクトル・線形写像・行列

| 記号・形 | 呼び名・数学の意味 | 使用形・正式名 | 詳細 |
| --- | --- | --- | --- |
| `•` | スカラー倍 $cv$ | `c • v`、`SMul.smul c v` | [点とベクトル](spaces.md#点と関数) |
| `![…]` | 有限個の成分を並べた関数 | `![x, y]` は二成分。`Fin 2 → ℝ` など | [座標](spaces.md)、[高階微分の方向の組](higher_derivatives.md#多変数の高階微分) |
| `‖x‖` | ノルム $\lVert x\rVert$ | `norm x` | [空間とノルム](spaces.md#ユークリッド空間とノルム) |
| `\|x\|` | 絶対値 $\lvert x\rvert$ | `abs x` | [ヤコビアンの行列式](change_variables.md) |
| `⟪x, y⟫_ℝ` | 実内積 $\langle x,y\rangle$ | `inner ℝ x y` | [勾配](partial_gradient.md#勾配) |
| `⟪x, y⟫` | スカラーをスコープで決めた内積 | 実内積のスコープなら `inner ℝ x y` | [勾配](partial_gradient.md#勾配) |
| `E →ₗ[ℝ] F` | 実線形写像 $A:E\to F$ の型 | `LinearMap (RingHom.id Real) E F` | [正式名](linear_maps.md#線形写像の型と正式名) |
| `E →L[ℝ] F` | 実連続線形写像 $A:E\to F$ の型 | `ContinuousLinearMap (RingHom.id Real) E F` | [全微分の値](linear_maps.md) |
| `E ≃ₗ[ℝ] F` | 線形同値、線形な可逆写像 | `LinearEquiv (RingHom.id Real) E F` | [線形写像](linear_maps.md) |
| `E ≃L[ℝ] F` | 連続線形同値。逆写像も連続 | `ContinuousLinearEquiv (RingHom.id Real) E F` | [線形写像](linear_maps.md) |
| `E [×k]→L[ℝ] F` | $k$ 個の方向を受け取る連続多重線形写像 | `ContinuousMultilinearMap Real (fun _ : Fin k => E) F` | [高階微分](higher_derivatives.md#多変数の高階微分) |
| `A v` | 線形写像を方向に適用、$A(v)$ | 全微分なら `fderiv ℝ f x v` | [線形写像の操作](linear_maps.md#線形写像に対する操作) |
| `M i j` | 行列の成分 $M_{ij}$ | 第一添字が行、第二添字が列 | [ヤコビアン](linear_maps.md#ヤコビアン行列) |
| `!![…; …]` | 行を並べた行列の記法 | `!![1, 2; 3, 4]` | [行列の具体例](matrices_basis.md#行列とベクトルの積) |
| `M *ᵥ x` | 行列と列ベクトルの積 $Mx$ | `Matrix.mulVec M x` | [行列積](matrices_basis.md#行列とベクトルの積) |
| `M * N`（行列） | 行列積 $MN$ | 内側の添字について有限和を取る | [行列積](matrices_basis.md#行列とベクトルの積) |
| `ι →₀ ℝ` | 有限台関数。非零の値を取る添字が有限個 | `Finsupp ι ℝ` | [有限台関数](finitely_supported.md) |
| `c.support`（有限台関数） | 非零の係数を持つ添字の有限集合 | `c : ι →₀ ℝ` なら `Finset ι` の値 | [台](finitely_supported.md#関数と有限台関数の違い) |
| `WithLp.toLp p x`・`WithLp.ofLp y` | 別のノルムを付ける型への変換・元の値の取り出し | 成分の値を変更しない | [WithLp](with_lp.md) |
| `b.repr x i` | 基底 $b$ に関する第 $i$ 座標 | 一般の基底と正規直交基底で座標の型が異なる | [基底](matrices_basis.md#基底と座標)、[正規直交基底](norms_inner_products.md#正規直交族と正規直交基底) |
| `Mᵀ` | 転置行列 $M^{\mathsf T}$ | `Matrix.transpose M` | [Hessian](higher_derivatives.md#hessian-行列) |
| `A.det` | 行列式 $\det A$ | 連続線形自己写像、または行列の `.det` | [変数変換](change_variables.md#領域微分体積の倍率) |

`![x, y]` は、座標番号を受け取る関数。リスト `[x, y]`、配列 `#[x, y]`、ペア `(x, y)` とは型が違う。

ノルムは型によって異なる。例えば `Fin n → ℝ` の標準ノルムと `EuclideanSpace ℝ (Fin n)` のユークリッドノルムは、同じ数式として扱わない。連続線形写像の `‖A‖` は[作用素ノルム](norms_inner_products.md#作用素ノルム)であり、特定の出力の `‖A x‖` とは別の値である。

## 近傍・極限・漸近的な条件

フィルターが何を表すか、入力側と出力側をどう読むかは[フィルターと極限](filters.md)を参照。

| 記号・形 | 呼び名・数学の意味 | 使用形・正式名 | 詳細 |
| --- | --- | --- | --- |
| `𝓝 x` | 点 $x$ の近傍フィルター | `nhds x` | [極限と近傍](limits_continuity.md#極限と近傍) |
| `𝓝[s] x` | 領域 $s$ 内から近づく近傍 | `nhdsWithin x s` | [領域内の微分](fderiv.md#領域内の全微分) |
| `𝓝[≠] x` | 点自身を除いた穴あき近傍 | `nhdsWithin x {x}ᶜ` | [一変数微分](deriv.md) |
| `𝓤 E` | 近い点の組の条件を集めたフィルター | `uniformity E : Filter (E × E)` | [一様空間](uniform_spaces.md#位相距離一様構造) |
| `atTop` | 添字が限りなく大きくなるフィルター | `Filter.atTop`。列の $k\to\infty$ など | [数列](sequences_series.md#数列と部分和) |
| `TendstoUniformlyOn F f l s` | 領域上の一様収束 | 点によらず共通の添字で誤差を抑える | [関数列](function_sequences.md#各点収束と一様収束) |
| `∀ᶠ x in l, P x` | フィルターに沿って eventually 成立 | `Filter.Eventually P l` | [十分先・十分近くで成立](filters.md#十分先十分近くで成立するeventually) |
| `f =ᶠ[l] g` | フィルターに沿って eventually 等しい | `Filter.EventuallyEq l f g` | [Eventually](filters.md#十分先十分近くで成立するeventually)。各点での恒等式とは異なる |
| `𝓟 s` | 固定した集合の主フィルター | `Filter.principal s` | [フィルターと集合](filters.md#十分先十分近くで成立するeventually) |
| `l₁ ≤ l₂`（フィルター） | 集合の所属の包含と逆向きの順序 | `l₂` の集合はすべて `l₁` にも属する | [フィルターの順序](filters.md#フィルターの順序と空の条件) |
| `f =o[l] g` | little-o、$f=o(g)$。$g$ に比べて小さい | `Asymptotics.IsLittleO l f g` | [全微分の一次近似](fderiv.md#fréchet-微分) |
| `f =O[l] g` | big-O、$f=O(g)$。ノルムを定数倍で抑えられる | `Asymptotics.IsBigO l f g` | ノルムによる漸近的な評価 |

`=ᶠ[l]`、`=o[l]`、`=O[l]` の `=` は、通常の等式の見た目に似ているが、それぞれ専用の条件を表す。little-o の `o` は小文字、big-O の `O` は大文字である。

`f : E → F` と `g : E → G` の出力にノルムがあるとき、big-O と little-o は次の不等式で表す。出力の型 `F` と `G` は異なっていてもよい。

| 条件 | フィルターに沿うノルムの評価 |
| --- | --- |
| `Asymptotics.IsBigO l f g` | ある実定数 $C$ について、eventually $\lVert f(x)\rVert\le C\lVert g(x)\rVert$ |
| `Asymptotics.IsLittleO l f g` | すべての $\varepsilon>0$ について、eventually $\lVert f(x)\rVert\le\varepsilon\lVert g(x)\rVert$ |

Lean で量化を明示すると、それぞれ次の条件になる。

```text
∃ C : ℝ, ∀ᶠ x in l, ‖f x‖ ≤ C * ‖g x‖
∀ ε : ℝ, 0 < ε → ∀ᶠ x in l, ‖f x‖ ≤ ε * ‖g x‖
```

little-o では、条件が成立する入力の範囲は $\varepsilon$ ごとに変わってよい。例えば実数の $h\to0$ で $h^2=o(h)$ となるのは、$\lvert h\rvert\le\varepsilon$ なら $\lvert h^2\rvert\le\varepsilon\lvert h\rvert$ だからである。

定義は $\lVert f(x)\rVert/\lVert g(x)\rVert$ という商を使わない。したがって $g(x)=0$ でも読み取れ、その点で上の不等式が成立するには $\lVert f(x)\rVert=0$ が必要になる。商の極限や有界性に言い換える場合には、分母が零でないことなどの条件を確認する。

## 微分・勾配・滑らかさ

| 記号・形 | 呼び名・数学の意味 | Lean での対応 | 詳細 |
| --- | --- | --- | --- |
| 数学の $f'(x)$ | 一変数の微分 | `deriv f x` | [一変数微分](deriv.md) |
| 数学の $\partial_i f(x)$ | 第 $i$ 変数の偏微分 | `deriv (fun t => f (Function.update x i t)) (x i)` | [偏微分](partial_gradient.md#偏微分) |
| 数学の $Df(x)$ | Fréchet 微分、全微分 | `fderiv ℝ f x` | [全微分](fderiv.md#fréchet-微分) |
| `∇ f x` | 勾配 $\nabla f(x)$ | `gradient f x` | [勾配](partial_gradient.md#勾配) |
| 数学の $D^k f(x)$ | 第 $k$ 階全微分 | `iteratedFDeriv ℝ k f x` | [高階微分](higher_derivatives.md#多変数の高階微分) |
| 数学の $C^k$・$C^\infty$ | 連続微分可能性・滑らかさ | `ContDiff ℝ k f`、`ContDiff ℝ ∞ f` | [滑らかさ](higher_derivatives.md#連続微分可能性) |

数学の $f'$、$\partial_i f$、$Df$ が、そのまま Lean の演算子になるわけではない。Lean の `f'` は通常、アポストロフィを含む別の名前である。`f '' s` は集合の像であり、二階微分ではない。

`∇ f x` はベクトル、`fderiv ℝ f x` は連続線形写像。完備な実内積空間では $Df(x)(v)=\langle\nabla f(x),v\rangle$ により対応する。この固定版の `gradient`・`HasGradientAt` は、内積空間の構造に加えて `[CompleteSpace E]` を要求する。ユークリッド空間はこの条件を満たす。どちらも値の表現であり、存在の主張には `HasGradientAt` や `HasFDerivAt` を使う。

## 積分・測度・ほとんど至る所

| 記号・形 | 呼び名・数学の意味 | 使用形・正式名 | 詳細 |
| --- | --- | --- | --- |
| `∫ x, f x` | 標準の体積測度による積分 | $\int f(x)\,dx$。測度は `volume` | [測度と積分](measure_integrals.md#測度と積分の表現) |
| `∫ x, f x ∂μ` | 指定した測度による積分 | `MeasureTheory.integral μ f` | [測度と積分](measure_integrals.md#測度と積分の表現) |
| `∫ x in s, f x ∂μ` | 領域上の積分 $\int_s f\,d\mu$ | `MeasureTheory.integral (μ.restrict s) f` | [領域上の積分](measure_integrals.md) |
| `∫ x in a..b, f x` | 向き付き区間積分 $\int_a^b f(x)\,dx$ | `intervalIntegral f a b volume` | [区間積分](interval_integrals.md) |
| 積分の `∂μ` | 積分に用いる測度の指定、$d\mu$ | 例えば `∂volume`。偏微分の記号ではない | [測度と積分](measure_integrals.md#測度と積分の表現) |
| 区間積分の `a..b` | 積分の始点・終点 | 集合の `[a,b]` とは異なり、向きを持つ | [区間積分](interval_integrals.md) |
| `∫⁻ x, f x ∂μ` | 非負積分。値は $[0,\infty]$ | `MeasureTheory.lintegral μ f` | [非負積分](measure_integrals.md#非負関数の積分) |
| `∫ x, ∫ y, f (x, y)` | 累次積分 | 内側の第二変数を先に積分 | [多重積分](multiple_integrals.md) |
| `μ.prod ν` | 積測度 $\mu\otimes\nu$ | `MeasureTheory.Measure.prod μ ν` | [二重積分](multiple_integrals.md#積測度と二重積分) |
| `∀ᵐ x ∂μ, P x` | $\mu$ に関してほとんど至る所で成立 | `Filter.Eventually P (MeasureTheory.ae μ)` | [可測性と可積分性](measure_integrals.md#可測性と可積分性) |
| `f =ᵐ[μ] g` | ほとんど至る所で等しい | `Filter.EventuallyEq (MeasureTheory.ae μ) f g` | [零測度の例外](strong_measurability.md#零測度の例外を許す) |
| `E →ₘ[μ] F` | ほとんど至る所で等しい関数の同値類 | `MeasureTheory.AEEqFun E F μ` | [関数を同一視した空間](strong_measurability.md#関数を同一視した空間) |
| `E →₁[μ] F`・`E →₂[μ] F` | $L^1$・$L^2$ の要素の型 | `MeasureTheory.Lp F 1 μ`・`MeasureTheory.Lp F 2 μ`（定義域は `E`） | [Lp の要素](strong_measurability.md#関数を同一視した空間) |

`∀ᶠ` は一般のフィルターに沿う条件、`∀ᵐ` は測度に関して零測度の例外を許す条件である。すべての点で成立する `∀` と区別する。

`∫` の値を書くことと、`Integrable f μ` を主張することは別。`∫⁻` は無限大を許す非負積分であり、通常の実数・ベクトル値の積分とは値域も条件も異なる。

## 有限和・有限積・無限和

| 記号・形 | 呼び名・数学の意味 | 使用形・正式名 | 関連 |
| --- | --- | --- | --- |
| `∑ i ∈ s, f i` | 有限集合上の和 $\sum_{i\in s}f(i)$ | `Finset.sum s f` | [有限和](sequences_series.md#数列と部分和) |
| `∑ i, f i` | 有限型の全要素についての和 | `Finset.sum Finset.univ f` | 例えば添字の型が `Fin n` |
| `∏ i ∈ s, f i` | 有限集合上の積 $\prod_{i\in s}f(i)$ | `Finset.prod s f` | 座標ごとの積 |
| `∏ i, f i` | 有限型の全要素についての積 | `Finset.prod Finset.univ f` | 例えば添字の型が `Fin n` |
| `∑ n ∈ Finset.range N, u n` | 最初の $N$ 項の部分和 | 添字は $0$ から $N-1$ まで | [部分和](sequences_series.md#数列と部分和) |
| `∑' n, u n` | 無条件の無限和 $\sum_n u_n$ | `tsum u` | [値と収束条件](sequences_series.md#無限和の値と収束条件) |
| `∑'[L] n, u n` | 和を取る方法を指定した無限和 | `tsum u L`。`L : SummationFilter ℕ` | [順序を固定した収束](sequences_series.md#項の順序を固定した収束) |

`∑` は有限和であり、無限級数の和は `∑' i, f i`、正式名 `tsum f` で表す。有限和の `∑` と依存ペア型の `Σ` は別の記法。`Summable u` は収束条件、`HasSum u a` は収束と和の値を表す命題であり、`tsum u` の値だけでは収束を主張しない。条件収束級数では、既定の無条件の和と自然数の順に足す和を区別する。

## 記法の有効範囲

記法には、必要なモジュールのインポートに加えてスコープの指定が必要なものがある。

| 記法 | 関係するスコープ |
| --- | --- |
| `𝓝` とその領域内の記法 | `Topology` |
| 一様構造の `𝓤` | `Uniformity` |
| 主フィルターの `𝓟` | `Filter` |
| `⟪x, y⟫_ℝ` | `InnerProductSpace` |
| 実内積の `⟪x, y⟫` | `RealInnerProductSpace` |
| `∇` | `Gradient` |
| `ContDiff` の `∞`・`ω` | `ContDiff` |
| `∑`・`∏` | `BigOperators` |
| `ℝ≥0` | `NNReal` |
| 行列の `ᵀ`・`*ᵥ` | `Matrix` |
| `ENNReal` の `∞` | `ENNReal` |
| $L^1$・$L^2$ の矢印 `→₁[μ]`・`→₂[μ]` | `MeasureTheory` |

例えば `open scoped Gradient` は勾配の記法を有効にする指定であり、勾配の存在を仮定する命令ではない。正式名や式の型を確認すると、記号の見た目だけでは分からない意味を区別できる。

共通の仕組みは [notation・infix・scoped](../syntax/notation.md)と[公式リファレンス：Notations and Macros](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/)を参照。

[mathlib の索引に戻る](README.md) · [Lean 全般の記号索引](../symbols.md)
