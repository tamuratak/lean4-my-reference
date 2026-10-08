# 自分用 Lean 4 リファレンス

## Disclaimer

GPT-6.1 Sol (Medium〜Extra High) に生成させたものです。正しさは一切保証されません。
[記号索引](docs/symbols.md) および  [mathlib の記号索引](docs/mathlib/symbols.md) が便利です。

## 概要

自分で読み返して理解できることを重視した、Lean 4 の日本語リファレンス。

目的に応じて、次の一覧から読む。

- [数学の概念を型で組み立て、性質を証明する](docs/mathematical_constructions.md)：自然数から実数までの構成を通して、型・データ・命題・証明の関係を理解する。
- [mathlib の数学リファレンス](docs/mathlib/README.md)：多変数・多次元の微分積分を中心に、級数、行列・基底、ノルム・内積、コンパクト性、関数列と極限の交換も調べる。
- [記号索引](docs/symbols.md)：`⟨…⟩`、`?_`、`·`、`<;>` など、記号の形や呼び名から説明を探す。
- [mathlib の記号索引](docs/mathlib/symbols.md)：線形写像、ノルム、内積、近傍、勾配、積分、有限和など、数学の記法から意味を探す。
- [文法要素の一覧](docs/syntax/README.md)：宣言、式、型、名前空間など、Lean のコードの読み方と書き方。
- [基本データ型の一覧](docs/basic-types/README.md)：数値・文字列・コレクション・商型などの作り方と基本操作。ハッシュマップや順序付き集合も扱う。
- [確認・実行・検査用の `#` コマンド](docs/commands/README.md)：型、計算結果、宣言内容、期待した動作の確認。
- [属性の一覧](docs/attributes/README.md)：`@[simp]` など、宣言の登録や追加の扱い。
- [標準タクティクスの一覧](docs/tactics/README.md)：仮定やゴールを操作する証明の命令。
- [プログラム検証の案内](docs/tactics/program_verification.md)：`mstart`・`mintro`・`mvcgen` などの用途、記法、関連タクティクスへの索引。
- [追加ライブラリのタクティクス](docs/library-tactics/README.md)：mathlib4 の算術・論理・式変形と、Aesop の証明探索。

## コード例の検証方法

例の検証には、[追加ライブラリの準備](docs/library-tactics/README.md#例の実行と検証)を行う。通常の編集では、リポジトリのルートで変更した記事だけを検証する。

```sh
python3 scripts/check_examples.py --changed
```

`--changed` は、直近のコミット `HEAD` から変更された `docs/` 内の Markdown ファイルを選ぶ。ステージ済み・未ステージの変更と Git 未登録の新規ファイルを含み、削除済みファイルは除く。コミット済みの記事や `docs/` 外の参考 MD は自動選択しない。これは前回の検証結果を保存する仕組みではなく、未コミットの変更が残っていれば再度選択される。

実行時には、選択件数とリポジトリのルートからの相対パスの一覧を表示する。パス内の改行などはエスケープして表示する。

特定の記事だけを検証する場合は、パスを指定できる。

```sh
python3 scripts/check_examples.py docs/mathlib/filters.md
```

全カテゴリを検証する場合は、引数なしで実行する。記事を編集するたびに全件を検証する必要はないが、Lean のバージョンや依存設定、検証スクリプトなど共通の条件を変更した場合は全件を確認する。

```sh
python3 scripts/check_examples.py
```

検証スクリプトのテストは、リポジトリのルートで次のように実行する。Lean や追加ライブラリの準備は不要で、Python の標準ライブラリと Git を使用する。

```sh
python3 scripts/test_check_examples.py
```
