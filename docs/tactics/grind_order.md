# `grind_order`

`grind_order` は、**`grind` の順序についての推論に絞って証明する**タクティクスである。

順序の推移性を使う例である。

```lean
example (a b c : Nat) (hab : a ≤ b) (hbc : b ≤ c) : a ≤ c := by
  grind_order
```

部分順序や線形順序について登録された情報を使う。数値の加算なども関わる場合は、`omega` や `grind` の算術機能が必要になることがある。

`grind_linarith` は線形算術の機能に絞る関連タクティクスである。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`grind_order`](https://lean-lang.org/doc/api/Init/Grind/Tactics.html#Lean.Parser.Tactic.grind_order)。

[タクティクス一覧に戻る](README.md)
