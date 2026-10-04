# `repeat`

`repeat` は、**指定したタクティクスを、失敗するまで繰り返す**タクティクスである。

複数の引数を導入する例である。

```lean
example (P Q : Prop) : P → Q → P := by
  repeat intro
  assumption
```

`intro` ができなくなったところで繰り返しを終える。

`repeat` は先頭のゴールを中心に処理する。`repeat'` は生じた各ゴールにも繰り返し適用し、`repeat1'` は少なくとも一回の成功を要求する。

```lean
example (P Q R : Prop) (hp : P) (hq : Q) (hr : R) : P ∧ Q ∧ R := by
  repeat' constructor
  all_goals assumption
```

`repeat skip` のように、成功しても何も変えない操作は終了しないので避ける。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
