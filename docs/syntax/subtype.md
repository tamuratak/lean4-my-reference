# 部分型：`{x : α // P x}`

`{x : α // P x}` は、`α` 型の値と、その値が条件 `P` を満たす証明をまとめる型である。

```lean
def three : {n : Nat // n > 0} := ⟨3, by decide⟩

example : three.val = 3 := rfl
example : three.val > 0 := three.property
```

`⟨3, by decide⟩` は、値 `3` と `3 > 0` の証明を渡している。`.val` で値、`.property` で条件の証明を取り出せる。

関数の入力に使うと、条件を満たす値だけを受け取れる。

```lean
def positiveValue (x : {n : Nat // n > 0}) : Nat := x.val

example : positiveValue ⟨2, by decide⟩ = 2 := rfl
```

単に `(2 : Nat)` を渡すだけでは、その値について必要な証明がない。値を部分型の中へ入れる側で条件を証明する必要がある。

存在命題 `∃ x : α, P x` も値と証明を組にするが、それ自体は `Prop` の命題である。部分型は条件付きのデータとして値を保持し、`.val` を計算に使える。

２番目に条件の証明ではなく、１番目の値に応じた型のデータを保持したい場合は、[依存ペア型 `Σ x : α, β x`](sigma.md) を使う。

また、`{α : Type}` のような引数の波括弧は暗黙の引数であり、`//` を含むこの部分型の記法とは違う。

参照：[公式リファレンス：Subtypes](https://lean-lang.org/doc/reference/latest/Basic-Types/Subtypes/)。

[文法要素の一覧に戻る](README.md)
