# `rwa`

`rwa` は、`rw` で書き換えた後、仮定でゴールを閉じるタクティクスである。

書き換えによって手元の仮定と同じゴールになる場合に便利である。

```lean
example (P : Nat → Prop) (a b : Nat) (h : a = b) (hb : P b) : P a := by
  rwa [h]
```

`rw [h]` で `P a` が `P b` になり、その後の `assumption` で `hb` を使って閉じる。

```lean
example (P : Nat → Prop) (a b : Nat) (h : a = b) (hb : P b) : P a := by
  rw [h]
  assumption
```

単なる書き換えでゴールを残したいなら `rw` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`rwa`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.rwa)。

[タクティクス一覧に戻る](README.md)
