# `run_tac`

`run_tac` は、**タクティクスの実装用の Lean コードを、証明の途中で実行する**タクティクスである。

この操作にはメタプログラミング用の `Lean` モジュールが必要である。

```lean
import Lean

example : True := by
  run_tac Lean.Elab.Tactic.evalTactic (← `(tactic| exact True.intro))
```

この例では、タクティクスの構文を作り、それを実行している。

`run_tac` に書くのは一般の証明項ではなく、タクティクス実行環境で動くコードである。普通の証明を書く段階では、`exact True.intro` と直接書けばよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`run_tac`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.runTac)。

[タクティクス一覧に戻る](README.md)
