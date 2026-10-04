# `bv_omega`

`bv_omega` は、**ビットベクトルの算術を自然数の条件に変換し、`omega` で解く**タクティクスである。

値の自然数への変換とビット幅の範囲を利用する。

```lean
example (x : BitVec 8) : x.toNat < 256 := by
  bv_omega
```

`bv_decide` がビット演算の命題を SAT ソルバーで扱うのに対し、`bv_omega` は自然数の線形算術に帰着する形で使う。

ビット演算を含むどんな式でも解けるわけではない。変換後に `omega` が扱える形になることが必要である。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
