# `#check`・`#eval`・`#print`

`#check` は型、`#eval` は実行結果、`#print` は宣言の内容を表示する。**コードを読みながら確認するためのコマンド**である。

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

`#check` は値を実行するのではなく、式が正しい型を持つか確認する。

`#eval` は計算を実行して結果を表示する。

```lean
#eval 2 + 3
#eval [1, 2, 3].length
```

順に `5` と `3` が表示される。結果を表示できる型の値を使う必要がある。計算結果が見えたこと自体は、定理として等式を登録したことにはならない。

`#print` は名前を指定して、既存の宣言を確認する。

```lean
def double (n : Nat) : Nat := n + n

#check double
#print double
```

`#check double` では `Nat → Nat` という型、`#print double` では定義の本体も確認できる。

型が期待どおりか迷ったときは `#check`、具体的な入力で動きを確認したいときは `#eval`、定義そのものを読みたいときは `#print` を使う。

表示や処理の設定を変更する [`set_option`](set_option.md)、定理の依存公理を表示する [`#print axioms`](opaque_axiom.md) も使える。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[文法要素の一覧に戻る](README.md)
