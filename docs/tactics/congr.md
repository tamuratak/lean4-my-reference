# `congr`

`congr` は、**同じ関数などの等式を、対応する引数の等式に分解する**タクティクスである。

ゴールが `f a = f b` のとき、同じ関数 `f` に渡す引数が等しいことを示せばよい。

```lean
example (f : Nat → Nat) (a b : Nat) (h : a = b) : f a = f b := by
  congr 1
```

分解後の等式が仮定にあれば、この例のように自動で閉じることもある。

`congr 1` の数字は、分解の深さを制限する。省略するとさらに分解を進めることがある。

`injection` はコンストラクターの等式という仮定から引数の等式を取り出す操作であり、`congr` は等式のゴールを引数の等式へ帰着する操作である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`congr`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.congr)。

[タクティクス一覧に戻る](README.md)
