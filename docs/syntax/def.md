# `def`・`abbrev`

`def` は、値や関数に名前を付け、後から使える定義として登録する構文である。

```text
def 名前 (引数 : 型) : 結果の型 := 本体
```

`:` の右側が型、`:=` の右側が実際の値や計算である。

```lean
def double (n : Nat) : Nat := n + n

#eval double 3
example : double 3 = 6 := rfl
```

`double` は `Nat → Nat` 型の関数になる。`double 3` と書くと、引数 `n` に `3` を渡した結果を得られる。`#eval` の出力は `6` である。

引数がなければ、単に値を定義する。

```lean
def greeting : String := "hello"

#eval greeting
```

## `where` による構造体の値の定義

構造体の値を定義するときは、`:= 本体` の代わりに `where` を書き、その後ろにフィールドごとの値を並べられる。

```lean
structure Point where
  x : Nat
  y : Nat

def p : Point where
  x := 2
  y := 3

example : p = ({ x := 2, y := 3 } : Point) := rfl
example : p.x = 2 := rfl
example : p.y = 3 := rfl
```

`structure Point where …` はフィールドの名前と型を宣言し、`def p : Point where …` はそのフィールドに値を渡して `p` を定義する。後者は `def p : Point := { x := 2, y := 3 }` と同じ意味である。詳しい構築方法やフィールドの更新は、[構造体のページ](structure.md)を参照。

ここでの `where` は、構造体の値を作るための区切りである。定義の本体の後ろに補助関数を置く [`where`](where.md) とは用途が異なる。

## `abbrev`：展開されやすい別名

`abbrev` も定義を作るが、Lean が型を合わせる際に、通常の `def` より積極的に本体を展開する。型などの短い別名を作りたいときに使える。

```lean
abbrev Names := List String

def guests : Names := ["Ada", "Emmy"]
example : guests.length = 2 := rfl
```

`def` は名前を登録する。[`let`](let.md) は式の中だけで使う名前を作る。[`theorem`](theorem.md) は証明済みの命題を登録する。

補助関数を後ろに添える [`where`](where.md)、名前の範囲を指定する [`private`・`protected`](visibility.md)、実行不能な定義の [`noncomputable`](noncomputable.md) は、それぞれ別のページで説明する。

参照：[公式リファレンス：Definitions](https://lean-lang.org/doc/reference/latest/Definitions/Definitions/)。

[文法要素の一覧に戻る](README.md)
