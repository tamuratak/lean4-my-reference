# `grobner`

`grobner` は、可換な環や半環上の多項式の等式を証明するタクティクスである。

加算と乗算の分配法則などを使う等式に利用できる。

```lean
example (x y : Int) : (x + y) * (x + y) = x * x + 2 * x * y + y * y := by
  grobner
```

多項式の等式の仮定も使える。

```lean
example (x y : Int) (h : x * x = y) : x * x + 1 = y + 1 := by
  grobner
```

`grind` の多項式ソルバーに絞った操作である。`ac_rfl` は結合則と交換則の並べ替えに使い、`grobner` は分配法則なども含む多項式の関係に使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`grobner`](https://lean-lang.org/doc/api/Init/Grind/Tactics.html#Lean.Parser.Tactic.grobner)。

[タクティクス一覧に戻る](README.md)
