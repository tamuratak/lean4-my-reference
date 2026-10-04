# 数学の概念を型で組み立て、性質を証明する

Lean では、**数学の対象を型と値で表し、命題を `Prop` に属する型で表し、その型の値を証明として扱う**。対象を構成する定義と、その性質を示す証明を、基本的な部品から積み重ねていく。

ここでは、自然数から実数を構成する数学的な方法は既知として、各段階を Lean のどの仕組みで書くかを説明する。実数の構成全体を実装するのではなく、仕組みが見える短い例を使う。

## 1. 型と値：数学の対象を表す

`n : Nat` は「`n` は自然数」、`s : Nat → Rat` は「`s` は自然数を添字とする有理数の列」を表す。`Nat` や `Rat` 自体は `Type` に属する型である。

数学での構成と Lean での表現は、次のように対応する。`ℕ`・`ℤ`・`ℚ` は、それぞれ `Nat`・`Int`・`Rat` の表記である。

| 数学の対象 | Lean での表現 | どのように作るか |
| --- | --- | --- |
| 自然数 | `Nat` | `0` から始め、「すでにある自然数に 1 を足す」ことで次の数を作る。 |
| 整数 | `Int` | 自然数 `n` を使い、`n` と `-(n + 1)` の二通りで、ゼロ以上の整数と負の整数を表す。 |
| 有理数 | `Rat` | 整数の分子と自然数の分母に、「分母はゼロでない」「既約である」という証明を添える。 |
| 有理数の列 | `ℕ → ℚ` | 項の番号を受け取り、その番号の有理数を返す関数で表す。 |
| 有理数のコーシー列 | `CauSeq ℚ abs` | 有理数の列に、「この列はコーシー列である」という証明を添える。 |
| 列を同一視したもの | `CauSeq.Completion.Cauchy (abs : ℚ → ℚ)` | 差が 0 に近づくコーシー列どうしを、同じ値として扱う新しい型を作る。 |
| 実数 | `Real`（`ℝ`） | 一つ前の段階で作った値を中に持つ型を作り、実数として扱う。 |

自然数・整数・有理数は Lean に用意されている。ここで述べるコーシー列と実数の実装は mathlib のものである。

## 2. 帰納型：値の作り方を指定する

`inductive` は、**その型の値を作る方法（コンストラクター）を指定する**。`Nat` の値はゼロか、ある自然数の後者である。`Int` の値は、自然数 `n` を非負整数とする `Int.ofNat n` か、`-(n + 1)` を表す `Int.negSucc n` である。

定義の形だけを抜き出すと、次のようになる。これは既存の型を説明する断片であり、再定義するコードではない。

```text
inductive Nat where
  | zero : Nat
  | succ : Nat → Nat

inductive Int where
  | ofNat : Nat → Int
  | negSucc : Nat → Int
```

帰納型を宣言すると、その構造に沿った場合分けや帰納法の原理も得られる。自然数についての証明なら、ゼロの場合と、後者の場合に分けられる。

```lean
example (n : Nat) : 0 + n = n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    change Nat.succ (0 + n) = Nat.succ n
    exact congrArg Nat.succ ih
```

後者の場合では、仮定 `ih : 0 + n = n` が使える。ゴールを後者どうしの等式に変え、等式の両辺に `Nat.succ` を適用する `congrArg` で証明する。**値の構成に沿って、性質も証明する**のである。

## 3. 構造体：データと条件の証明をまとめる

`structure` は複数のフィールドをまとめる。有理数 `Rat` は、実際には分数の商型ではなく、既約分数の形で実装されている。主なフィールドは次のとおりである。

```text
num     : Int
den     : Nat
den_nz  : den ≠ 0
reduced : num.natAbs.Coprime den
```

`num` と `den` はデータ、`den_nz` と `reduced` は条件の証明である。例えば `den_nz` の型は、同じ構造体に入っている `den` の値によって変わる。このように、**型が値に依存できる仕組みが依存型**である。

```lean
import Init.Data.Rat.Basic

def half : Rat where
  num := 1
  den := 2
  den_nz := by decide
  reduced := by decide

example : half.den ≠ 0 := half.den_nz
```

`half` を作る時点で必要な条件を証明しているので、使う側は `.den_nz` からその証明を取り出せる。毎回ゼロでないことを証明し直す必要はない。

有理数の足し算などを定義する際には、計算結果を既約化し、結果もこれらの条件を満たすことを証明する。型を作ることと、演算を定義してその法則を証明することは、それぞれ必要な作業である。

## 4. 関数型と部分型：列に条件を付ける

有理数の列は関数 `ℕ → ℚ` である。有限個の項を保存するリストではなく、任意の添字に対して項を与える。

```lean
import Init.Data.Rat.Basic

def constantSequence (q : Rat) : Nat → Rat := fun _ => q

example (q : Rat) (n : Nat) : constantSequence q n = q := rfl
```

次に、コーシー列であるという条件を `Prop` として定義する。mathlib の `IsCauSeq abs s` は、`s` がコーシー列であることを表す。この条件を列の型に付ける。

```text
CauSeq ℚ abs = {s : ℕ → ℚ // IsCauSeq abs s}
```

`{x : α // P x}` は**部分型**であり、値 `x` と証明 `h : P x` を `⟨x, h⟩` にまとめる。`.val` で値、`.property` で証明を取り出せる。より簡単な条件なら、次のように書ける。

```lean
def PositiveNat := {n : Nat // 0 < n}

def three : PositiveNat := ⟨3, by decide⟩

example (x : PositiveNat) : 0 < x.val := x.property
```

コーシー列も同じ仕組みで作る。ただし、`by decide` で具体的な数の条件を確かめる代わりに、その列についてコーシー条件の証明を渡す。

## 5. 商型：同値な列を同じ値にする

まず、コーシー列どうしの関係「差が 0 に近づく」を定義し、その反射性・対称性・推移性を証明する。**関係と同値関係であることの証明をまとめたものが `Setoid`**、それによって値を同一視する型が `Quotient` である。

仕組みだけなら、自然数を「2 で割った余りが等しい」で同一視する短い例で確認できる。

```lean
def sameParity : Setoid Nat where
  r a b := a % 2 = b % 2
  iseqv := ⟨fun _ => rfl, fun h => h.symm, fun h₁ h₂ => h₁.trans h₂⟩

def Parity := Quotient sameParity

def parityClass (n : Nat) : Parity := Quotient.mk sameParity n

example : parityClass 1 = parityClass 3 :=
  Quotient.sound (by decide : 1 % 2 = 3 % 2)

def remainder (q : Parity) : Nat :=
  Quotient.lift (fun n => n % 2) (fun _ _ h => h) q

example : remainder (parityClass 3) = 1 := rfl
```

`Quotient.mk` は代表元から商型の値を作る。`Quotient.sound` は、代表元どうしが関係を満たす証明を、商型での等式の証明に変える。`1` と `3` 自体を等しくするわけではない。

商型からの関数は `Quotient.lift` で定義する。その際、**同値な代表元なら結果も等しい**という証明が必要になる。上の `remainder` では、その条件が同値関係そのものなので、仮定 `h` を渡せる。商型の値について性質を証明する際には、`Quotient.inductionOn` により、代表元から作った値についての証明に帰着できる。

実数でも同様に、コーシー列の商を作る。実数の足し算を定義するには、列の各項を足した結果がコーシー列になることに加え、代表する列を取り替えても結果が同値になることを証明する。mathlib の `Real` は、こうして構成した商型を `cauchy` フィールドに持つ構造体である。

## 6. 命題と証明：必要な型の値を組み立てる

対象の型を作った後、その性質を命題として記述する。`P : Prop` に対する `h : P` は、**命題 `P` の型に属する値、つまり `P` の証明**である。

論理の操作は、証明の作り方と対応する。

| 証明したい命題 | 用意する証明 |
| --- | --- |
| `P ∧ Q` | `P` の証明と `Q` の証明をまとめたもの |
| `P → Q` | `P` の証明を受け取り、`Q` の証明を返す関数 |
| `∀ x : α, R x` | 任意の `x` を受け取り、`R x` の証明を返す関数 |
| `∃ x : α, R x` | 具体的な `x` と、`R x` の証明をまとめたもの |

例えば、証明済みの含意をつなぐ操作は関数適用になる。

```lean
theorem chain {P Q R : Prop} (hp : P) (hpq : P → Q) (hqr : Q → R) : R :=
  hqr (hpq hp)

example {P Q R : Prop} (hp : P) (hpq : P → Q) (hqr : Q → R) : R := by
  have hq : Q := hpq hp
  exact hqr hq
```

最初は `P` の証明 `hp` を持つ。`hpq hp` で `Q` の証明を作り、`hqr` に渡して `R` の証明を作る。二つ目の例は、その途中の証明に `hq` という名前を付けたものである。

`∀ x : α, R x` では、返す証明の型 `R x` が引数 `x` に依存する。数学の「任意の対象について、その対象の性質を示す」という操作も依存型で表せる。

タクティクは、この証明の値を作るための支援機能である。`intro` で引数を受け取り、`apply` で定理に必要な前提へゴールを分け、`exact` で要求された型の証明を渡す。最終的に Lean のカーネルが、できあがった値が目的の命題の型を持つか検査する。

## 7. 構成した後は、証明済みの性質を使う

実数を構成して演算を定義しただけでは、交換法則や完備性まで自動的に得られるわけではない。これらも構成に基づいて証明する。例えば加法の交換法則は、有理数の列の各項についての交換法則から、列、商型、実数へと引き継ぐ。

一度証明した性質は、新しい定理で使える。普段の実数の証明で、コーシー列の構成まで戻る必要はない。

```lean
import Mathlib.Basic.Real.Basic

example (x y : ℝ) : (x + y) + 0 = y + x := by
  calc
    (x + y) + 0 = x + y := add_zero (x + y)
    _ = y + x := add_comm x y
```

`add_zero` と `add_comm` は、実数にも適用できる証明済みの定理である。型クラスを通じて、実数に用意された演算と法則が選ばれる。この証明は、二つの等式の証明をつないで目的の等式の証明を作っている。

群などの抽象的な構造も、要素の型に演算と法則の証明を組み合わせて表す。型クラスにそれらをまとめれば、群一般について証明した定理を、その構造を持つ具体的な型で使える。

なお、型の検査で確認できるのは、**記述した定義と前提のもとで、その命題が証明されていること**である。意図した数学の概念を正しく定義したかは、定義自体を読む必要がある。証明が公理に依存する場合は、その公理も前提に含まれる。

## 関連ページと参照

- 個別の文法：[帰納型](syntax/inductive.md)、[構造体](syntax/structure.md)、[関数型](syntax/function_types.md)、[部分型](syntax/subtype.md)、[型クラス](syntax/class.md)。
- 個別の型：[自然数](basic-types/nat.md)、[整数](basic-types/int.md)、[有理数](basic-types/rat.md)、[商型](basic-types/quotient.md)。
- 公式リファレンス：[帰納型と構造体](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)、[部分型](https://lean-lang.org/doc/reference/latest/Basic-Types/Subtypes/)、[商型](https://lean-lang.org/doc/reference/latest/The-Type-System/Quotients/)、[命題と証明](https://lean-lang.org/doc/reference/latest/The-Type-System/Propositions/)。
- 公式 API：[有理数 `Rat` の定義](https://lean-lang.org/doc/api/Init/Data/Rat/Basic.html#Rat)。

[リファレンスのトップに戻る](../README.md)
