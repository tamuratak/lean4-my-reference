# インストール先と設定ファイル

Lean の開発環境では、Lean 本体をホームディレクトリ以下で共有し、追加ライブラリとビルド生成物を各プロジェクト内に置くのが一般的である。配置の管理には、Lean のバージョンを切り替える [elan](elan_lake.md) と、依存関係やビルドを管理する [Lake](elan_lake.md) を使う。Lean 本体、Lake、標準ライブラリなどをまとめた一式を「ツールチェーン」と呼ぶ。

以下では、macOS・Linux で elan を通常の方法で導入し、Lean `v4.35.0-rc3` をインストールした場合の配置を示す。`~` はホームディレクトリを表す。
`lean-toolchain` に書く名前は `leanprover/lean4:v4.35.0-rc3` で、保存先のディレクトリ名は `leanprover--lean4---v4.35.0-rc3` となる。別のバージョンも、それぞれのディレクトリに保存される。

## ホームディレクトリ以下の配置

| 場所 | 内容 |
| --- | --- |
| `~/.elan/bin/` | `elan` と、選択されたバージョンの `lean`・`lake` などを呼び出す代理コマンド |
| `~/.elan/toolchains/leanprover--lean4---v4.35.0-rc3/` | バージョンごとのツールチェーン本体 |
| `~/.elan/toolchains/leanprover--lean4---v4.35.0-rc3/bin/` | 実際の `lean`・`lake`・`leanc` などの実行ファイル |
| `~/.elan/toolchains/leanprover--lean4---v4.35.0-rc3/src/lean/` | 標準ライブラリや Lean・Lake の Lean ソース |
| `~/.elan/toolchains/leanprover--lean4---v4.35.0-rc3/lib/lean/` | 標準ライブラリなどのコンパイル済みファイルとライブラリ |
| `~/.elan/toolchains/leanprover--lean4---v4.35.0-rc3/include/` | 生成した C コードのコンパイルなどに使うヘッダーファイル |
| `~/.elan/settings.toml` | elan の既定のツールチェーン、ディレクトリごとの上書き設定など |
| `~/.lake/config.toml` | Lake のシステム設定。リモートキャッシュサービスの登録など |

elan の保存先は環境変数 `ELAN_HOME`、Lake のシステム設定ファイルは `LAKE_CONFIG` で変更できる。`~/.lake/config.toml` は必要なときに用意するファイルで、存在しなくても通常のプロジェクトをビルドできる。

参照：[公式リファレンス：elan](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/)、[Lake](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/)。

## プロジェクト内の配置

次のパスはプロジェクトのルートからの相対パスである。`.lake/` 以下は、依存関係の取得やビルドに応じて作られる。

| 場所 | 内容 |
| --- | --- |
| `lean-toolchain` | プロジェクトで使用する Lean のバージョン |
| `lakefile.toml` または `lakefile.lean` | パッケージ名、依存関係、ビルド対象などの設定 |
| `lake-manifest.json` | 解決済みの依存関係と具体的なリビジョンの記録 |
| `.lake/packages/` | 取得した追加ライブラリのソース。mathlib なら通常は `.lake/packages/mathlib/` |
| `.lake/build/lib/lean/` | プロジェクトの `.olean` など、Lean のインポートやエディタで使う生成物 |
| `.lake/build/bin/` | ビルドした実行ファイル |
| `.lake/build/ir/` | 生成した C コードなどの中間生成物 |

追加ライブラリにも独自のビルドディレクトリがある。例えば、mathlib の生成物は通常 `.lake/packages/mathlib/.lake/build/` 以下に置かれる。ローカルのディレクトリを依存先に指定した場合は、そのディレクトリを使用する。

標準ライブラリの `Init`・`Std` はツールチェーンに付属する。一方、mathlib などの追加ライブラリはプロジェクトの依存関係として取得する。`import Mathlib` を書くだけで mathlib がインストールされるわけではない。

参照：[公式リファレンス：Lake の概念と構成](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/#lake-vocab)。

## 設定の参照順

| 設定対象 | 参照先と、指定がない場合の扱い |
| --- | --- |
| Lean のバージョン | 現在のディレクトリから親へ `lean-toolchain`・elan の上書き設定を探す。指定がなければ elan の既定のバージョンを使用。[選択の優先順位](elan_lake.md#バージョン選択の優先順位) |
| Lake のプロジェクト | 通常はルートの `lakefile.lean`、なければ `lakefile.toml`。両方なければ設定が必要な操作はエラー。[プロジェクトの設定](elan_lake.md#プロジェクトの設定) |
| Lake のシステム設定 | `LAKE_CONFIG` の指定先、未指定なら `~/.lake/config.toml`。ファイルがなくても通常のビルドは可能 |

`lake-manifest.json` は解決済みの依存関係を記録するファイルで、`lakefile` の代替にはならない。ホーム側の `~/.lake/config.toml` もプロジェクトの `lakefile` とは用途が異なる。

## キャッシュの保存場所

キャッシュには、プロジェクトをまたいで再利用するためのダウンロード済みファイルやビルド生成物が保存される。

| 種類 | 標準的な保存場所・変更方法 |
| --- | --- |
| mathlib の `lake exe cache get` 用 | `~/.cache/mathlib/`。`MATHLIB_CACHE_DIR` があれば指定先、なければ `XDG_CACHE_HOME` がある場合はその下の `mathlib/` |
| Lake のローカル成果物キャッシュ | elan のツールチェーンを使う場合は通常 `~/.elan/toolchains/leanprover--lean4---v4.35.0-rc3/lake/cache/`。`LAKE_CACHE_DIR` で変更可能 |
| Lake のシステムキャッシュ | 通常は `~/.cache/lake/`。`XDG_CACHE_HOME` があればその下の `lake/`。空でない `LAKE_CACHE_DIR` があれば指定先を優先する。ツールチェーン用の保存先を使えない場合などにも使用 |

mathlib のキャッシュ取得では、ダウンロードした圧縮ファイルなどを共有キャッシュに置き、展開した生成物をプロジェクト内の各ライブラリのビルドディレクトリに配置する。

Lake のローカル成果物キャッシュは実験的な機能である。有効化の設定によっては生成物を共有キャッシュに保存するため、すべての生成物が必ず `.lake/build/` 以下にあるとは限らない。

参照：[公式リファレンス：Lake](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/)、[公式 API：Lake の環境設定](https://lean-lang.org/doc/api/Lake/Config/Env.html)。

## 使用中の環境の確認

プロジェクトのルートで、次のコマンドを実行できる。

| コマンド | 確認できる内容 |
| --- | --- |
| [`elan show`](elan_lake.md#elan-の基本操作) | 使用中のツールチェーンと、選択の理由 |
| [`elan which lean`](elan_lake.md#elan-の基本操作) | elan が起動する実際の Lean 実行ファイルの絶対パス |
| [`lake env lean --print-prefix`](elan_lake.md#プロジェクト環境でのコマンド実行) | プロジェクトの環境で使う Lean のインストール先 |
| [`elan override list`](elan_lake.md#elan-の基本操作) | ディレクトリごとの上書き設定 |

参照：[公式リファレンス：elan のコマンド](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/)、[Lake のコマンド](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/#lake-cli)。

[Lean のツールと周辺知識に戻る](README.md)
