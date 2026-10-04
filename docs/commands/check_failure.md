# `#check_failure`

`#check_failure 式` は、**その式の型の確認が失敗することを検査する**コマンドである。

```lean
#check_failure (true : Nat)
```

`true` は `Bool` 型なので、`Nat` としては確認できない。そのため、この失敗の検査は成功する。

関数の引数が合わないことも検査できる。

```lean
def addOne (n : Nat) : Nat := n + 1

#check_failure addOne "three"
```

`addOne` は自然数を受け取るので、文字列を渡すと型が合わない。

逆に、次の断片は式の型の確認に成功するので、`#check_failure` としてはエラーになる。

```text
#check_failure (3 : Nat)
```

通常の [`#check`](check.md) とは成功・失敗の判定が逆である。失敗時の情報がメッセージとして表示されることはあるが、検査が期待どおりならファイル全体のエラーにはしない。

特定の失敗理由やメッセージの文面まで確認したい場合は [`#guard_msgs`](guard_msgs.md) を使う。`#check_failure` は、その理由までは指定しない。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
