# `with_reducible`

`with_reducible` は、**内側のタクティクスで、定義の展開の強さを制限する**タクティクスである。

等しさを照合する際、どの定義を展開するかに関わる操作である。

```lean
abbrev twice (n : Nat) := n + n

example (n : Nat) : twice n = n + n := by
  with_reducible rfl
```

`with_reducible` は展開しやすい定義に絞り、`with_reducible_and_instances` は型クラスのインスタンスも含める。`with_unfolding_all` は通常の定義も強く展開し、`with_unfolding_none` は展開を制限する。

```lean
def twice (n : Nat) := n + n

example (n : Nat) : twice n = n + n := by
  with_unfolding_all rfl
```

展開の設定は内側の操作に対して適用される。普通の証明では先に `change`、`unfold`、`simp [定義名]` で必要な形を明示すると読みやすい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`with_reducible`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.withReducible)。

[タクティクス一覧に戻る](README.md)
