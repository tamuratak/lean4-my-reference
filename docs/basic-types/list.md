# `List α`：リスト

`List α` は、**`α` 型の要素を順序付きで並べるデータ型**である。空でもよく、同じ値を複数回含めることもできる。`List Nat` は自然数のリスト、`List String` は文字列のリストになる。

`List` 自体は型クラスではない。要素の型を渡した `List α` が、リストの値の型になる。追加の `import` は不要である。

## 値を作る

```lean
def numbers : List Nat := [1, 2, 3]
def words : List String := ["Lean", "List"]
def empty : List Nat := []

example : numbers.length = 3 := rfl
example : words.length = 2 := rfl
example : empty.length = 0 := rfl
```

`[…]` はリストの値、`[]` は空リストを表す。要素はすべて指定した要素型に合う必要がある。空リストだけでは要素型が決まらないので、周囲の型から分からないときは `([] : List Nat)` のように指定する。

リストは、空の `List.nil` と、先頭と残りを組み合わせる `List.cons` の２つのコンストラクターでできている。通常はそれぞれ `[]`、`x :: xs` と書く。

```lean
example : ([] : List Nat) = List.nil := rfl
example : 1 :: [2, 3] = List.cons 1 [2, 3] := rfl
example : [1, 2, 3] = 1 :: (2 :: (3 :: [])) := rfl
```

`::` は要素を先頭に付け、`++` は２つのリストをつなぐ。要素を付ける操作と、リストどうしをつなぐ操作を区別する。

```lean
example : 0 :: [1, 2] = [0, 1, 2] := rfl
example : ([1, 2] : List Nat) ++ [3, 4] = [1, 2, 3, 4] := rfl
```

## 空かどうかで分ける

```lean
def first? (xs : List Nat) : Option Nat :=
  match xs with
  | [] => none
  | x :: _ => some x

example : first? [] = none := rfl
example : first? [7, 8] = some 7 := rfl
```

`[]` の枝には要素がない。`x :: xs` の形で分解すれば、先頭 `x : Nat` と残り `xs : List Nat` が使える。ここでは残りを使わないので `_` と書いている。

結果の [`Option Nat`](option.md) は、先頭があれば `some x`、なければ `none` になる。標準の `List.head?` でも先頭をこの形で取り出せる。

## よく使う操作

```lean
example : ([1, 2, 3] : List Nat).head? = some 1 := rfl
example : ([] : List Nat).head? = none := rfl
example : ([1, 2, 3] : List Nat).tail = [2, 3] := rfl
example : ([10, 20] : List Nat)[1]? = some 20 := rfl
example : ([10, 20] : List Nat)[2]? = none := rfl
example : ([1, 2, 3] : List Nat).map (fun n => n + 1) = [2, 3, 4] := rfl
example : ([1, 2, 3] : List Nat).filter (fun n => n > 1) = [2, 3] := rfl
```

`.length` は要素数、`.head?` は先頭の有無、`.tail` は先頭を除いた残りを返す。空リストの `.tail` は空リストになる。`xs[i]?` は０から数えた添字の要素を取り出し、範囲外なら `none` を返す。

`.map` は各要素に関数を適用し、`.filter` は真偽値を返す条件で要素を選ぶ。上の `.filter` の条件は `Bool` を返すことが期待されるため、命題 `n > 1` は自動で判定される。

`List` と `Array` は別の型である。`[1, 2, 3]` はリスト、`#[1, 2, 3]` は配列の記法であり、相互に置き換わるわけではない。[リテラルの記法](../syntax/literals.md)と[添字アクセス](../syntax/indexing.md)も参照。

参照：[公式リファレンス：Linked Lists](https://lean-lang.org/doc/reference/latest/Basic-Types/Linked-Lists/)。

[基本データ型の一覧に戻る](README.md)
