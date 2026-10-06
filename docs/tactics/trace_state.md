# `trace_state`

`trace_state` は、現在の仮定とゴールをメッセージに表示するタクティクスである。

タクティクスで証明状態がどう変わったかを調べるために使う。

```lean
example (P : Prop) : P → P := by
  intro hp
  trace_state
  exact hp
```

表示される状態は概ね次のようになる。

```text
P : Prop
hp : P
⊢ P
```

`trace "message"` や `dbg_trace "message"` は文字列を表示する関連操作である。どちらもそれだけではゴールを証明しない。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`trace_state`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.traceState)。

[タクティクス一覧に戻る](README.md)
