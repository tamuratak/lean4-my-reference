# `norm_cast`

`norm_cast` は、**型変換が絡む式を、登録された補題で整理する**タクティクスである。

自然数を整数に変換した等式から、元の自然数の等式へ戻す例である。

```lean
import Std.Tactic

example (n m : Nat) (h : (n : Int) = (m : Int)) : n = m := by
  norm_cast at h
```

この例では、整理した仮定がゴールと合うので、その場で証明が完了する。

`push_cast` は演算の外側にある変換を内側へ移す。

```lean
import Std.Tactic

example (n m : Nat) : ((n + m : Nat) : Int) = (n : Int) + (m : Int) := by
  push_cast
  rfl
```

変換には `↑` や `(n : Int)` という表記を使う。変換を整理できるかは、その型や演算についての補題が登録されているかによる。

`exact_mod_cast`、`apply_mod_cast`、`rw_mod_cast`、`assumption_mod_cast` は、型変換を整理しながらそれぞれの操作を行う変種である。

`norm_cast` は型変換を整理した後、`trivial` によるゴールの解決を試す。`norm_cast0` は同じ整理を行うが、この最後の処理を行わない。

```lean
import Std.Tactic

example (n m : Nat) (h : (n : Int) = (m : Int)) : n = m := by
  norm_cast0 at h
  exact h
```

`norm_cast0 at h` の後には `h : n = m` とゴール `n = m` が残るので、`exact h` が必要になる。最初の例の `norm_cast at h` は、最後の `trivial` が仮定を使ってゴールを閉じる。

参照：[公式 API：`norm_cast`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticNorm_cast__)、[公式 API：`norm_cast0`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.normCast0)。

[タクティクス一覧に戻る](README.md)
