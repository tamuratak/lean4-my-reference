# `injection`

`injection` は、**同じコンストラクターで作った値の等式から、引数どうしの等式を取り出す**タクティクスである。

`Nat.succ n = Nat.succ m` なら、引数も等しく `n = m` である。

```lean
example (n m : Nat) (h : Nat.succ n = Nat.succ m) : n = m := by
  injection h with hnm
```

リストの等式からは、先頭と残りの等式を取り出せる。

```lean
example (a b : Nat) (xs ys : List Nat) (h : a :: xs = b :: ys) : a = b := by
  injection h with hab htail
```

取り出した等式でゴールを直接証明できるときは、その場で閉じる。この例では追加の `exact` は不要である。

`injections` は仮定にあるコンストラクターの等式に対して、この操作を繰り返す。一般の関数 `f` は単射とは限らないので、`f a = f b` から常に `a = b` を取り出せるわけではない。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`injection`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.injection)。

[タクティクス一覧に戻る](README.md)
