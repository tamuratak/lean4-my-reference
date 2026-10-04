# `push_cast`

`push_cast` は、**型変換を演算の内側へ移して、変換後の演算に揃える**タクティクスである。

自然数の和を整数に変換した式を、整数の和へ変える例である。

```lean
example (n m : Nat) : ((n + m : Nat) : Int) = (n : Int) + (m : Int) := by
  push_cast
  rfl
```

変換の整理で式が反射的な等式になっても、この操作の後には `rfl` が必要なことがある。

`push_cast at h` と仮定も対象にできる。元の型への等式に戻すなど、より広い型変換の整理には `norm_cast` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`push_cast`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.pushCast)。

[タクティクス一覧に戻る](README.md)
