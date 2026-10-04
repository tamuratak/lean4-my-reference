# `rw`

`rw` は、**等式や同値を使って、ゴールや仮定を書き換える**タクティクスである。

`h : a = b` があれば、`rw [h]` は `a` を `b` に書き換える。

```lean
example (a b : Nat) (h : a = b) : a + 1 = b + 1 := by
  rw [h]
```

逆向きには `←` を付ける。仮定を書き換えるには `at` を付ける。

```lean
example (P : Nat → Prop) (a b : Nat) (h : a = b) (ha : P a) : P b := by
  rw [h] at ha
  exact ha

example (a b : Nat) (h : a = b) : b + 1 = a + 1 := by
  rw [← h]
```

複数なら `rw [h₁, h₂]` と書く。`rw` は書き換えの後、定義上の等しさでゴールを閉じることも試す。`rewrite` はその最後の処理を行わない。

`rwa [h]` は `rw [h]` の後に `assumption` を試す書き方である。`erw` は通常の `rw` より定義の展開を許して書き換える。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`rw`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.rwSeq)。

[タクティクス一覧に戻る](README.md)
