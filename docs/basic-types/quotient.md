# `Quotient`：同じとみなす値をまとめる商型

商型は、ある規則で同じとみなす値をまとめ、新しい型の値として扱うための仕組みである。Lean では `Quotient` を使って商型を作れる。追加の `import` は不要である。

例えば自然数を偶奇でまとめる商型では、`1` と `3` は同じ値になる。商型の値を表す自然数 `1` や `3` を、その値の代表元と呼ぶ。

## 商型の構成と値の等式

同一視する値の型を `α` とする。自然数を偶奇でまとめる例では、`α` は `Nat` である。`Quotient` で商型を作るには、`α` のどの値どうしを同一視するかを同値関係で指定する。Lean では、同値関係と同値関係であることの証明を `s : Setoid α` にまとめ、`Quotient s` によって商型を作る。

次の例では、`sameParity` が「２で割った余りが等しい」という規則を指定し、`Parity` がその規則で自然数をまとめた商型になる。`r` が関係の定義、`iseqv` が同値関係であることの証明である。

```lean
def sameParity : Setoid Nat where
  r a b := a % 2 = b % 2
  iseqv := {
    refl := fun _ => rfl
    symm := fun h => h.symm
    trans := fun h₁ h₂ => h₁.trans h₂
  }

def Parity := Quotient sameParity

def parityClass (n : Nat) : Parity := Quotient.mk sameParity n

example : parityClass 1 = parityClass 3 :=
  Quotient.sound (by decide : 1 % 2 = 3 % 2)

def remainder (q : Parity) : Nat :=
  Quotient.lift (fun n => n % 2) (fun _ _ h => h) q

example : remainder (parityClass 3) = 1 := rfl
```

`Quotient sameParity` は、偶奇によって自然数をまとめた型である。`parityClass n` は自然数 `n` から作った商型の値であり、`parityClass 1 = parityClass 3` は、奇数の代表元を `1` としても `3` としても同じ値になることを表す。

`Quotient.mk s a` は、代表元 `a` から商型の値を作る。`Quotient.sound` は `s.r a b` の証明を受け取り、商型での等式を返す。上の例では、`1 % 2 = 3 % 2` の証明から `parityClass 1 = parityClass 3` の証明を作っている。

この等式は、代表元の値が同じになるという意味ではない。関係によって等しいとみなすことを証明しているため、一般には `rfl` の代わりに `Quotient.sound` を使う。

## 商型から値を返す関数の定義と証明条件

`Quotient.lift f h` は、代表元に適用する関数 `f : α → β` を、商型からの関数にする。証明 `h` に求められる形は次のとおりである。

```text
∀ a b, s.r a b → f a = f b
```

つまり、同じとみなす代表元に対して、関数の結果も等しい必要がある。上の `remainder` は余りを返すので条件を満たす。代表元そのものを返す `fun n => n` は、同じ商型の値から `1` と `3` という異なる結果を返してしまうため、この商型では使えない。

代表元を選び直すことと、商型から計算可能な関数を定義することは別の操作である。商型を普通のペアのように分解し、任意の代表元を計算用に取り出すことはできない。

## 商型の性質の証明

```lean
example {α : Type} (s : Setoid α) (P : Quotient s → Prop)
    (h : ∀ a, P (Quotient.mk s a)) (q : Quotient s) : P q := by
  induction q using Quotient.inductionOn with
  | h a => exact h a
```

`Quotient.inductionOn` によって、任意の商型の値についての証明を、代表元 `a : α` から作った値についての証明に帰着できる。商型を使う関数の定義には `lift`、性質の証明にはこの帰納原理を使う。

## `Setoid α`

`Setoid α` は、型 `α` の値どうしを「同じとみなす」ための同値関係を、証明とともにまとめる型クラスである。例えば自然数の偶奇だけに注目するなら、２で割った余りが等しいことを同値関係として指定する。

`Setoid α` の値 `s` には、次の二つのフィールドがある。

| フィールド | 型 | 意味 |
| --- | --- | --- |
| `s.r` | `α → α → Prop` | 二つの値が同じとみなせる、という命題を返す関係 |
| `s.iseqv` | `Equivalence s.r` | 関係 `s.r` の反射性・対称性・推移性の証明 |

例えば `s.r a b` は、「`a` と `b` が関係 `s.r` で結び付く」という命題である。`Equivalence s.r` は、次の三つの証明をまとめる構造体である。

| 性質 | 証明のフィールド | 必要な証明 | 意味 |
| --- | --- | --- | --- |
| 反射性 | `s.iseqv.refl` | `∀ a, s.r a a` | 各値を自分自身と同じとみなせる |
| 対称性 | `s.iseqv.symm` | `∀ {a b}, s.r a b → s.r b a` | 同じとみなす関係の向きを逆にできる |
| 推移性 | `s.iseqv.trans` | `∀ {a b c}, s.r a b → s.r b c → s.r a c` | 同じとみなす関係をつなげられる |

関係を定義しただけでは、三つの性質の証明は自動的には得られない。例えば自然数の大小関係 `a ≤ b` は反射的・推移的だが、対称的ではないので、そのまま `Setoid Nat` の関係にはできない。

### `sameParity` の証明条件

偶奇の例の `sameParity.r a b` は、`a % 2 = b % 2` という命題である。`iseqv` の三つの証明には、余りの等式の性質を使っている。

`refl` では、各自然数 `a` に対する `a % 2 = a % 2` を `rfl` で証明する。`symm` では、仮定 `h : a % 2 = b % 2` の向きを `h.symm` で逆にする。`trans` では、二つの等式 `a % 2 = b % 2` と `b % 2 = c % 2` を `h₁.trans h₂` でつなぐ。

### インスタンスによる同値関係の記法

`[Setoid α]` としてインスタンスを利用する場合、その同値関係を `a ≈ b` と書ける。反射性・対称性・推移性には、それぞれ `Setoid.refl`、`Setoid.symm`、`Setoid.trans` を使える。

```lean
example {α : Type} [Setoid α] (a : α) : a ≈ a :=
  Setoid.refl a

example {α : Type} [Setoid α] {a b : α} (h : a ≈ b) : b ≈ a :=
  Setoid.symm h

example {α : Type} [Setoid α] {a b c : α}
    (hab : a ≈ b) (hbc : b ≈ c) : a ≈ c :=
  Setoid.trans hab hbc
```

名前付きの値 `s : Setoid α` を直接使う場合は `s.r a b` と書き、証明には `s.iseqv.refl a`、`s.iseqv.symm h`、`s.iseqv.trans hab hbc` を使える。`≈` の記法ではインスタンスから関係を選び、`s.r` の記法では関係を明示する。

定義済みの `sameParity` を証明内でインスタンスとして使うには、`letI : Setoid Nat := sameParity` と書く。その範囲では、自然数の `a ≈ b` は `a % 2 = b % 2` を意味する。

`Setoid α` の指定だけで、型 `α` の等号 `=` の意味が変わることはない。偶奇の関係では自然数の `1` と `3` を同じとみなせるが、`1 = 3` は成立しない。`a ≈ b` と型 `α` での `a = b` を区別し、商型での等式が必要なときに `Quotient.sound` を使う。

## `Quot` と `Quotient` の関係

`Quot r` は同値関係の証明を要求しない基礎となる仕組みである。同値関係で商を作る通常の用途では、関係と証明をまとめた `Setoid` を渡す `Quotient` が使いやすい。[部分型](../syntax/subtype.md)が条件を満たす値を選ぶのに対し、商型は同値関係で結び付く値どうしを同一視する。

参照：[公式リファレンス：Quotients](https://lean-lang.org/doc/reference/latest/The-Type-System/Quotients/)、[公式 API：`Setoid`](https://lean-lang.org/doc/api/Init/Core.html#Setoid)、[公式 API：`Equivalence`](https://lean-lang.org/doc/api/Init/Core.html#Equivalence)。

[基本データ型の一覧に戻る](README.md)
