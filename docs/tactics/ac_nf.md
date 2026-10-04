# `ac_nf`

`ac_nf` は、**結合則と交換則を使って、式を共通の標準形に並べ替える**タクティクスである。

項の順序や括弧が異なる式を、同じ形に揃える。

```lean
example (a b c : Nat) : (a + b) + c = c + (b + a) := by
  ac_nf
```

仮定も対象にできる。

```lean
example (a b c : Nat) (h : a + b = c) : b + a = c := by
  ac_nf at *
```

`ac_rfl` はそのような等式を証明するために使い、`ac_nf` は式の正規化にも使う。分配法則による多項式の展開には `grobner` などを使う。

仮定も正規化した結果、その仮定でゴールを閉じられる場合は `ac_nf` 自体が閉じることがある。二つ目の例では追加の `assumption` は不要である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`ac_nf`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticAc_nf_)。

[タクティクス一覧に戻る](README.md)
