# `Rat`：有理数

`Rat` は、整数の分子と正の自然数の分母で有理数を正確に表す型である。浮動小数点の丸めを使わず、分数の演算を行える。標準の `import Init.Data.Rat` を使い、mathlib は不要である。

## 分数を作る・計算する

```lean
import Init.Data.Rat

def half : Rat := (1 : Rat) / 2

#guard half + half = 1
#guard (1 : Rat) / 10 + (2 : Rat) / 10 = (3 : Rat) / 10
#guard (2 : Rat) / 4 = half
```

`Rat` の `/` は分数として計算する。`Nat`・`Int` の整数の商とは異なり、`1 / 2` の情報を保持する。分子・分母は約分された形で保持されるため、`2 / 4` と `1 / 2` は同じ値になる。

## 分子と分母を取り出す

```lean
import Init.Data.Rat

def fraction : Rat := (-6 : Rat) / 8

#guard fraction.num = (-3 : Int)
#guard fraction.den = 4
#guard (0 : Rat).den = 1
```

`.num` は分子の `Int`、`.den` は分母の `Nat` を返す。符号は分子側にあり、０は分母１の形で表される。

## `Float` と除算の違い

[`Float`](float.md) は有限精度の近似計算、`Rat` は有理数の厳密な計算に使う。上の `1/10 + 2/10 = 3/10` は丸め誤差なく成立する。ただし、任意の実数を表す型ではなく、例えば無理数そのものを分数として保持することはできない。

```lean
import Init.Data.Rat

#guard (1 : Rat) / 0 = 0
```

Lean の `Rat` の除算は０で割る場合にも値を返し、結果を `0` と定めている。これは数学で０除算が可能という意味ではない。除数が非零であることを必要とする性質を使う場合は、その条件を別に証明する。

参照：[公式 API：Rat](https://lean-lang.org/doc/api/Init/Data/Rat/Basic.html#Rat)。

[基本データ型の一覧に戻る](README.md)
