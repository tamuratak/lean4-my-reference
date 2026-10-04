# `def`・`abbrev`

`def` は、**値や関数に名前を付け、後から使える定義として登録する**構文である。

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
