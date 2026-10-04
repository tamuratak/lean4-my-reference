# `dsimp`

`dsimp` は、**定義上の等しさを保つ計算や展開によって、式を簡単にする**タクティクスである。

`let` や関数適用を計算したいときに使える。

```lean
example (n : Nat) : (fun x : Nat => x) n = n := by
  dsimp

example (n m : Nat) (h : n = m) : (let x := n; x) = m := by
  dsimp
  exact h
```

`simp` は一般の等式の定理も使うが、`dsimp` は定義上の等しさによる簡単化に使う。

`dsimp [定義名]` と展開する定義を指定したり、`dsimp at h` と仮定を指定したりできる。`dsimp!`、`dsimp?`、`dsimp?!` という変種もある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`dsimp`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.dsimp)。

[タクティクス一覧に戻る](README.md)
