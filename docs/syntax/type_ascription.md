# 型の指定：`(e : α)`・`show … from …`

`(e : α)` は、**式 `e` を型 `α` として読むよう Lean に伝える**記法である。

```lean
#check (3 : Nat)
#check (3 : Int)
#check ([] : List Nat)
```

同じ `3` でも、指定した型によって自然数か整数かが決まる。空リストのように中身から型が分からない式にも使える。

宣言での `x : α` は名前の型を示し、式での `(e : α)` は既に書いた式に期待する型を与える。

```lean
def emptyNames : List String := []

example : emptyNames = ([] : List String) := rfl
```

`show α from e` は、型を先に書く形である。長い式や証明で、何を作るか先に示したいときに使える。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q :=
  show P ∧ Q from ⟨hp, hq⟩
```

`e` をタクティクスで作るなら、`show α by …` と書ける。

```lean
example (n : Nat) : n = n :=
  show n = n by
    rfl
```

型指定は、合わない型の値を自由に変換する命令ではない。Lean は指定した型で式を確認し、必要なら利用可能な型変換を補うが、型が合わなければエラーになる。

`by` の中でゴールを選び直す操作は、[タクティクスの `show`](../tactics/show.md)を参照。

参照：[公式リファレンス：Type Ascription](https://lean-lang.org/doc/reference/latest/Terms/Type-Ascription/)。

[文法要素の一覧に戻る](README.md)
