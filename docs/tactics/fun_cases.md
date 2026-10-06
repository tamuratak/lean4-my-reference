# `fun_cases`

`fun_cases` は、関数の定義に沿って場合分けするタクティクスである。

関数がどのパターンの入力を受け取ったかで分けたいときに使う。

```lean
def mark : Nat → Bool
  | 0 => true
  | _ + 1 => false

example (n : Nat) : mark n = true ∨ mark n = false := by
  fun_cases mark n <;> simp [mark]
```

`fun_cases mark n` は、その関数について生成された場合分けの原理を使う。

`fun_induction` と違って、再帰呼出しに対する帰納法の仮定は作らない。入力の形に応じた分岐だけが必要なときに使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`fun_cases`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.funCases)。

[タクティクス一覧に戻る](README.md)
