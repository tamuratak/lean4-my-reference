# 式の `if … then … else …`

`if` は、**条件に応じて二つの式のどちらかを返す**構文である。

```lean
def larger (x y : Nat) : Nat :=
  if x ≤ y then y else x

example : larger 2 5 = 5 := rfl
example : larger 7 3 = 7 := rfl
```

`x ≤ y` が成り立つなら `y`、成り立たないなら `x` を返す。両方の分岐は、全体に期待される同じ型の値を返す必要がある。

条件を `h` と名付けると、分岐の中でその条件の証明を使える。

```lean
def firstOrZero (xs : List Nat) : Nat :=
  if h : 0 < xs.length then xs[0]'h else 0

example : firstOrZero [8, 9] = 8 := rfl
example : firstOrZero [] = 0 := rfl
```

`then` 側では `h : 0 < xs.length`、`else` 側では `h : ¬ (0 < xs.length)` が使える。この例は `then` 側の証明で、添字 `0` が範囲内であることを示す。

条件には `Decidable`、つまり真偽を判定する仕組みが必要である。自然数の比較には既に用意されている。任意の `P : Prop` がそのまま計算で判定できるわけではない。

`Bool` 型の条件も書ける。

```lean
def label (b : Bool) : String := if b then "yes" else "no"

example : label true = "yes" := rfl
```

値のコンストラクターごとに分けるなら [`match`](match.md)、`by` 内で証明の分岐を選ぶ場合は[タクティクスの `if`](../tactics/if.md)を参照。

パターンに一致するかで分岐し、その成分も取り出す場合は [`if let`](if_let.md) を使える。

参照：[公式リファレンス：Conditionals](https://lean-lang.org/doc/reference/latest/Terms/Conditionals/)。

[文法要素の一覧に戻る](README.md)
