# `Int`：整数

`Int` は、負の数、０、正の数を含む整数の型である。`…, -2, -1, 0, 1, 2, …` を表し、型として固定の上限・下限はない。追加の `import` は不要である。

## 値と計算

```lean
def offset : Int := -3

example : offset + 5 = 2 := rfl
example : (2 : Int) - 5 = -3 := rfl
example : (-3 : Int) * 2 = -6 := rfl
```

[`Nat`](nat.md) の引き算は０で止まるが、`Int` の引き算は負の結果も返す。型を指定せずに書いた正の数は `Nat` と解釈される場合があるので、整数の計算を意図するときは `Int` を明示すると分かりやすい。

## 自然数との変換

```lean
def asInt (n : Nat) : Int := (n : Int)

example : asInt 3 = (3 : Int) := rfl
example : (5 : Int).toNat = 5 := rfl
example : (-3 : Int).toNat = 0 := rfl
```

`Nat` から `Int` への変換は、`(n : Int)` のように型を指定して使える。逆方向の `.toNat` は、非負ならその自然数を返し、負なら `0` を返す。したがって、整数を `.toNat` で変換すると負の値の情報は失われる。

## 商と余り

```lean
example : (7 : Int) / 3 = 2 := rfl
example : (7 : Int) % 3 = 1 := rfl
example : (-7 : Int) / 3 = -3 := rfl
example : (-7 : Int) % 3 = 2 := rfl
```

`/` は整数の商であり、分数や小数を返さない。Lean の整数の `/`・`%` はユークリッド除算を使う。正の除数 `3` に対しては、余りが `0` 以上 `3` 未満になるように商を選ぶため、`-7 = (-3) * 3 + 2` となる。負の数の商を単純に０方向へ切り捨てる計算とは異なる。

参照：[公式リファレンス：Integers](https://lean-lang.org/doc/reference/latest/Basic-Types/Integers/)。

[基本データ型の一覧に戻る](README.md)
