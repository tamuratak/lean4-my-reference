# `Unit`・`Empty`：値が１つの型と値がない型

`Unit` は値が１つだけあるデータ型、`Empty` は値が１つもないデータ型である。「情報を持たない値がある」ことと「値がない」ことを区別する。追加の `import` は不要である。

## `Unit` は `()` を持つ

```lean
def result : Unit := ()

example : result = Unit.unit := rfl
example (u : Unit) : u = () := by
  cases u
  rfl
```

`()` はコンストラクター `Unit.unit` の記法である。`u : Unit` を場合分けしても形は１つだけなので、どの値も `()` と等しい。

関数が具体的な結果を返す必要がないときにも使う。

```lean
def ignore (_ : Nat) : Unit := ()

example : ignore 3 = () := rfl
example : (some () : Option Unit) ≠ none := by decide
```

`ignore` の返す値に入力の情報は残らない。`some ()` は「値がある」状態なので、`none` とは異なる。入出力を行う関数の `IO Unit` も、実行後の戻り値に具体的な情報を持たせないときによく使われる。

## `Empty` にはコンストラクターがない

```lean
def impossibleValue {α : Type} (e : Empty) : α := nomatch e
```

`e : Empty` が与えられたと仮定すると、対応するコンストラクターが１つもないため、[`nomatch`](../tactics/nomatch.md) で処理できる。どの結果の型 `α` に対しても関数を定義できるが、実際に渡せる `Empty` の値はない。

空リスト `[] : List Nat` や `none : Option Nat` は、それぞれの型の実際の値である。`Empty` には、そのような「空を表す値」もない。

## `True`・`False` との違い

`True` と `False` は `Prop` に属する命題である。`True` には証明があり、`False` には証明がない。一方、`Unit` と `Empty` は `Type` に属するデータ型である。形は対応していても、データと命題の役割は異なる。[`Prop`・`Type`](../syntax/universes.md)も参照。

参照：[公式リファレンス：The Unit Type](https://lean-lang.org/doc/reference/latest/Basic-Types/The-Unit-Type/)、[The Empty Type](https://lean-lang.org/doc/reference/latest/Basic-Types/The-Empty-Type/)。

[基本データ型の一覧に戻る](README.md)
