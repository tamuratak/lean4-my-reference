# 確認・実行・検査用の `#` コマンド

`#check`・`#eval` など、Lean のファイルに書いて、型・計算結果・宣言・検査結果を確認するコマンドをまとめる。各ページはこのディレクトリの直下に置く。

## 文法・タクティクスとの関係

厳密には、これらも Lean の**コマンド構文**である。`def`・`theorem`・`import` も同じトップレベルのコマンドという構文分類に属する。

このリファレンスでは、学習時の用途から探しやすくするため、`#` で始まる確認・実行・検査用のコマンドを独立したカテゴリとして扱う。[文法要素](../syntax/README.md)と[タクティクス](../tactics/README.md)の説明とは別に置く。

`#` は対話的な確認用のコマンド名に付ける慣例であり、シェルの命令ではない。通常は `by` の外に書き、エディタのメッセージ表示や `lean` の出力で結果を確認する。配列の `#[…]` は値の記法なので、ここで扱うコマンドとは別である。

## 最初に使うもの

| やりたいこと | コマンド |
| --- | --- |
| 式や定理の型を知りたい | [`#check`](check.md) |
| 具体的な計算結果を見たい | [`#eval`](eval.md) |
| 定義の本体や証明項を読みたい | [`#print`](print.md) |
| 定義の計算でどこまで展開されるか知りたい | [`#reduce`](reduce.md) |
| 型クラスの実装が見つかるか知りたい | [`#synth`](synth.md) |

```lean
def double (n : Nat) : Nat := n + n

#check double 3
#eval double 3
#print double
```

最初は型 `Nat`、次は値 `6`、最後は `double` の宣言の内容が表示される。

## 宣言や環境を調べる

| ページ | 何を確認するか |
| --- | --- |
| [`#print axioms`](print_axioms.md) | 宣言が依存する公理 |
| [`#print equations`・`#print eqns`](print_equations.md) | 関数の定義から生成される等式の定理 |
| [`#where`・`#version`](where_version.md) | 名前空間・変数・設定などの範囲、Lean のバージョン |
| [`#import_path`](import_path.md) | 宣言を読み込むインポートの経路 |

`#print sig` は [`#print`](print.md)、`#eval!` は [`#eval`](eval.md) のページにまとめている。

## 動作を検査する

| ページ | 何を検査するか |
| --- | --- |
| [`#guard`](guard.md) | 条件を計算した結果が真か |
| [`#guard_expr`](guard_expr.md) | 二つの式が指定した意味で一致するか |
| [`#guard_msgs`](guard_msgs.md) | 出力・警告・エラーのメッセージが期待どおりか |
| [`#check_failure`](check_failure.md) | 式の型の確認が失敗するか |
| [`#check_tactic`・`#check_simp`](check_tactic.md) | タクティクスの変形結果、または失敗が期待どおりか |

`#check_tactic_failure` と `#check_simp … !~>` は、タクティクス検査のページにまとめている。

## 処理時間と打ち切り

| ページ | 何をするか |
| --- | --- |
| [`#time`](time.md) | 一つのコマンドの処理時間を測る |
| [`#exit`](exit.md) | その位置でファイルの後続の処理を打ち切る |

## 対象と例の検証

対象は **Lean 4.34.1 の主な確認・実行・検査用コマンド**である。内部実装を調べる専用コマンド、依存関係の制約を検査する全コマンド、追加ライブラリ独自のコマンドまでは網羅しない。

`lean` のコードブロックはそれぞれ独立して実行できる。必要な追加インポートはブロック内に明記し、共通インポートは補わない。表示だけの断片は `text` として区別する。

`#check_failure` や `#guard_msgs` では、内側の失敗が期待どおりであることを確認する完成例もある。型の合わない式を、型が通る例として扱っているわけではない。

リポジトリのルートで、全カテゴリの完成例をまとめて検証する。

```sh
python3 scripts/check_examples.py
```

一つのページだけを指定することもできる。

```sh
python3 scripts/check_examples.py docs/commands/check.md
```

`#eval` や `#guard` による実行結果の確認と、命題の証明の作成は区別する。コマンドが通ったことから、任意の定理の証明が登録されるわけではない。また、`#exit` より後は検証されないので、実行例ではその後に完成した証明を置かない。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)、[公式 API：Command](https://lean-lang.org/doc/api/Lean/Parser/Command.html)。

[リポジトリの案内に戻る](../../README.md)
