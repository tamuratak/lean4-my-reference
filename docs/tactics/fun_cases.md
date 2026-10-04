# `fun_cases`

`fun_cases` は、**関数の定義に沿って場合分けする**タクティクスである。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
