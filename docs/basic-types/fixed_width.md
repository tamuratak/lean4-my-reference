# 固定幅整数・`BitVec`：ビット数が決まった数

`UInt8` などの固定幅整数は、**決まったビット数で数を表す型**である。任意の大きさを扱う [`Nat`](nat.md)・[`Int`](int.md) と異なり、範囲を超えると演算結果が巡回する。追加の `import` は不要である。

## 符号なし・符号付きの整数

| 型 | 範囲・特徴 |
| --- | --- |
| `UInt8` | ０から255までの８ビット符号なし整数 |
| `UInt16`・`UInt32`・`UInt64` | 16・32・64ビットの符号なし整数 |
| `Int8` | −128から127までの８ビット符号付き整数 |
| `Int16`・`Int32`・`Int64` | 16・32・64ビットの符号付き整数 |
| `USize`・`ISize` | 実行環境に応じた幅の符号なし・符号付き整数 |

```lean
#guard (255 : UInt8).toNat == 255
#guard ((255 : UInt8) + 1).toNat == 0
#guard (256 : UInt8).toNat == 0
#guard ((127 : Int8) + 1).toInt == (-128 : Int)
```

`.toNat`・`.toInt` で通常の自然数・整数へ変換できる。`UInt8` の加算は256を法として巡回し、数値リテラルも範囲に合わせて巡回する。したがって、範囲外の数を拒否するための型としては、そのまま使えない。

## `BitVec w`：幅を型で指定する

```lean
def bits : BitVec 4 := 15

example : bits.toNat = 15 := rfl
example : (bits + 1).toNat = 0 := rfl
example : (16 : BitVec 4).toNat = 0 := rfl
example : ((12 : BitVec 4) &&& 10).toNat = 8 := rfl
```

`BitVec 4` は４ビットの列を表し、自然数としては０から15までになる。`.toNat` は符号なしの値として取り出す。`&&&` は各ビットの AND であり、上の例では `1100` と `1010` から `1000` を得る。

`UInt8` のような機械整数とは別の型であり、`BitVec w` は幅 `w` を任意に指定できる。ビット演算の性質を証明する用途には [`bv_decide`](../tactics/bv_decide.md) なども使える。

## `Fin` との違い

[`Fin n`](fin.md) は任意の上限 `n` 未満の自然数を表す。`BitVec w` の範囲は `2^w` 未満であり、`w` は上限ではなくビット数である。例えば `Fin 4` の値は０から３まで、`BitVec 4` の値は０から15までになる。

参照：[公式リファレンス：Fixed-Precision Integers](https://lean-lang.org/doc/reference/latest/Basic-Types/Fixed-Precision-Integers/)、[Bitvectors](https://lean-lang.org/doc/reference/latest/Basic-Types/Bitvectors/)。

[基本データ型の一覧に戻る](README.md)
