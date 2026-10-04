# `rcases`

`rcases` は、**仮定にある帰納型の値を、パターンに従ってまとめて分解する**タクティクスである。

例えば、`h : ∃ x, P x` に対して `rcases h with ⟨x, hx⟩` と書くと、証人 `x` とその条件 `hx : P x` を取り出せる。

```lean
example (α : Type) (P Q : α → Prop) (h : ∃ x, P x ∧ Q x) : ∃ x, Q x := by
  rcases h with ⟨x, hp, hq⟩
  exact ⟨x, hq⟩
```

このように、入れ子の存在命題と論理積も一度に分解できる。

```text
x  : α
hp : P x
hq : Q x
```

論理和のように複数のコンストラクターがある場合は、`|` で場合分けする。

```lean
example (P Q R S : Prop) (h : (P ∧ Q) ∨ (R ∧ S)) : Q ∨ S := by
  rcases h with ⟨hp, hq⟩ | ⟨hr, hs⟩
  · exact Or.inl hq
  · exact Or.inr hs
```

`|` がコンストラクターごとの場合分け、`⟨...⟩` が中身の分解を表す。不要な成分の名前には `_` を使える。

`rcases` は、複数回の `cases` をパターンでまとめて書くためのタクティクスと考えるとよい。

`rcases? h` は分解するパターンの候補を提案する。`rcases` を自分で書く前に、値の構造を確認したい場合に使える。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`rcases`](https://lean-lang.org/doc/api/Init/RCases.html#Lean.Parser.Tactic.rcases)。

[タクティクス一覧に戻る](README.md)
