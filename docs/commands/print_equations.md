# `#print equations`・`#print eqns`

`#print equations 名前` は、**関数の定義から生成された等式の定理を表示する**コマンドである。`#print eqns` は同じコマンドの短い書き方である。

```lean
def predecessor : Nat → Nat
  | 0 => 0
  | n + 1 => n

#print equations predecessor
```

`predecessor 0 = 0` と、任意の `n` に対する `predecessor (n + 1) = n` を表す定理が表示される。

定義を使って書き換えるときに、どの等式が用意されているかを確認できる。

```lean
def predecessor : Nat → Nat
  | 0 => 0
  | n + 1 => n

#print eqns predecessor

example (n : Nat) : predecessor (n + 1) = n := by
  simp [predecessor]
```

[`#print`](print.md) で関数の本体を表示すると、再帰の内部表現などが現れることがある。`#print equations` は、入力のパターンに沿った等式を読む用途に向いている。

表示される定理名は定義によって異なるので、名前を推測する前に確認するとよい。このコマンド自身が式を書き換えるわけではなく、書き換えに使える情報を表示する。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
