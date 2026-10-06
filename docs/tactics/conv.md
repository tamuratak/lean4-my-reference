# `conv`

`conv` は、式の特定の部分を選び、その部分だけを書き換えるタクティクスである。

例えば等式の左辺だけで加算を交換したい場合に使える。

```lean
example (a b : Nat) : a + b = b + a := by
  conv =>
    lhs
    rw [Nat.add_comm]
```

`lhs` は等式の左辺、`rhs` は右辺を選ぶ。関数の引数に進むなら `arg 1` などを使う。

```lean
example (f : Nat → Nat) (a b : Nat) : f (a + b) = f (b + a) := by
  conv =>
    lhs
    arg 1
    rw [Nat.add_comm]
```

`conv at h => ...` は仮定の中、`conv in パターン => ...` は一致する部分を対象にする。内部では `rw`、`simp`、`dsimp`、`unfold` などが使える。

`conv` の中のゴールは、通常の「命題を証明する」ゴールではなく、「選んだ式をどの式に変えるか」を表す。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Targeted-Rewriting-with--conv/)、[公式 API ドキュメント：`conv`](https://lean-lang.org/doc/api/Init/Conv.html#Lean.Parser.Tactic.conv)。

[タクティクス一覧に戻る](README.md)
