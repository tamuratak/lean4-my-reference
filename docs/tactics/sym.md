# `sym`

`sym` は、**共有された式の表現を使う証明モードで、簡単化や推論を実行する**タクティクスである。

`grind` に関連する高度な操作であり、`sym =>` の中では通常のタクティクスとは別の構文を使う。

```lean
example (n : Nat) : 0 + n = n := by
  sym =>
    simp [Nat.zero_add]
```

この例では、そのモードの簡単化によって等式を閉じる。

通常の証明では `rfl` や `simp` と直接書けばよい。`sym` の内側で使える操作や設定は通常の証明モードと同じとは限らないため、より細かな制御が必要なときに公式リファレンスを確認する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`sym`](https://lean-lang.org/doc/api/Init/Grind/Tactics.html#Lean.Parser.Tactic.sym)。

[タクティクス一覧に戻る](README.md)
