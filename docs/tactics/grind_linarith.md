# `grind_linarith`

`grind_linarith` は、**`grind` の線形算術の機能に絞って証明する**タクティクスである。

変数を一次式として扱える関係に使う。

```lean
example (x y : Int) (h : x ≤ y) : x + 1 ≤ y + 1 := by
  grind_linarith
```

利用できる型は、線形算術の構造が登録されているものに依存する。整数の離散的な性質も使うなら `lia`、自然数と整数の線形算術なら `omega` も選択肢になる。

`grind` は算術に加えて等式や論理の推論も連携させる。まず `grind` で証明できたものを、必要に応じて機能を絞って書ける。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
