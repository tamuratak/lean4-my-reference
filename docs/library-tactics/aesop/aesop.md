# `aesop`・`aesop?`

`aesop` は、論理の分解・簡単化・仮定や登録された補題の適用を組み合わせ、証明を探索するタクティクスである。Aesop パッケージが提供し、mathlib の依存にも含まれている。

```lean
import Aesop

example (P Q R : Prop) (h : P ∧ Q) (f : Q → R) : R ∧ P := by
  aesop
```

この例では `h` を分解して `P` と `Q` を取り出し、`f` で `R` を証明して、ゴールの論理積を組み立てる。手で書くと次の証明になる。

```lean
import Aesop

example (P Q R : Prop) (h : P ∧ Q) (f : Q → R) : R ∧ P := by
  rcases h with ⟨hp, hq⟩
  exact ⟨f hq, hp⟩
```

仮定の論理和による場合分けも探索に含まれる。

```lean
import Aesop

example (P Q R : Prop) (h : P ∨ Q) (f : P → R) (g : Q → R) : R := by
  aesop
```

`aesop?` は、探索した証明に対応するタクティクス列を提案する。提案の細部は、使える規則やバージョンによって変わる。

```lean
import Aesop

example (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
  aesop?
```

Lean 本体の `simp` は主に登録された書き換え規則で簡単化する。Aesop は簡単化に加えて、ゴールの分解や補題の適用を探索する。mathlib の全定理を無条件に検索するわけではなく、利用する規則や探索の制限によって成功する範囲が変わる。

算術や多項式の問題には [linarith](../mathlib/linarith.md)・[ring](../mathlib/ring.md) などの専用タクティクスも使う。独自の補題を探索に加える方法は [規則の追加](rules.md) を参照。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（標準タクティクスとの比較用）。Aesop の仕様資料については[検証・参照方針](../README.md#検証と参照方針)を参照。

[Aesop タクティクス一覧に戻る](README.md)
