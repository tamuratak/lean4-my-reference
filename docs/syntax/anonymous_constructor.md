# `⟨…⟩`・`(x, y)`

`⟨…⟩` は、**期待される型に合わせて、コンストラクターへ成分を渡す**記法である。型から使うコンストラクターが一意に決まる場合に使える。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q := ⟨hp, hq⟩
```

ここでは `P ∧ Q` が期待されるので、`⟨hp, hq⟩` は `And.intro hp hq` として読まれる。

存在命題では、最初の成分が証人、次が条件の証明になる。

```lean
example : ∃ n : Nat, n = 3 := ⟨3, rfl⟩
```

入れ子の構造はまとめて書ける。

```lean
example (P Q R : Prop) (hp : P) (hq : Q) (hr : R) : P ∧ Q ∧ R :=
  ⟨hp, hq, hr⟩
```

`P ∧ Q ∧ R` は `P ∧ (Q ∧ R)` なので、この `⟨hp, hq, hr⟩` は `⟨hp, ⟨hq, hr⟩⟩` に相当する。

ペアの値には `(x, y)` も使う。

```lean
def pair : Nat × String := (3, "three")

example : pair.1 = 3 := rfl
example : pair.2 = "three" := rfl
example : (⟨3, "three"⟩ : Nat × String) = pair := rfl
```

`.1` と `.2` は成分を取り出す。`(x, y)` はペアの記法であり、論理積の証明なども作れる `⟨…⟩` より用途が限定される。

[`rcases`](../tactics/rcases.md) のパターン内の `⟨…⟩` は中身を取り出す指定である。式として書く `⟨…⟩` は、逆に中身を渡して値や証明を作る。

参照：[公式リファレンス：Structures and Constructors](https://lean-lang.org/doc/reference/latest/Terms/Structures-and-Constructors/)。

[文法要素の一覧に戻る](README.md)
