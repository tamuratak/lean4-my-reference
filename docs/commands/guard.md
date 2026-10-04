# `#guard`

`#guard 条件` は、**条件を計算し、真になることを検査する**コマンドである。成功した場合は通常、何も表示しない。

```lean
#guard (2 + 3 == 5)
#guard ([1, 2, 3].length == 3)
```

`==` は `Bool` 型の比較であり、どちらも `true` になるので検査に通る。

判定可能な命題も渡せる。

```lean
#guard (2 + 3 = 5)
#guard (3 < 5)
```

この場合は、命題の判定を通じて真偽を調べる。`#guard false` のように偽になる条件を渡すとエラーになる。

関数の具体的な入力に対する、簡単な動作確認に使える。

```lean
def double (n : Nat) : Nat := n + n

#guard (double 3 = 6)
```

ただし、計算による検査であり、命題の証明を定理として登録するものではない。証明が必要なら `example` や `theorem` として書く。

`variable (n : Nat)` で用意した未指定の値については、具体的な計算ができないので、このコマンドで任意の `n` に対する性質を検査することはできない。

計算結果を表示するなら [`#eval`](eval.md)、式の定義上の一致を検査するなら [`#guard_expr`](guard_expr.md) を使う。

参照：[公式 API：`#guard`](https://lean-lang.org/doc/api/Init/Guard.html#Lean.Parser.Command.guardCmd)。

[`#` コマンドの一覧に戻る](README.md)
