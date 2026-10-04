# `exact_mod_cast`

`exact_mod_cast` は、**型変換を整理し、渡した証明をゴールに合わせる**タクティクスである。

自然数の等式から、整数に変換した等式を証明する例である。

```lean
example (n m : Nat) (h : n = m) : (n : Int) = (m : Int) := by
  exact_mod_cast h
```

`exact h` のままでは証明の型とゴールの型が違う。`exact_mod_cast` は登録された型変換の補題を使って、その違いを整理する。

`apply_mod_cast` は前提を残す適用、`rw_mod_cast` は書き換え、`assumption_mod_cast` は仮定からの探索を、型変換の整理と組み合わせる変種である。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
