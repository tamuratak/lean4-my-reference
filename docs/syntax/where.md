# 補助定義の `where`

定義の本体に続く `where` は、**その定義で使う補助関数や補助的な値を、後ろにまとめて書く**構文である。

```lean
def doubledNext (n : Nat) : Nat := double (n + 1)
where
  double (k : Nat) : Nat := k + k

example : doubledNext 2 = 6 := rfl
```

本体では `double` を先に使い、その実装を `where` の後に書いている。`double` は入力を二倍にする補助関数である。

補助定義は、外側の引数を使うこともできる。

```lean
def addTwice (n x : Nat) : Nat := addN (addN x)
where
  addN (k : Nat) : Nat := k + n

example : addTwice 3 2 = 8 := rfl
```

ここでは `addN` が外側の `n` を使う。Lean は必要な外側の変数を、生成する補助定義の引数として補う。

補助定義には、外側の定義名に続く名前が付く。

```lean
def doubledNext (n : Nat) : Nat := double (n + 1)
where
  double (k : Nat) : Nat := k + k

#check doubledNext.double
example : doubledNext.double 4 = 8 := rfl
```

したがって、補助名 `double` をどこでも単独で使えるわけではないが、生成された定義は `doubledNext.double` として参照できる。完全に非公開にしたい場合は [`private`](visibility.md) も検討する。

[`let`](let.md) は式の途中で名前を導入する。`where` は、先に主要な処理を書き、補助定義を後ろに置くときに使いやすい。

[`structure`](structure.md) や `def p : Point where …` の `where` はフィールドを並べる区切りであり、ここで説明する補助定義とは別の用途である。

参照：[公式 API：補助定義の `where`](https://lean-lang.org/doc/api/Lean/Parser/Term.html#Lean.Parser.Term.whereDecls)、[公式リファレンス：Recursive Definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/)。

[文法要素の一覧に戻る](README.md)
