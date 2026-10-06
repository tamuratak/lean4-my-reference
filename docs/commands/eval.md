# `#eval`・`#eval!`

`#eval` は、式をプログラムとして実行し、その結果を表示するコマンドである。

```lean
#eval 2 + 3
#eval [1, 2, 3].length
```

出力は順に `5` と `3` である。型だけを見る [`#check`](check.md) とは違い、具体的な計算を行う。

定義した関数にも使える。

```lean
def double (n : Nat) : Nat := n + n

#eval double 3
```

出力は `6` になる。結果を表示するため、型に応じた表示の仕組みが必要になる。独自の型の表示には、例えば [`deriving Repr`](../syntax/deriving.md) を使える。

`IO` の処理も実行できる。

```lean
#eval IO.println "hello Lean"
```

これは `hello Lean` を出力する。`#eval` はファイルを確認するときに処理を実行するので、`IO` の例では書かれた作用も実際に起きる。

結果の型も表示したいときは設定を付けられる。

```lean
set_option eval.type true in
#eval 2 + 3
```

この場合は `5 : Nat` と表示される。

`#eval!` は、通常の `#eval` が行う「仮の証明 `sorry` に依存していないか」の検査を外す変種である。完成したコードの計算には通常の `#eval` を使えばよい。

計算結果が表示されたこと自体は、等式を定理として登録したことにはならない。式を定義上の計算で展開して調べる場合は [`#reduce`](reduce.md) を使う。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
