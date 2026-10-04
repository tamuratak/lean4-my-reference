# `intros`

`intros` は、**導入できる引数や仮定をまとめて導入する**タクティクスである。

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

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
