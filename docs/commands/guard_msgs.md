# `#guard_msgs`

`#guard_msgs in コマンド` は、**コマンドが出すメッセージを、直前のドキュメントコメントに書いた内容と比較する**検査用のコマンドである。

```lean
/-- info: 5 -/
#guard_msgs in
#eval 2 + 3
```

期待する出力は `info: 5` である。実際の出力が一致すれば検査に通り、一致しなければエラーになる。コメントの `info:` はメッセージの種類を表す。

エラーが出ることも、意図した振る舞いとして検査できる。

```lean
/-- error: Unknown identifier `missingName` -/
#guard_msgs in
#check missingName
```

内側の `#check` は失敗するが、その失敗メッセージが期待どおりなので、コード全体は検査に通る。型が通る例として `missingName` を紹介しているわけではない。

期待するメッセージを書かなければ、通常は出力がないことを検査する。

```lean
#guard_msgs in
example : (3 : Nat) = 3 := rfl
```

検査する種類は、括弧内の設定で指定できる。`info`・`warning`・`error` を選び、`drop` はその種類を比較から除く指定である。空白の扱いには `whitespace := exact`・`normalized`・`lax`、順序には `ordering := exact`・`sorted` がある。

エラーが起きることだけを見る場合は [`#check_failure`](check_failure.md)、出力の文面まで確かめる場合は `#guard_msgs` が向いている。出力の表現はバージョンや表示設定で変わるので、このリファレンスの例は固定した Lean バージョンで確認する。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
