# `intros`

`intros` は、導入できる引数や仮定をまとめて導入するタクティクスである。

引数の数を一つずつ意識せず、仮定を取り出せる。

```lean
example (P Q : Prop) : P → Q → P := by
  intros
  assumption
```

この後のゴールは `P` で、`P` と `Q` の証明が仮定にある。名前も指定できる。

```lean
example (P Q : Prop) : P → Q → P := by
  intros hp hq
  exact hp
```

名前を省略した `intro` は一つ導入するが、名前を省略した `intros` は可能な分をまとめて導入する。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`intros`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.intros)。

[タクティクス一覧に戻る](README.md)
