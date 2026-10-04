# `fun_induction`

`fun_induction` は、**再帰関数の定義に沿った帰納法を行う**タクティクスである。

自然数を一つずつ減らすとは限らない再帰関数では、関数専用の帰納法が役立つ。

```lean
def down : Nat → Nat
  | 0 => 0
  | n + 1 => down n

example (n : Nat) : down n = 0 := by
  fun_induction down n <;> simp_all [down]
```

`fun_induction down n` は、関数について生成された帰納法の原理を使う。再帰呼出しについて帰納法の仮定が得られる。

`induction n` は自然数のコンストラクターに沿う。`fun_induction` は関数の分岐と再帰呼出しに沿う、という違いがある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`fun_induction`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.funInduction)。

[タクティクス一覧に戻る](README.md)
