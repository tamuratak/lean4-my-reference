# `syntax`・`macro`・`macro_rules`

`syntax` は、新しい書き方を Lean が構文として読めるようにするコマンドである。`macro_rules` は、その書き方を既存の構文へ展開する規則を与える。

```lean
import Lean

syntax "twice(" term ")" : term

macro_rules
  | `(twice($x:term)) => `($x + $x)

example : twice(3) = 6 := rfl
```

`syntax` の引用符の部分はそのまま書く文字列、途中の `term` は一つの式が入る場所である。最後の `: term` は、新しい構文全体も式として使えることを指定する。

`syntax` だけでは、その式が何を意味するかは決まらない。この例では `macro_rules` が `twice(3)` を `3 + 3` の構文へ展開し、その後で型や証明が確認される。

展開規則には、構文の引用と埋め込みを使う。

```text
`( … )      構文を引用する
$x          取り出した構文を埋め込む
$x:term     式の構文としてパターンから取り出す
```

ここでのバッククォートは Markdown の区切りではなく、Lean の構文の一部である。`x` は自然数の値ではなく、入力された式の構文を表す。

`macro` は、構文の宣言と一つの展開処理をまとめて書く形式である。

```lean
import Lean

macro "succ!(" x:term ")" : term => `($x + 1)

example : succ!(3) = 4 := rfl
```

`macro_rules` は複数のパターンを並べる場合にも使える。

```lean
import Lean

syntax "answer" : term
syntax "answer+(" term ")" : term

macro_rules
  | `(answer) => `((42 : Nat))
  | `(answer+($x:term)) => `(42 + $x)

example : answer = 42 := rfl
example : answer+(3) = 45 := rfl
```

`macro_rules` の `| … => …` は構文を照合するパターンであり、自然数やリストの値を場合分けする [`match`](match.md) とは処理する対象が違う。

単純な別名や演算子の記法なら [`notation`・`infix`](notation.md) が簡潔である。構文をパターンで読み替える必要がある場合に、これらの構文拡張を使う。このページでは基本的な展開だけを扱い、構文木を操作する一般的なメタプログラムまでは扱わない。

参照：[公式リファレンス：Notations and Macros](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/)、[公式リファレンス：Macros](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/Macros/)。

[文法要素の一覧に戻る](README.md)
