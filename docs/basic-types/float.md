# `Float`・`Float32`：浮動小数点数

`Float` は**64ビットの浮動小数点数**、`Float32` は**32ビットの浮動小数点数**を表す型である。小数を含む数値計算に使うが、有限の精度なので丸めがある。追加の `import` は不要である。

## 小数を計算する

```lean
def half : Float := 0.5

#guard half + 0.25 == 0.75
#guard (3.0 : Float) / 2.0 == 1.5
#guard (0.5 : Float32) + 0.25 == 0.75
```

小数のリテラルは周囲の型に従って解釈される。`Nat`・`Int` の除算とは異なり、小数の結果を返せる。具体的な計算の検査には [`#guard`](../commands/guard.md)、結果の表示には [`#eval`](../commands/eval.md) を使う。

## 丸めによって数学の計算と異なる

```lean
#guard !((0.1 : Float) + 0.2 == 0.3)
```

0.1や0.2を二進の有限桁で正確に表せないため、この比較は等しくならない。上の0.5や0.25のように正確に表せる値もあるが、一般に実数の等式をそのまま浮動小数点数に当てはめることはできない。

## `NaN`・無限大と比較

```lean
def invalid : Float := (0.0 : Float) / 0.0
def infinity : Float := (1.0 : Float) / 0.0

#guard invalid.isNaN
#guard !(invalid == invalid)
#guard infinity.isInf
```

`NaN` は数として定まらない計算結果、無限大は有限の範囲を超える結果などを表す特殊値である。`NaN` は自分自身との `==` も偽になる。ここでの `==` は浮動小数点の比較であり、Lean の等式 `=` と同一視してはいけない。[真偽値の比較](../syntax/boolean_operators.md)も参照。

数学で厳密な有理数や実数を扱う [`Rat`](rat.md)・mathlib の `ℝ` とは用途が異なる。`Float` は丸めを含む数値計算のための型である。

参照：[公式リファレンス：Floating-Point Numbers](https://lean-lang.org/doc/reference/latest/Basic-Types/Floating-Point-Numbers/)。

[基本データ型の一覧に戻る](README.md)
