# Lean における識別子の特殊な記法

Lean では、通常は `x` や `selected` のような識別子を使う。識別子には通常の書き方に加えて、特殊な記法がある。このページでは、名前の前にドットを付ける `.some` と、名前を括弧で囲む `«a+b»` の二つの記法を説明する。

## 名前の前のドット `.名前`

`.some` のように名前の前にドットを置くと、期待される型の名前空間を利用して名前を探す。

```lean
def selected : Option Nat := .some 3
def absent : Option Nat := .none

example : selected = some 3 := rfl
example : absent = none := rfl
```

この例では期待される型が `Option Nat` なので、`.some` と `.none` は `Option.some` と `Option.none` として解決される。

型は、式に直接指定することもできる。

```lean
example : (.some 3 : Option Nat) = some 3 := rfl
```

入力される引数だけではなく、その式に何の型が期待されているかが重要である。名前を解決できない場合は、型を指定するか `Option.some` のように完全な名前を書く。

Lean における識別子は、変数や宣言などを指す名前である。先頭の `.名前` と名前を囲む `«…»` は、名前の書き方や解決に関わる記法である。

## 特殊な名前の括弧 `«…»`

`«…»` は、予約語や通常の識別子に使えない文字を含む名前を書くための括弧である。

```lean
namespace Demo

def «a+b» : Nat := 3
def «match» : Nat := 7

example : «a+b» + «match» = 10 := rfl

end Demo
```

`«a+b»` は一つの名前であり、`a + b` という加算ではない。`«match»` も、場合分けの構文ではなく宣言名である。

名前空間の区切りを含む名前では、一部分を囲める。

```lean
namespace Demo

def «a+b» : Nat := 3

end Demo

example : Demo.«a+b» = 3 := rfl
```

文字列の `"…"` とも異なる。普通に書ける名前なら通常の識別子を使い、この括弧は既存の特殊な名前を読む・参照するためにも覚えておくとよい。

参照：[公式リファレンス：Identifiers](https://lean-lang.org/doc/reference/latest/Terms/Identifiers/)、[公式 API：識別子の構文](https://lean-lang.org/doc/api/Lean/Parser/Extra.html#Lean.Parser.ident)。

[記号索引に戻る](../symbols.md) · [文法要素の一覧に戻る](README.md)
