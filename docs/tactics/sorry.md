# `sorry`

`sorry` は、**まだ書けていない証明を、仮の穴として受け入れさせる**タクティクスである。

証明を途中まで書き、残りを後で埋めるための操作である。

```lean-incomplete
example (P : Prop) : P → P := by
  intro hp
  sorry
```

Lean は受け入れるが、宣言が `sorry` を使っているという警告を出す。これは完成した証明ではない。上の例なら `sorry` を `exact hp` に置き換えれば完成する。

`admit` も同じ用途で使える。`stop` はその後のタクティクスを実行せず、ゴールを仮の穴で閉じるデバッグ用の操作である。

このリファレンスでは、仮の穴を含む例を `lean-incomplete` と表示し、完成した証明の自動検証から除外する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`sorry`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticSorry)。

[タクティクス一覧に戻る](README.md)
