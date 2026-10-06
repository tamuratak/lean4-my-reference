# 式の `let`

`let` は、式の途中で値に名前を付け、その後の式で使う構文である。

```lean
def squareNext (n : Nat) : Nat :=
  let next := n + 1
  next * next

example : squareNext 3 = 16 := rfl
```

`next` はこの定義の本体だけで使える。`let` の後に続く最後の式 `next * next` が、全体の返す値になる。

型を明示したり、`;` で一行にまとめたりすることもできる。

```lean
example : (let x : Nat := 3; x + x) = 6 := rfl
```

`let x := 3` の `x` は値を持つ局所定義なので、Lean は計算時に `3` へ展開できる。

パターンで値の成分を取り出す書き方もある。

```lean
def sumPair (p : Nat × Nat) : Nat :=
  let (x, y) := p
  x + y

example : sumPair (2, 3) = 5 := rfl
```

`(x, y)` はペアの成分に名前を付ける。一般的な場合分けには [`match`](match.md) を使う。

[`def`](def.md) は後から呼び出せる名前を登録するが、`let` の名前は後続の式だけで使える。`by` の中で仮定に局所定義を追加する操作は、[タクティクスの `let`](../tactics/let.md)を参照。

局所的な関数が自身を再帰的に呼ぶ場合は [`let rec`](let_rec.md) を使う。

参照：[公式 API ドキュメント：式の `let`](https://lean-lang.org/doc/api/Lean/Parser/Term.html#Lean.Parser.Term.let)。

[文法要素の一覧に戻る](README.md)
