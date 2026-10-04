# Lean の日本語リファレンス

自分で読み返して理解できることを重視した、Lean 4 の日本語リファレンス。

目的に応じて、次の一覧から読む。

- [文法要素の一覧](docs/syntax/README.md)：宣言、式、型、名前空間など、Lean のコードの読み方と書き方。
- [確認・実行・検査用の `#` コマンド](docs/commands/README.md)：型、計算結果、宣言内容、期待した動作の確認。
- [属性の一覧](docs/attributes/README.md)：`@[simp]` など、宣言の登録や追加の扱い。
- [標準タクティクスの一覧](docs/tactics/README.md)：仮定やゴールを操作する証明の命令。
- [追加ライブラリのタクティクス](docs/library-tactics/README.md)：mathlib4 の算術・論理・式変形と、Aesop の証明探索。

文法要素は `docs/syntax/`、確認用の `#` コマンドは `docs/commands/`、属性は `docs/attributes/`、標準タクティクスは `docs/tactics/` に分ける。追加ライブラリのタクティクスは `docs/library-tactics/` に分離し、その中でも `mathlib/` と `aesop/` を分ける。各分類のページはそれぞれのディレクトリ直下に置く。

説明は短い具体例を中心にする。対象の Lean バージョンは `lean-toolchain`（4.35.0-rc3）を参照。追加ライブラリの依存バージョンと検証状況は[専用の一覧](docs/library-tactics/README.md#検証と参照方針)に記載する。

全カテゴリの例をまとめて検証するには、[追加ライブラリの準備](docs/library-tactics/README.md#例の実行と検証)を行ってから、リポジトリのルートで次を実行する。

```sh
python3 scripts/check_examples.py
```
