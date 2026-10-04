# `#time`

`#time コマンド` は、**直後のコマンドを処理する時間を測り、ミリ秒単位で表示する**コマンドである。

```lean
#time example : (2 : Nat) + 3 = 5 := rfl
```

証明を確認する処理の後、例えば `time: …ms` のような情報が表示される。数値は環境や実行時の状態によって変わる。

定義や確認用のコマンドにも付けられる。

```lean
#time def double (n : Nat) : Nat := n + n

#time #check double
#time #eval double 3
```

それぞれ定義の処理、型の確認、実行結果の表示にかかる処理時間を測る。

ここで測るのは Lean がそのコマンドを処理する時間である。`#time #eval …` では計算だけでなく、型の確認や実行の準備なども含むので、関数単体の実行速度とは区別する。

`#time` を付けても宣言や証明の意味は変わらない。どのコマンドの処理に時間がかかっているかを、大まかに調べたい場合に使える。

参照：[公式 API：`#time`](https://lean-lang.org/doc/api/Init/Notation.html#Lean.timeCmd)。

[`#` コマンドの一覧に戻る](README.md)
