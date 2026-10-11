# 証明項と基本的な証明の一覧

証明項（proof term）は、命題を型として持つ項である。`P : Prop` に対して `t : P` が成り立つとき、項 `t` は命題 `P` の証明である。項とは、Lean で型を持つ式のことで、名前、関数適用、`fun` 式などが含まれる。

```lean
example : True := True.intro

example (P : Prop) (hp : P) : P := hp

example (P Q : Prop) (hp : P) (hpq : P → Q) : Q := hpq hp
```

`True.intro` は標準で用意された証明、`hp` は仮定として受け取った証明、`hpq hp` は証明を関数に渡して得た証明である。いずれも、`:=` の右側に要求される命題の型を持つため、そのまま証明として使える。

## 1. 既存の証明と一覧の範囲

Lean には、論理の基本操作に使うコンストラクターや定理と、自然数など個別の対象についての定理が用意されている。`True.intro` や `Eq.refl` はコンストラクター、`Eq.trans` や `Nat.add_comm` は定理、`rfl` は `Eq.refl` を使う定義である。宣言の種類は異なるが、必要な引数を渡して目的の命題の証明として使える。

```lean
example (m n : Nat) : m + n = n + m := Nat.add_comm m n
```

`Nat.add_comm m n` も証明項である。「用意されている証明」には標準ライブラリや mathlib の定理も含まれ、利用できる宣言は Lean のバージョンとインポートするモジュールによって変わる。証明項は既存宣言の適用や関数式などでも構成できるため、宣言名だけの一覧には収まらない。特定の環境の既存宣言だけなら有限だが、その宣言の一覧と、引数を渡した式も含む証明項の一覧は異なる。

基本的な論理と等式の操作は、次の表から選べる。個別の数学的対象については、対象の API ドキュメントにある定理を探す。

## 2. 命題の証明を構成する基本宣言

表の `hp : P`、`hq : Q`、`hpq : P → Q`、`hqp : Q → P` は、すでに使える証明を表す。`R : α → Prop` は述語、`x : α` は証人、`hx : R x` は証人が条件を満たす証明である。暗黙の引数は、期待される型から推論される。

| 宣言 | 証明項の書き方 | 得られる証明の型 |
| --- | --- | --- |
| [`True.intro`](https://lean-lang.org/doc/api/Init/Prelude.html#True.intro) | `True.intro` | `True` |
| [`trivial`](https://lean-lang.org/doc/api/Init/Core.html#trivial) | `trivial` | `True` |
| [`rfl`](https://lean-lang.org/doc/api/Init/Prelude.html#rfl) | `rfl` | `a = a`、または定義的に等しい等式 |
| [`Eq.refl`](https://lean-lang.org/doc/api/Init/Prelude.html#Eq.refl) | `Eq.refl a` | `a = a`、または定義的に等しい等式 |
| [`And.intro`](https://lean-lang.org/doc/api/Init/Prelude.html#And.intro) | `And.intro hp hq` | `P ∧ Q` |
| [`Or.inl`](https://lean-lang.org/doc/api/Init/Prelude.html#Or.inl) | `Or.inl hp` | `P ∨ Q` |
| [`Or.inr`](https://lean-lang.org/doc/api/Init/Prelude.html#Or.inr) | `Or.inr hq` | `P ∨ Q` |
| [`Iff.intro`](https://lean-lang.org/doc/api/Init/Core.html#Iff.intro) | `Iff.intro hpq hqp` | `P ↔ Q` |
| [`Exists.intro`](https://lean-lang.org/doc/api/Init/Core.html#Exists.intro) | `Exists.intro x hx` | `∃ x : α, R x` |

### 論理結合子の証明の構成

`And.intro hp hq` は、両方の証明をまとめて `P ∧ Q` の証明を作る。例えば、`hp : P` と `hpq : P → Q` があれば、関数適用 `hpq hp` で `Q` の証明を得てから組み合わせられる。

```lean
example (P Q : Prop) (hp : P) (hpq : P → Q) : P ∧ Q :=
  And.intro hp (hpq hp)
```

`Or.inl hp` は左側の命題 `P` の証明から、`Or.inr hq` は右側の命題 `Q` の証明から、`P ∨ Q` の証明を作る。渡していない側の命題は、期待される型から推論される。

```lean
example (P Q : Prop) (hp : P) : P ∨ Q := Or.inl hp

example (P Q : Prop) (hq : Q) : P ∨ Q := Or.inr hq
```

`Iff.intro hpq hqp` は、`P → Q` と `Q → P` の両方向の証明をまとめて `P ↔ Q` の証明を作る。`And.intro` と `Iff.intro` は、期待される型が分かっていれば、コンストラクターの省略記法 [`⟨…⟩`](../syntax/anonymous_constructor.md) でも書ける。

```lean
example (P Q : Prop) (hpq : P → Q) (hqp : Q → P) : P ↔ Q :=
  Iff.intro hpq hqp
```

### `rfl` の暗黙引数と定義的な等しさ

`rfl` は、概略として次のように定義されている。

```text
def rfl {α : Sort u} {a : α} : a = a := Eq.refl a
```

`Eq.refl a` では値 `a` を明示する。`rfl` では値も暗黙の引数なので、証明したい等式から推論される。`2 + 3` は計算すると `5` になるため、`2 + 3 = 5` は `5 = 5` と定義的に等しい型として扱われる。

```lean
example : 2 + 3 = 5 := rfl

example : 2 + 3 = 5 := Eq.refl 5
```

定義的な等しさは、定義の展開や計算によって一致することを意味する。すべての数学的な等式を `rfl` で証明できるわけではない。例えば任意の自然数についての加算の交換法則には、`Nat.add_comm m n` のような定理を使える。

## 3. 既存の証明を利用する基本宣言

既存の証明から成分を取り出したり、等式を組み合わせたりして、別の命題の証明を得られる。

| 宣言・操作 | 必要な証明など | 証明項の書き方 | 得られる証明の型 |
| --- | --- | --- | --- |
| `And.left`・`And.right` | `h : P ∧ Q` | `h.left`・`h.right` | `P`・`Q` |
| `Iff.mp`・`Iff.mpr` | `h : P ↔ Q`、`hp : P` または `hq : Q` | `h.mp hp`・`h.mpr hq` | `Q`・`P` |
| `Or.elim` | `h : P ∨ Q`、`f : P → S`、`g : Q → S` | `Or.elim h f g` | `S` |
| `Exists.elim` | `h : ∃ x : α, R x`、`f : ∀ x : α, R x → S` | `Exists.elim h f` | `S` |
| `False.elim` | `h : False` | `False.elim h` | 目的の命題 `P` |
| `absurd` | `hp : P`、`hnp : ¬ P` | `absurd hp hnp` | 目的の命題 `Q` |
| `Eq.symm` | `h : a = b` | `Eq.symm h` または `h.symm` | `b = a` |
| `Eq.trans` | `hab : a = b`、`hbc : b = c` | `Eq.trans hab hbc` または `hab.trans hbc` | `a = c` |
| `Eq.subst` | `hab : a = b`、`ha : R a` | `Eq.subst hab ha` | `R b` |
| `congrArg` | 関数 `f`、`hab : a = b` | `congrArg f hab` | `f a = f b` |
| `funext` | `h : ∀ x, f x = g x` | `funext h` | `f = g` |
| `propext` | `h : P ↔ Q` | `propext h` | `P = Q` |

表の `P`、`Q`、`S` は命題である。`Exists.elim` の結論 `S` は、存在命題から取り出す証人 `x` に依存しない。`funext` は点ごとの等しさから関数の等しさを得る。`propext` は命題の論理的同値から命題の等しさを得る公理であり、定理が使う公理は [`#print axioms`](../commands/print_axioms.md) で確認できる。

### 論理結合子の証明の利用

`h : P ∧ Q` からは、`h.left` で `P` の証明、`h.right` で `Q` の証明を取り出せる。`And.left h`・`And.right h` と書いても同じである。

```lean
example (P Q : Prop) (h : P ∧ Q) : P := h.left

example (P Q : Prop) (h : P ∧ Q) : Q := h.right
```

`h : P ↔ Q` からは、`h.mp : P → Q` と `h.mpr : Q → P` を取り出せる。対応する前提の証明を渡すと、反対側の命題の証明を得られる。

```lean
example (P Q : Prop) (h : P ↔ Q) (hp : P) : Q := h.mp hp

example (P Q : Prop) (h : P ↔ Q) (hq : Q) : P := h.mpr hq
```

`Or.elim h f g` は、`h : P ∨ Q` の場合分けによって共通の結論を得る。`f` は左側の証明を受け取る関数、`g` は右側の証明を受け取る関数で、どちらも同じ命題の証明を返す必要がある。次の例では、左側なら `hpq` を使い、右側なら受け取った `Q` の証明をそのまま返す。

```lean
example (P Q : Prop) (h : P ∨ Q) (hpq : P → Q) : Q :=
  Or.elim h hpq (fun hq => hq)
```

### 等式の証明の利用

`Eq.trans` は等式をつなぎ、`Eq.subst` は等しい値についての条件の証明を移す。`funext` と `propext` は、それぞれ点ごとの等しさと論理的同値から、関数と命題の等式の証明を得る。

```lean
example (α : Type) (a b c : α) (hab : a = b) (hbc : b = c) : a = c :=
  Eq.trans hab hbc

example (α : Type) (R : α → Prop) (a b : α) (hab : a = b) (ha : R a) : R b :=
  Eq.subst hab ha

example (α β : Type) (f g : α → β) (h : ∀ x, f x = g x) : f = g :=
  funext h

example (P Q : Prop) (h : P ↔ Q) : P = Q := propext h
```

## 4. 証明項の記法とタクティクス

証明項は宣言名のほか、関数やコンストラクターの記法でも書ける。

| 記法 | 意味 | 例 |
| --- | --- | --- |
| `fun` | 引数を受け取って証明を返す関数 | `fun hp => hp` は `P → P` の証明 |
| `⟨…⟩` | 期待される型のコンストラクターによる構成 | `⟨hp, hq⟩` は `P ∧ Q` の証明 |
| `‹P›` | 仮定から型 `P` の証明の取得 | `hp : P` があれば `‹P›` を使用可能 |
| `by …` | タクティクスによる項の構成 | `by exact hp` は `P` の証明 |

`fun` や `⟨…⟩` はデータの構成にも使える記法で、命題の型を持つときに証明項になる。`exact` や `apply` は、証明項を使ってゴールを解決するタクティクスである。タクティクスで構成した場合も、完成した証明項の型をカーネルが検査する。

```lean
example : 2 + 3 = 5 := rfl

example : 2 + 3 = 5 := by
  rfl

example : 2 + 3 = 5 := by
  exact rfl
```

最初の `rfl` は証明項、二つ目はタクティクス、三つ目はタクティクス `exact` に渡す証明項である。同じ名前でも、項を書く場所かタクティクスを書く場所かによって役割が変わる。

ゴールの型から証明を組み立てる過程は、[タクティクスの仕組みと利点](tactics.md)を参照。

## 5. 宣言の型の確認と定理の検索

`#check` は、既存の宣言の型や、引数を渡した証明項の型を表示する。定理の型を読むと、必要な引数と得られる結論が分かる。

```lean
#check True.intro
#check @And.intro
#check @Eq.trans
#check Nat.add_comm
#check Nat.add_comm 2 3
```

`Nat.add_comm` は任意の自然数に対する交換法則の証明であり、`Nat.add_comm 2 3` は特定の等式 `2 + 3 = 3 + 2` の証明である。`@` を付けると、暗黙の引数も明示して扱える。

標準ライブラリの宣言は[公式 API ドキュメント](https://lean-lang.org/doc/api/)の検索から探せる。mathlib で使う定理は、[mathlib のリファレンス](../mathlib/README.md)で対象ごとの説明を確認し、`#check` で実際の型を確認できる。[`exact?`](../tactics/exact_search.md)・[`apply?`](../tactics/apply_search.md) は、ゴールに使える証明や定理の候補を探す手段になる。

## 関連ページと参照

- [カリー・ハワード対応と Lean の命題・証明](curry_howard.md)：論理の推論と項の構成の対応。
- [`theorem`・`example`](../syntax/theorem.md)、[`exact`](../tactics/exact.md)、[`apply`](../tactics/apply.md)：証明の登録と利用。
- [公式リファレンス：Basic Propositions](https://lean-lang.org/doc/reference/latest/Basic-Propositions/)
- [公式 API：`Init.Core`](https://lean-lang.org/doc/api/Init/Core.html)、[`Init.Prelude`](https://lean-lang.org/doc/api/Init/Prelude.html)

[型と証明の基礎に戻る](README.md)
