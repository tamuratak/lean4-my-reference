# `delta`

`delta` は、**指定した定数を、その定義本体に置き換える**タクティクスである。

定義を直接開く操作である。

```lean
def twice (n : Nat) : Nat := n + n

example (n : Nat) : twice n = n + n := by
  delta twice
  rfl
```

`delta twice at h` で仮定の中を展開できる。

`unfold` は定義に対応する等式を利用するが、`delta` は定数の定義本体を直接展開する。再帰関数の内部表現まで開くと式が読みにくくなることがあるので、通常の証明では先に `unfold` や `simp [定義名]` を使うとよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`delta`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.delta)。

[タクティクス一覧に戻る](README.md)
