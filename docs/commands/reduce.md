# `#reduce`

`#reduce` は、**式を定義上の計算で展開し、これ以上その計算で簡単にならない形を表示する**コマンドである。

```lean
def double (n : Nat) : Nat := n + n

#reduce double 3
```

出力は `6` になる。具体的な値の場合は [`#eval`](eval.md) と同じ結果になることもあるが、使う計算の仕組みが違う。

`#reduce` は関数の内側も展開する。

```lean
#reduce (fun n : Nat => n + 0)
#reduce (fun n : Nat => 0 + n)
```

最初は `fun n => n` になる。自然数の加算は右の引数について再帰的に定義されているので、`n + 0` はそのまま `n` へ計算できる。

一方、`0 + n` では未知の `n` について再帰する必要があり、単に `n` という形にはならない。出力には再帰の内部表現が現れる。この違いは [`rfl`](../tactics/rfl.md) で証明できる等式を理解する助けになる。

本体を展開しない [`opaque`](../syntax/opaque_axiom.md) では、実行結果との差が分かる。

```lean
opaque hidden : Nat := 3

#eval hidden
#reduce hidden
```

`#eval` の出力は `3`、`#reduce` の出力は `hidden` である。

通常の計算結果を知りたいなら `#eval`、定義がどこまで展開されるかを調べたいなら `#reduce` を使う。既定では式の中の証明や型の展開を省く部分があり、必要なら `(proofs := true)`・`(types := true)` を付けて指定できる。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
