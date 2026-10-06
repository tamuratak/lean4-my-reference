# `get_elem_tactic`

`get_elem_tactic` は、添字アクセスに必要な、添字が範囲内にあるという条件を証明するタクティクスである。

`xs[i]` のようなアクセスには、通常 `i < xs.length` の証明が必要になる。

```lean
example (xs : Array Nat) (i : Nat) (h : i < xs.size) : i < xs.size := by
  get_elem_tactic
```

手元の仮定や算術の自動化で、この条件を閉じることを試す。添字アクセスの記法から自動で呼ばれることも多い。

```lean
example : (#[10, 20, 30] : Array Nat)[1] = 20 := by
  rfl
```

`get_elem_tactic_trivial` や `get_elem_tactic_extensible` は、この自動処理を構成・拡張するための関連操作である。

証明を明示する `xs[i]'h`、範囲外を `none` にする `xs[i]?`、範囲外でパニックを起こす `xs[i]!` の違いは[添字アクセス](../syntax/indexing.md)を参照。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`get_elem_tactic`](https://lean-lang.org/doc/api/Init/Tactics.html)。

[タクティクス一覧に戻る](README.md)
