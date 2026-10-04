# `notation`・`infix`・`scoped`

`notation` は、**既存の式に対して、読み書きしやすい記法を付ける**構文である。記号の見た目だけでなく、何の式に対応するかを指定する。

```lean
section

local notation "three" => (3 : Nat)
example : three + 1 = 4 := rfl

end
```

この範囲では `three` が `3` の記法になる。`local` の記法は現在のセクションの終わりまで有効である。

二つの引数の間に置く記号は `infix` で定義できる。

```lean
def combine (x y : Nat) : Nat := x + y

infixl:65 " <+> " => combine

example : 2 <+> 3 <+> 4 = 9 := rfl
```

`infixl` は左結合なので、`2 <+> 3 <+> 4` は `(2 <+> 3) <+> 4` と読む。`65` は優先順位で、大きいほど強く結び付く。右結合なら `infixr` を使う。

名前空間を開いたときだけ使う記法には `scoped` を付ける。

```lean
namespace Demo

scoped notation "three" => (3 : Nat)

end Demo

open scoped Demo
example : three + 1 = 4 := rfl
```

`open scoped Demo` はスコープ付き記法などを有効にする。名前空間の普通の定義名まで短くするものではない。

記法は新しい数学的性質を証明するものではなく、式の書き方を増やすものである。一般的な構文や展開処理を定義する `syntax`・`macro` は、このページの対象には含めない。

参照：[公式リファレンス：Notations and Macros](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/)。

[文法要素の一覧に戻る](README.md)
