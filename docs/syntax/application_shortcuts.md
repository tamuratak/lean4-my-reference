# 関数適用の `..`・`|>`・`<|`・関数合成 `∘`

これらは、引数の渡し方や関数を組み合わせる形を短く書く記法である。通常の `f x` や名前付き引数については [関数適用](application.md) を参照。

## 残りの引数を推論する `..`

関数適用の最後に `..` を付けると、残りの引数を推論用の穴として補う。定理の引数がゴールからわかる場合にも使える。

```lean
example (a b : Nat) : a + b = b + a := Nat.add_comm ..
```

ここでは結果に期待される型から、`Nat.add_comm` に渡す二つの自然数が決まる。明示すると `Nat.add_comm a b` である。

`..` は任意の証明を探索する命令ではない。推論に必要な情報がなければ失敗する。また、実際に入力するのは二つのピリオドであり、説明文で省略を示す `…` や三つのピリオド `...` とは区別する。

## 適用の向きを変える `|>` と `<|`

`x |> f` は `f x` と同じ適用で、入力を左に書く。連続して書くと、左から処理を追える。

```lean
def addOne (n : Nat) := n + 1
def double (n : Nat) := n * 2

example : (3 |> addOne |> double) = 8 := rfl
```

これは `double (addOne 3)` に相当する。

`f <| 式` は、右側の式全体を引数にする。括弧を減らして書きたい場合に使える。

```lean
def addOne (n : Nat) := n + 1
def double (n : Nat) := n * 2

example : (double <| addOne <| 3) = 8 := rfl
```

これも `double (addOne 3)` に相当する。`|>`・`<|` は関数適用、[<|>](monad_operators.md) は計算の候補を選ぶ演算子であり、別の記法である。

## 関数を作る `∘`

`f ∘ g` は、入力にまず `g`、次に `f` を適用する関数である。

```lean
def addOne (n : Nat) := n + 1
def double (n : Nat) := n * 2

example : (double ∘ addOne) 3 = 8 := rfl
```

`double ∘ addOne` は `fun x => double (addOne x)` に相当する。`3 |> addOne` が値を計算する適用であるのに対し、`double ∘ addOne` は入力を待つ関数を作る。

参照：[公式リファレンス：Function Application](https://lean-lang.org/doc/reference/latest/Terms/Function-Application/)、[公式 API：Function.comp](https://lean-lang.org/doc/api/Init/Prelude.html#Function.comp)。

[記号索引に戻る](../symbols.md) · [文法要素の一覧に戻る](README.md)
