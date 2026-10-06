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

検査する種類や比較方法は、`#guard_msgs (...) in` の括弧内にカンマで区切って指定する。`info`・`warning`・`error` はその種類を比較する指定、`drop warning` などはその種類のメッセージを捨てて比較から除く指定である。種類の指定がなければ、すべてのメッセージを比較する。

空白の比較では、どの設定でも文面の先頭と末尾の空白類を除く。その後の扱いが次のように違う。

| 設定 | 比較方法 |
| --- | --- |
| `whitespace := exact` | 内部の空白・改行もそのまま比較する |
| `whitespace := normalized` | 改行を空白に変えて比較する。連続する空白はまとめない。既定値 |
| `whitespace := lax` | 空白・改行・タブなどの連続を一つの空白にまとめて比較する |
| `ordering := exact` | メッセージの出た順番で比較する。既定値 |
| `ordering := sorted` | メッセージを文字列の辞書順に並べて比較する |

```lean
/-- info: alpha
beta -/
#guard_msgs (info, whitespace := normalized) in
#eval IO.println "alpha beta"

/-- info: alpha beta -/
#guard_msgs (info, whitespace := lax, ordering := exact) in
#eval IO.println "alpha  \n\tbeta"
```

一つ目は期待する文面の改行を空白に変えて比較する。二つ目は実際の出力にある連続した空白・改行・タブを一つの空白にまとめる。二つ目を `normalized` にすると、連続した空白やタブは残るので一致しない。

```lean
/-- error: ❌️ Docstring on `#guard_msgs` does not match generated message: -/
#guard_msgs (error, substring := true) in
/-- info: alpha beta -/
#guard_msgs (info, whitespace := normalized) in
#eval IO.println "alpha  \n\tbeta"
```

内側の `#guard_msgs` は、上の二つ目と同じ出力を `normalized` で比較し、不一致のエラーを出す。外側は `substring := true` により、そのエラーメッセージにコメントの文面が含まれることを検査する。意図した不一致を外側で確認するので、例全体は検査に通る。

エラーが起きることだけを見る場合は [`#check_failure`](check_failure.md)、出力の文面まで確かめる場合は `#guard_msgs` が向いている。出力の表現はバージョンや表示設定で変わるので、このリファレンスの例は固定した Lean バージョンで確認する。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
