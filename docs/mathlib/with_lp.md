# 同じ成分に別のノルムを与える型

同じ座標 $x=(x_0,\ldots,x_{n-1})$ に対して、最大値によるノルムとユークリッドノルムは異なる。

$$
\lVert x\rVert_\infty=\max_i\lvert x_i\rvert,\qquad
\lVert x\rVert_2=\sqrt{\sum_i x_i^2}.
$$

mathlib は、元の型の値を別の型に包み、演算を引き継ぎながら別のノルムを付けるために `WithLp` を使う。

## 元の型と包んだ型

| 意味 | Lean |
| --- | --- |
| 元の型 | `V` |
| $p$ に対応するノルムを付けるための型 | `WithLp p V` |
| 元の値を包む | `WithLp.toLp p x` |
| 元の値を取り出す | `WithLp.ofLp y` または `y.ofLp` |
| 値の対応を表す同値 | `WithLp.equiv p V : WithLp p V ≃ V` |

`p` の型は `ENNReal`。`WithLp` は元の値を保持し、加法・スカラー倍などを引き継ぐが、任意の `V` を包むだけで自動的にノルムが付くわけではない。有限個の成分を持つ空間などに対して、対応するノルムのインスタンスが別途定義される。

元の型にノルムがあっても、それをそのまま引き継ぐための仕組みではない。同じ型の `norm` に複数の意味を混在させず、包んだ型に意図したノルムを持たせる。

## 座標空間とユークリッド空間

| 型 | 標準のノルム・意味 |
| --- | --- |
| `Fin n → ℝ` | 最大値によるノルム（$n>0$） |
| `PiLp p (fun _ : Fin n => ℝ)` | 座標関数を `WithLp p` で包んだ型 |
| `EuclideanSpace ℝ (Fin n)` | 上の $p=2$ の型。ユークリッドノルムと内積を持つ |

有限個の成分について、$1\le p<\infty$ の通常のノルムは $\bigl(\sum_i\lvert x_i\rvert^p\bigr)^{1/p}$。ノルム空間として使うには、対応する $p$ の条件が必要になる。$p=\infty$ では最大値によるノルムを使う。

例えば成分 $(3,4)$ の値を包むと、成分は変わらず、ノルムが $4$ から $5$ に変わる。

```lean
import Mathlib.Analysis.InnerProductSpace.PiL2

def coordinates : Fin 2 → ℝ := ![3, 4]
def point : EuclideanSpace ℝ (Fin 2) := WithLp.toLp 2 coordinates

example : WithLp.ofLp point = coordinates := rfl
example : point 0 = 3 := rfl
example : point 1 = 4 := rfl

#check (‖coordinates‖ : ℝ)
#check (‖point‖ : ℝ)
```

`WithLp.toLp` は成分を変更する座標変換ではない。包む前後で値が対応していても、ノルムを含む等式や評価は、それぞれの型の構造に従う。

## 測度論の Lp との違い

`WithLp p V` と `MeasureTheory.Lp E p μ` は別の対象である。

| 対象 | 何を表すか |
| --- | --- |
| `WithLp p V` | 元の値を別の型に包み、別のノルムを付けるための仕組み |
| `MeasureTheory.Lp E p μ` | ほとんど至る所で等しい関数を同一視し、対応する有限性条件を課した空間 |

有限次元の座標を包む操作は、一般の無限個の座標に総和可能性の条件を付けたり、測度に関して関数を同一視したりする操作ではない。測度論の $L^p$ の要素と、もとの点ごとの関数の違いは[強可測性と同一視](strong_measurability.md)を参照。

関連：[空間と標準ノルム](spaces.md#ユークリッド空間とノルム)、[ノルムと内積](norms_inner_products.md)、[拡張非負実数](extended_nonnegative.md)。共通の構文：[公式リファレンス：構造体](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

[mathlib の索引に戻る](README.md)
