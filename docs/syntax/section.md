# `section`・`variable`・`include`

`section` は、**共通の変数や設定を使う範囲を区切る**構文である。`variable` で用意した変数は、その範囲の宣言で使える。

```lean
section

variable {α : Type} (x : α)

def keep := x

end

example : keep (3 : Nat) = 3 := rfl
```

`keep` は、概ね次の型で登録される。

```text
keep {α : Type} (x : α) : α
```

使った `x` と、その型に必要な `α` が引数になる。`end` の後も `keep` 自体は残るが、共通変数としての `x` は使えなくなる。

`section` に名前を付けても、宣言の名前に接頭辞は付かない。

```lean
section Demo

variable (n : Nat)
theorem selfEq : n = n := rfl

end Demo

example : 3 = 3 := selfEq 3
```

定理の引数は、原則として命題に現れる変数から決まる。証明の中でだけ使う共通仮定を追加するには `include` を使う。

```lean
section

variable (P : Prop) (hp : P)
include hp

theorem suppliedProof : P := hp

end

example (Q : Prop) (hq : Q) : Q := suppliedProof Q hq
```

ここでは `hp` を定理の引数に含めることで、証明内で使えるようにする。宣言した変数が何でも無条件に引数になるわけではない。

名前もまとめたいときは [`namespace`](namespace.md) を使う。`namespace` も変数や設定の範囲を区切る働きを持つ。

参照：[公式リファレンス：Namespaces and Sections / Section Variables](https://lean-lang.org/doc/reference/latest/Namespaces-and-Sections/)。

[文法要素の一覧に戻る](README.md)
