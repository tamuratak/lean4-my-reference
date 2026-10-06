# 論理の記号：`∧`・`∨`・`¬`・`↔`・`∃`

論理の記号は、命題から別の命題を作る記法である。命題の形によって、証明として何を渡すかが変わる。

| 記法 | 意味 | 証明に必要なもの |
| --- | --- | --- |
| `P ∧ Q` | `P` かつ `Q` | 両方の証明 |
| `P ∨ Q` | `P` または `Q` | どちらか一方の証明と、その側の指定 |
| `¬ P` | `P` ではない | `P` の証明から矛盾を導く関数 |
| `P ↔ Q` | `P` と `Q` は同値 | `P → Q` と `Q → P` の両方向の証明 |
| `∃ x : α, R x` | 条件を満たす `x` が存在する | 値 `x` と `R x` の証明 |

論理積は両方の証明をまとめる。論理和は `Or.inl` または `Or.inr` で側を指定する。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := ⟨hp, hq⟩
example (P Q : Prop) (hp : P) : P ∨ Q := Or.inl hp
example (P Q : Prop) (hq : Q) : P ∨ Q := Or.inr hq
```

否定 `¬ P` は `P → False` の略である。`False` は矛盾を表す命題で、コンストラクターを持たない。

```lean
example (P : Prop) (hp : P) (hnp : ¬ P) : False := hnp hp
```

同値では、二つの向きの含意をまとめる。

```lean
example (P Q : Prop) (f : P → Q) (g : Q → P) : P ↔ Q := ⟨f, g⟩
```

存在命題は、証人となる値とその条件の証明を渡す。

```lean
example : ∃ n : Nat, n = 3 := ⟨3, rfl⟩
```

`∧` と `∨` は右結合で、`∧` の方が強く結び付く。`P ∧ Q ∨ R` は `(P ∧ Q) ∨ R`、`P ∧ Q ∧ R` は `P ∧ (Q ∧ R)` と読む。迷う場合は括弧で明示するとよい。

含意 `→` と全称量化 `∀` は[関数の型](function_types.md)を参照。証明を分解・構築する操作は、[タクティクス一覧](../tactics/README.md)にまとめている。

参照：[公式リファレンス：Basic Propositions](https://lean-lang.org/doc/reference/latest/Basic-Propositions/)。

[文法要素の一覧に戻る](README.md)
