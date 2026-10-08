# `Quotient`：同じとみなす値をまとめる商型

`Quotient s` は、同値関係 `s` で結び付く値を等しいものとして扱う型である。例えば自然数を「２で割った余りが同じなら同じ」とみなすと、`0` と `2`、`1` と `3` をそれぞれ同じ商型の値として扱える。追加の `import` は不要である。

## `Setoid` による同値関係の指定

`Setoid α` は、関係 `r : α → α → Prop` と、その関係が反射的・対称的・推移的である証明をまとめる型クラスである。ここではインスタンスとして登録せず、名前付きの値を `Quotient` に明示して渡す。

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

`Quotient.mk s a` は、元の値 `a`（代表元）から商型の値を作る。`Quotient.sound` は `s.r a b` の証明を受け取り、商型での等式を返す。上の例では、自然数の `1` と `3` は異なるが、`parityClass 1` と `parityClass 3` は等しい。

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

`Quot r` は同値関係の証明を要求しない基礎となる仕組みである。同値関係で商を作る通常の用途では、関係と証明をまとめた `Setoid` を渡す `Quotient` が使いやすい。[部分型](../syntax/subtype.md)が条件を満たす値を選ぶのに対し、商型は元の値どうしを同じとみなす。

参照：[公式リファレンス：Quotients](https://lean-lang.org/doc/reference/latest/The-Type-System/Quotients/)。

[基本データ型の一覧に戻る](README.md)
