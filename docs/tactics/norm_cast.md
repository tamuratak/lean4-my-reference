# `norm_cast`

`norm_cast` は、**型変換が絡む式を、登録された補題で整理する**タクティクスである。

自然数を整数に変換した等式から、元の自然数の等式へ戻す例である。

```lean
example (n m : Nat) (h : (n : Int) = (m : Int)) : n = m := by
  norm_cast at h
```

この例では、整理した仮定がゴールと合うので、その場で証明が完了する。

`push_cast` は演算の外側にある変換を内側へ移す。

```lean
example (n m : Nat) : ((n + m : Nat) : Int) = (n : Int) + (m : Int) := by
  push_cast
  rfl
```

変換には `↑` や `(n : Int)` という表記を使う。変換を整理できるかは、その型や演算についての補題が登録されているかによる。

`exact_mod_cast`、`apply_mod_cast`、`rw_mod_cast`、`assumption_mod_cast` は、型変換を整理しながらそれぞれの操作を行う変種である。

`norm_cast0` は型変換の整理の基本処理を行う変種である。通常は `norm_cast` を使えばよい。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`norm_cast`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticNorm_cast__)。

[タクティクス一覧に戻る](README.md)
