# `unfold`

`unfold` は、**指定した定義を、その定義式に従って展開する**タクティクスである。

名前で隠れている計算の中身を見たいときに使う。

```lean
def twice (n : Nat) : Nat := n + n

example (n : Nat) : twice n = n + n := by
  unfold twice
  rfl
```

`unfold twice at h` と書けば、仮定 `h` の中を展開する。

再帰的な定義では、定義に対応する等式を使って展開する。単純な略記を開くだけなら `dsimp [twice]` や `simp [twice]` でも扱える。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`unfold`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.unfold)。

[タクティクス一覧に戻る](README.md)
