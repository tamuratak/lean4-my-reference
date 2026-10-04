# 数値・文字列・リスト・配列の記法

リテラルは、**具体的な値を直接書く記法**である。同じ表記でも、周囲の型によって意味が決まるものがある。

```lean
#check (3 : Nat)
#check (3 : Int)
#check (-3 : Int)
```

数値の `3` は自然数にも整数にも使える。`-3` は負号を適用した式であり、整数を意図するときは `Int` と明示すると分かりやすい。

文字列は二重引用符、文字は単一引用符で囲む。

```lean
#check "hello"
#check 'a'
#eval "hello" ++ " Lean"
```

`"hello"` は `String`、`'a'` は `Char` 型である。`++` は文字列を連結し、この出力は `"hello Lean"` になる。

リストは `[…]`、配列は `#[…]` と書く。

```lean
def numbers : List Nat := [1, 2, 3]
def values : Array Nat := #[1, 2, 3]

example : numbers.length = 3 := rfl
example : values.size = 3 := rfl
example : 0 :: numbers = [0, 1, 2, 3] := rfl
```

`::` はリストの先頭に要素を付ける。リストと配列は別の型なので、括弧の違いに注意する。各要素は共通の要素型に合う必要がある。

空の場合には、要素型を指定する必要があることが多い。

```lean
#check ([] : List Nat)
#check (#[] : Array String)
```

引数宣言の `[ToString α]` はリストの値ではなく、[`インスタンス引数`](binders.md)である。

参照：[公式リファレンス：Numeric Literals](https://lean-lang.org/doc/reference/latest/Terms/Numeric-Literals/)。

[文法要素の一覧に戻る](README.md)
