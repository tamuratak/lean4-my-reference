# `let`

`let` は、証明の途中で、値を持つ局所的な定義を作るタクティクスである。

`let n := 3` とすると、`n` を値が `3` の名前として使える。

```lean
example : ∃ n : Nat, n = 3 := by
  let n : Nat := 3
  exact ⟨n, rfl⟩
```

`have hp : P := ...` は事実を追加するために、`let n : Nat := ...` は計算に使う値を定義するために使う、と考えるとよい。

局所定義の値は定義上の等しさの判定で展開できる。この例で `rfl` が使えるのは、`n` が `3` と定義されているからである。

`let'` は内部で `refine'` に対応する処理を使う変種である。`let rec` は局所的な再帰関数を定義するための構文で、再帰定義の停止性の条件も満たす必要がある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`let`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticLet__)。

[タクティクス一覧に戻る](README.md)
