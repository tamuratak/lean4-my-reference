# `intro`

`intro` は、**ゴールの引数や仮定を、名前を付けて取り出す**タクティクスである。

例えば、ゴールが `P → Q → P` なら、`intro hp hq` によって前提を取り出せる。

```text
hp : P
hq : Q
⊢ P
```

`∀ n : Nat, ...` のような全称量化でも、`intro n` で変数を取り出せる。

```lean
example (P Q : Prop) : P → Q → P := by
  intro hp hq
  exact hp

example : ∀ n : Nat, n = n := by
  intro n
  rfl
```

`intros` は導入できる引数をまとめて導入する。名前を指定しないと Lean が名前を選ぶので、後で使う仮定には `intro hp` のように名前を付けると読みやすい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
