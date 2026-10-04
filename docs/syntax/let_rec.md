# `let rec`

`let rec` は、**式の中で再帰的な補助関数を定義する**構文である。定義した関数を、その後の式で使える。

```lean
def sumUpTo (n : Nat) : Nat :=
  let rec loop : Nat → Nat
    | 0 => 0
    | k + 1 => loop k + k + 1
  loop n

example : sumUpTo 3 = 6 := rfl
```

`loop 0` は `0`、`loop (k + 1)` は `loop k` に次の数を足した値になる。最後の `loop n` が `sumUpTo` の返す値である。

補助関数の中で、外側の変数を使うこともできる。

```lean
def repeatAdd (x times : Nat) : Nat :=
  let rec loop : Nat → Nat
    | 0 => 0
    | k + 1 => loop k + x
  loop times

example : repeatAdd 3 4 = 12 := rfl
```

ここでは外側の `x` を固定して、残りの回数だけを減らす。再帰呼び出しのたびに `x` を渡し直す必要はない。

通常の `let f := …` は、定義中の `f` 自身を再帰的に呼ぶための構文ではない。再帰する場合に `rec` を付ける。

局所的な関数でも、通常の [`def` による再帰](recursive.md)と同様に停止が確認される。この二つの例は自然数の構造に従って再帰するので、自動で確認できる。

[`where`](where.md) は主要な定義の後に補助定義を添える。`let rec` は、式の途中に補助関数を置き、その後で呼び出す書き方である。

参照：[公式 API：`let rec`](https://lean-lang.org/doc/api/Lean/Parser/Term.html#Lean.Parser.Term.letrec)、[公式リファレンス：Recursive Definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/)。

[文法要素の一覧に戻る](README.md)
