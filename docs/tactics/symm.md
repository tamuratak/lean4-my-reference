# `symm`

`symm` は、等式など、対称な関係の向きを反転するタクティクスである。

ゴールが `a = b` のとき、`symm` で `b = a` に変えられる。

```lean
example (a b : Nat) (h : b = a) : a = b := by
  symm
  exact h
```

`at h` を付けると、仮定の向きを反転する。

```lean
example (a b : Nat) (h : a = b) : b = a := by
  symm at h
  exact h
```

`≤` のように対称でない関係を逆にすることはできない。`symm_saturate` は仮定にある対称な関係の逆向きの事実を追加するための関連タクティクスである。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`symm`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.symm)。

[タクティクス一覧に戻る](README.md)
