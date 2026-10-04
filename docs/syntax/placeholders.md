# 推論用の `_` と未完成の `?_`

式の `_` は、**周囲の型や引数から Lean に推論させる部分**を表す。必ずしも未完成の証明ではない。

```lean
def keep {α : Type} (x : α) : α := x

example : @keep _ (3 : Nat) = 3 := rfl
```

`@keep` の最初の引数は型である。次の引数が `Nat` 型なので、`_` は `Nat` と決まり、この例は完成している。

ただし、情報がなければ推論できない。

```text
def unknown : Nat := _
```

この断片は、自然数であることしか分からず、どの値かを決められないのでエラーになる。`_` は Lean に任意の値や証明を探させる命令ではない。

`?_` は、タクティクスによる証明の途中で、明示的に残したい穴に使う。

```lean-incomplete
example (P Q : Prop) (hp : P) : P ∧ Q := by
  refine ⟨hp, ?_⟩
```

この段階では `Q` を証明するゴールが残る。

```text
P Q : Prop
hp : P
⊢ Q
```

完成するには、そのゴールも証明する必要がある。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := by
  refine ⟨hp, ?_⟩
  exact hq
```

パターンの `_` は、推論用の穴ではなく「その成分に名前を付けず、どんな値でも受け取る」という意味になる。[`match`](match.md) を参照。

参照：[公式リファレンス：Holes](https://lean-lang.org/doc/reference/latest/Terms/Holes/)。

[文法要素の一覧に戻る](README.md)
