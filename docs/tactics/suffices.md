# `suffices`

`suffices` は、**本来のゴールを証明するために十分な、別の命題を提示する**タクティクスである。

ゴールが `Q` で `h : P → Q` があれば、まず `P` を示せば十分である。

```lean
example (P Q : Prop) (h : P → Q) (hp : P) : Q := by
  suffices hP : P from h hP
  exact hp
```

`from h hP` は「`P` が証明できたら本来のゴール `Q` をどう閉じるか」を指定する。その後に残るゴールは `P` である。

`have` が必要な事実を追加してから先へ進むのに対し、`suffices` は先にゴールを閉じる道筋を示す。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
