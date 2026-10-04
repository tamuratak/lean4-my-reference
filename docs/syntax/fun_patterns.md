# パターンを使う `fun`

`fun` の引数には、**受け取った値の成分を、その場で取り出すパターン**を書ける。

```lean
def sumPair : Nat × Nat → Nat := fun (x, y) => x + y

example : sumPair (2, 3) = 5 := rfl
```

ペア全体に名前を付けてから `.1`・`.2` を使う代わりに、二つの成分を直接 `x`・`y` と呼ぶ。

複数の形を持つ型では、`fun` の後に分岐を並べることもできる。

```lean
def valueOrZero : Option Nat → Nat := fun
  | none => 0
  | some n => n

example : valueOrZero none = 0 := rfl
example : valueOrZero (some 7) = 7 := rfl
```

これは入力を受け取って [`match`](match.md) する関数を、一度に書く記法である。`|` が分岐、`=>` の右側が返す式になる。

他の関数へ渡す、その場限りの関数にも使える。

```lean
#eval [(1, 2), (3, 4)].map (fun (x, y) => x + y)
```

出力は `[3, 7]` である。ペアの型はリストの要素から推論される。

`fun (x : Nat) => …` の括弧は引数の型指定、`fun (x, y) => …` の括弧とカンマはペアのパターンである。

`fun (x, y) => …` のように一つのパターンだけを書く場合は、すべての入力をそのパターンで扱える必要がある。`Option` の `some` だけでは `none` を扱えないので、上のように全場合を覆う分岐を書く。

匿名関数の基本形と `·` による省略形は [`fun`](fun.md) を参照。

参照：[公式リファレンス：Pattern Matching / Pattern Matching Functions](https://lean-lang.org/doc/reference/latest/Terms/Pattern-Matching/)。

[文法要素の一覧に戻る](README.md)
