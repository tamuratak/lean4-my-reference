# `#check`

`#check` は、式や宣言の型を確認し、メッセージとして表示するコマンドである。ファイルの中に直接書き、`by` の外で使う。

```lean
#check Nat
#check (3 : Nat)
#check Nat.add
```

概ね次の情報が表示される。

```text
Nat : Type
3 : Nat
Nat.add : Nat → Nat → Nat
```

`Nat` は型、`3` は自然数の値、`Nat.add` は自然数を二つ受け取る関数である。宣言名だけでなく、引数を渡した式も確認できる。

```lean
def double (n : Nat) : Nat := n + n

#check double
#check double 3
#check (rfl : 3 = 3)
```

`double` は `Nat → Nat`、`double 3` は `Nat`、最後の項は命題 `3 = 3` の証明として確認される。

`#check` は計算結果を表示するものではない。`double 3` の結果 `6` を見たい場合は [`#eval`](eval.md) を使う。

また、`#check` の表示には、まだ決まっていない型が残ることがある。

```lean
#check fun x => [x]
```

`x` の型を指定していないので、表示には `?m.…` という未確定の部分が現れることがある。`#check` が通ったことだけで、そのまま完成した定義として登録できるとは限らない。

定義の本体まで見るなら [`#print`](print.md)、型の確認が失敗することを検査するなら [`#check_failure`](check_failure.md) を使う。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
