# `cbv`

`cbv` は、**式を値の計算として評価し、ゴールや仮定を簡単にする**タクティクスである。

具体的なリスト操作などを計算したいときに使える。

```lean
example : (List.range 5).length = 5 := by
  cbv
```

`cbv at h` と書けば仮定を対象にできる。評価してもゴールが残るときは、続けてそのゴールを証明する。

`decide_cbv` は命題の判定手続きを、この評価方法で計算して証明する関連タクティクスである。

```lean
example : 3 < 5 := by
  decide_cbv
```

`omega` のように変数の一般的な算術関係を推論するのではなく、計算できる式を評価するために使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`cbv`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.cbv)。

[タクティクス一覧に戻る](README.md)
