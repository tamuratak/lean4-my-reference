# `trace_state`

`trace_state` は、**現在の仮定とゴールをメッセージに表示する**タクティクスである。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
