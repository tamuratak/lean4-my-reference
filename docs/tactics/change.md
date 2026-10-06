# `change`

`change` は、ゴールや仮定を、定義上等しい別の書き方に変えるタクティクスである。

例えば `n + 0` は計算すると `n` になる。そのため、次のようにゴールの見た目を変えられる。

```lean
example (n m : Nat) (h : n = m) : n + 0 = m := by
  change n = m
  exact h
```

仮定なら `at h` を使う。

```lean
example (n m : Nat) (h : n + 0 = m) : n = m := by
  change n = m at h
  exact h
```

単に同値なだけでは足りず、定義に従って計算した結果が同じである必要がある。一般の定理による変形には `rw` などを使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`change`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.change)。

[タクティクス一覧に戻る](README.md)
