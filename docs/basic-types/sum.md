# `Sum α β`・`α ⊕ β`：直和

`Sum α β` は、`α` 型の値か `β` 型の値のどちらか一方を、その区別とともに保持する型である。`α ⊕ β` とも書き、直和型と呼ぶ。追加の `import` は不要である。

## 左右の値の作成

```lean
def byNumber : Nat ⊕ String := Sum.inl 3
def byName : Nat ⊕ String := Sum.inr "three"

example : (Nat ⊕ String) = Sum Nat String := rfl
example : byNumber = Sum.inl 3 := rfl
example : byName = Sum.inr "three" := rfl
```

`Sum.inl` は左側の型 `α` の値、`Sum.inr` は右側の型 `β` の値を渡すコンストラクターである。上の例では、番号で指定する場合と名前で指定する場合を１つの型にまとめている。

## 左右の値による場合分け

```lean
def describe (x : Nat ⊕ String) : String :=
  match x with
  | Sum.inl n => s!"number={n}"
  | Sum.inr name => "name=" ++ name

example : describe (Sum.inl 3) = "number=3" := by decide
example : describe (Sum.inr "three") = "name=three" := by decide
```

左の枝では `n : Nat`、右の枝では `name : String` が使える。どちらの枝も、関数の結果の型 `String` に合う値を返す。

左右の型が同じでも、コンストラクターの区別は残る。

```lean
example : (Sum.inl 3 : Nat ⊕ Nat) ≠ Sum.inr 3 := by decide
```

## ペア・存在の有無・論理和との違い

[`Prod α β`](prod.md) は両方の値を保持する。直和は一方の値だけを保持するので、左右の値を同時に取り出すことはできない。

[`Option α`](option.md) は値があるかないかを表す。直和は、右側にも `β` 型のデータを保持できるため、２種類の入力などを区別して扱う場合に使える。

命題 `P ∨ Q` は「どちらかが成り立つ」という論理和であり、データ型 `α ⊕ β` とは別のものである。`Sum` の名前は、この型の値を数値として足し合わせるという意味ではない。

参照：[公式リファレンス：Sum Types](https://lean-lang.org/doc/reference/latest/Basic-Types/Sum-Types/)。

[基本データ型の一覧に戻る](README.md)
