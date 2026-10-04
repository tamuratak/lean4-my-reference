# `clear_value`

`clear_value` は、**局所定義の値を忘れ、名前と型だけを残す**タクティクスである。

`let n := 3` で導入した `n` から、値が `3` という定義を取り除ける。

```lean
example : ∃ n : Nat, n = 3 := by
  let n : Nat := 3
  clear_value (hn : n = 3)
  exact ⟨n, hn⟩
```

ここでは `clear_value (hn : n = 3)` で、先に `hn : n = 3` を残してから値を忘れている。

単に `clear_value n` と書くと、定義の値は展開できなくなる。`clear n` が名前そのものを消すのに対し、`clear_value` は値だけを消す。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`clear_value`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.clearValue)。

[タクティクス一覧に戻る](README.md)
