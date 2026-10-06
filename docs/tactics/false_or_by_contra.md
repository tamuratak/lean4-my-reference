# `false_or_by_contra`

`false_or_by_contra` は、ゴールの形に応じて仮定を導入し、最終的に `False` を示す形にするタクティクスである。

命題 `P` がゴールなら、通常は `¬ P` を仮定に追加して背理法の形にする。

```lean
example (P : Prop) (hp : P) : P := by
  false_or_by_contra
  contradiction
```

否定 `¬ P` は `P → False` なので、背理法を使う前に `P` を導入する。

```lean
example (P : Prop) (hnp : ¬ P) : ¬ P := by
  false_or_by_contra
  contradiction
```

既に `False` がゴールならそのままになる。導入される仮定に自分で名前を付けたい場合は、続けて `rename_i h` などを使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`false_or_by_contra`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.falseOrByContra)。

[タクティクス一覧に戻る](README.md)
