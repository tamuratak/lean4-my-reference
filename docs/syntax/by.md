# `by`：タクティクスによる項の作成

`by` は、**タクティクスで作った証明や値を、一つの項として使う**構文である。

```lean
example (P : Prop) (hp : P) : P := by
  exact hp
```

`:=` の右側に必要なのは `P` 型の項である。`by` に入ると、Lean はそれをゴールとして表示する。

```text
P  : Prop
hp : P
⊢ P
```

`exact hp` がゴールの証明を渡し、`by` 全体が `P` の証明になる。ここで `by` は式を始める文法、`exact` は内側で使うタクティクスである。

普通の式の中にも置ける。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q :=
  ⟨hp, by exact hq⟩
```

この `by` に期待される型は `Q` なので、内側のゴールも `Q` になる。

命題以外の値を作ることもできる。

```lean
def three : Nat := by
  exact 3

example : three = 3 := rfl
```

複数行のタクティクスは、`by` より深く字下げし、同じ段階の命令を揃える。未解決のゴールが残ったままでは完成した項にならない。

命令の使い方は[タクティクス一覧](../tactics/README.md)を参照。

参照：[公式リファレンス：Tactic Proofs](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/)。

[文法要素の一覧に戻る](README.md)
