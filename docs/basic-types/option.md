# `Option α`：値があるかないか

`Option α` は、**`α` 型の値が１つある場合と、値がない場合を表すデータ型**である。見つからない可能性のある検索や、要素のない可能性がある取り出しなどに使う。

`Option` 自体は型クラスではない。`Option Nat` は自然数の有無、`Option String` は文字列の有無を表す型になる。追加の `import` は不要である。

## `some` と `none`

値の形は、`some x` と `none` の２つだけである。それぞれコンストラクター `Option.some`、`Option.none` の短い名前である。

```lean
def present : Option Nat := some 3
def absent : Option Nat := none

example : present = Option.some 3 := rfl
example : absent = Option.none := rfl
example : (some 0 : Option Nat) ≠ none := by
  decide
```

`some 0` は「値 `0` がある」、`none` は「値がない」であり、区別される。`none` だけでは中身の型が決まらないので、必要なら `(none : Option Nat)` のように型を指定する。

## 中身を使う

`Option Nat` と `Nat` は別の型なので、`some 3` をそのまま自然数として足すことはできない。まず値の形で分ける。

```lean
def valueOrZero (x : Option Nat) : Nat :=
  match x with
  | some n => n
  | none => 0

example : valueOrZero (some 7) = 7 := rfl
example : valueOrZero none = 0 := rfl
```

`some n` の枝では、中身の `n : Nat` が使える。`none` の枝には中身がないので、ここでは代わりに `0` を返す。構文は [`match`](../syntax/match.md)や [`if let`](../syntax/if_let.md)を参照。

既定値で取り出すだけなら、`.getD` を使える。

```lean
example : (some 7 : Option Nat).getD 0 = 7 := rfl
example : (none : Option Nat).getD 0 = 0 := rfl
```

`.getD d` は、`some x` なら `x`、`none` なら指定した既定値 `d` を返す。「値がなかった」という情報を残したいときは、`Option` のまま扱う。

## 値がある場合だけ変換する

```lean
example : (some 3 : Option Nat).map (fun n => n + 1) = some 4 := rfl
example : (none : Option Nat).map (fun n => n + 1) = none := rfl
example : (some 3 : Option Nat).map toString = some "3" := by
  decide
```

`.map` は、`some` の中身にだけ関数を適用し、`none` はそのまま残す。`Nat → String` のような関数を使えば、結果の型も `Option Nat` から `Option String` に変わる。

次の関数自身も `Option` を返す場合は、`.bind` でつなげる。

```lean
def smallerThanTen? (n : Nat) : Option Nat :=
  if n < 10 then some n else none

example : (some 3 : Option Nat).bind smallerThanTen? = some 3 := rfl
example : (some 12 : Option Nat).bind smallerThanTen? = none := rfl
example : (none : Option Nat).bind smallerThanTen? = none := rfl
```

`.bind` は、`some n` なら関数を呼んでその結果を返し、`none` なら関数を呼ばず `none` を返す。`.map` で同じ関数を使うと結果は `Option (Option Nat)` になるが、`.bind` では `Option Nat` になる。`>>=` や `do` による書き方は[計算をつなぐ演算子](../syntax/monad_operators.md)と [`do` 記法](../syntax/do.md)を参照。

## リストの取り出しとの組み合わせ

```lean
example : ([10, 20] : List Nat).head? = some 10 := rfl
example : ([] : List Nat).head? = none := rfl
```

[`List α`](list.md) は０個以上の要素を持つリスト、`Option α` は値の有無を表す型である。リストから先頭を取り出す `.head?` は、空の場合も扱うため `Option α` を返す。

参照：[公式リファレンス：Optional Values](https://lean-lang.org/doc/reference/latest/Basic-Types/Optional-Values/)。

[基本データ型の一覧に戻る](README.md)
