# `simp_all`

`simp_all` は、ゴールと仮定を、互いの情報を使って繰り返し簡単化するタクティクスである。

仮定 `hp : P` があれば、別の仮定にある `P` も真として簡単化できる。

```lean
example (P Q : Prop) (hp : P) (h : P → Q) : Q := by
  simp_all

example (n : Nat) (h : n = 3) : 0 + n = 3 := by
  simp_all
```

`simp at *` は各仮定とゴールの簡単化を行う。`simp_all` は簡単化後の仮定をさらに他の簡単化に使い、情報が行き渡るように繰り返す。

`simp_all only [...]` で補題を制限できる。`simp_all!` は展開を積極的に行い、`simp_all?` と `simp_all?!` は使った補題に基づく提案を表示する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`simp_all`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.simpAll)。

[タクティクス一覧に戻る](README.md)
