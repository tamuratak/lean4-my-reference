# `with_reducible`

`with_reducible` は、内側のタクティクスで、定義の展開の強さを制限するタクティクスである。

等しさを照合する際、どの定義を展開するかに関わる操作である。

```lean
import Std.Tactic

abbrev twice (n : Nat) := n + n

example (n : Nat) : twice n = n + n := by
  with_reducible rfl
```

これらは、内側の操作で定義上の等しさを照合する際の透明性設定を変える。

| 書き方 | その透明性設定で自動展開できる定義 |
| --- | --- |
| `with_reducible` | `abbrev` や `[reducible]` の定義 |
| `with_reducible_and_instances` | 上記に加えて、型クラスのインスタンス |
| `with_unfolding_all` | `opaque` を除くすべての定義 |
| `with_unfolding_none` | なし。`abbrev` も自動展開しない |

```lean
import Std.Tactic

def twice (n : Nat) := n + n

example (n : Nat) : twice n = n + n := by
  with_unfolding_all rfl
```

`with_reducible` は展開する定義を絞るが、`with_unfolding_none` はその透明性設定による定義の自動展開を許さない。

```lean
import Std.Tactic

abbrev twice (n : Nat) := n + n

example (n : Nat) (h : n + n = 0) : twice n = 0 := by
  fail_if_success with_unfolding_none exact h
  with_reducible exact h
```

`fail_if_success` は、内側の操作が失敗することを確認する。この例では `with_unfolding_none exact h` は `twice n` と `n + n` を照合できず失敗し、`with_reducible exact h` は `abbrev` を展開できるので成功する。これは定義の自動展開の設定であり、`unfold twice` のような明示的な展開を禁止する操作ではない。

展開の設定は内側の操作に対して適用される。普通の証明では先に `change`、`unfold`、`simp [定義名]` で必要な形を明示すると読みやすい。

参照：[公式 API：`with_reducible`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.withReducible)、[公式 API：`with_unfolding_none`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.withUnfoldingNone)。

[タクティクス一覧に戻る](README.md)
