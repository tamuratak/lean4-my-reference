# `grind`

`grind` は、等式、論理的な仮定、算術などを組み合わせて自動で証明を探すタクティクスである。

等式から関数の値が等しいことを推論できる。

```lean
example (f : Nat → Nat) (a b : Nat) (h : a = b) : f a = f b := by
  grind

example (P Q : Prop) (hp : P) (h : P → Q) : Q := by
  grind
```

定義についての補題を渡すこともできる。

```lean
def twice (n : Nat) : Nat := n + n

theorem twice_eq (n : Nat) : twice n = n + n := rfl

example (n : Nat) : twice n = n + n := by
  grind [twice_eq]
```

`grind [補題名]` で探索に使う事実を追加する。`grind only [...]` は登録済みの定理の使用を制限するが、仮定や基本的な推論まで無効にする意味ではない。

`grind?` は証明に使った情報に基づく書き方を提案する。`simp` のような書き換えだけでなく、複数の推論方法を連携させるため、簡単化だけでは届かない証明にも使える。

`grind => ...` は、`grind` 専用の操作を明示して探索を制御するための構文である。内部の命令と、普通の `by` の中のタクティクスは同じとは限らない。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`grind`](https://lean-lang.org/doc/api/Init/Grind/Tactics.html#Lean.Parser.Tactic.grind)。

[タクティクス一覧に戻る](README.md)
