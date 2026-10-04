# `ext1`

`ext1` は、**外延性の定理を一段階だけ適用する**タクティクスである。

`ext` による分解が進みすぎる場合に、段階を区切れる。

```lean
example (f g : Nat → Nat) (h : ∀ n, f n = g n) : f = g := by
  ext1 n
  exact h n
```

この例では関数の入力 `n` を導入し、`f n = g n` が残る。

構造体の各成分を比較する場合にも使える。さらに成分が構造体であっても、自動で何段も分解したくないときに便利である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`ext1`](https://lean-lang.org/doc/api/Init/Ext.html)。

[タクティクス一覧に戻る](README.md)
