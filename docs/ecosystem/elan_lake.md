# elan と ake の役割と基本操作

elan は Lean をインストールしたり、使用する Lean のバージョンを切り替えるためのツールである。lake はプロジェクトに必要な追加ライブラリを取得し、Lean のコードをビルドするためのツールである。

| ツール | 何をするためのツールか | 主な設定ファイル | よく使うコマンド |
| --- | --- | --- | --- |
| `elan` | Lean をインストールし、プロジェクトに応じて使用するバージョンを切り替える | `lean-toolchain`、`~/.elan/settings.toml` | `elan show`、`elan default` |
| `lake` | プロジェクトを作成し、必要な追加ライブラリを取得して、Lean のコードをビルド・実行する | `lakefile.toml` または `lakefile.lean`、`lake-manifest.json` | `lake build`、`lake update` |

例えば「使用する Lean のバージョンの確認」には `elan show`、「Lean ファイルの編集後のビルド」には `lake build` を使う。

Lake は Lean のツールチェーンに付属する。`lake build` を実行すると、まず elan が使用する Lean のバージョンに対応する Lake を選び、起動された Lake がプロジェクトの設定を読んで必要な対象をビルドする。

## elan によるバージョン管理

通常、シェルから呼ぶ `lean`・`lake` は `~/.elan/bin/` にある代理コマンドである。代理コマンドが Lean のバージョンを選び、対応するツールチェーン内の実行ファイルを起動するため、プロジェクトを移動すると使用する Lean のバージョンも変わる。

### プロジェクトのバージョン指定

プロジェクトのルートにある `lean-toolchain` は、使用する Lean のバージョンを一行で指定するファイルである。例えば次の内容を保存する。

```text
leanprover/lean4:v4.35.0-rc3
```

プロジェクト内で `lean` や `lake` を実行すると、指定したバージョンを使用する。未インストールなら elan がダウンロードする。`lean-toolchain` を Git で共有すると、共同作業者も同じバージョンを選べる。

### バージョン選択の優先順位

elan は、次の順で使用する Lean のバージョンを決める。

1. `lean +leanprover/lean4:v4.35.0-rc3` など、コマンドで明示したバージョン。
2. 環境変数 `ELAN_TOOLCHAIN` の指定。
3. 現在のディレクトリから親へ探して最初に見つかった、ディレクトリ上書き設定または `lean-toolchain`。
4. elan に設定した既定のバージョン。

同じディレクトリに上書き設定と `lean-toolchain` がある場合は、上書き設定を優先する。親に上書き設定があっても、より近いディレクトリに `lean-toolchain` があれば近い方を使う。

### elan の基本操作

| コマンド | 用途 |
| --- | --- |
| `elan show` | 使用中の Lean のバージョンと選択の理由の確認 |
| `elan which lean` | 起動する Lean 実行ファイルの絶対パスの確認 |
| `elan toolchain list` | インストール済みのツールチェーンの一覧 |
| `elan default leanprover/lean4:v4.35.0-rc3` | プロジェクトなどで指定がない場合の既定のバージョンの設定 |
| `elan override set leanprover/lean4:v4.35.0-rc3` | 現在のディレクトリとその子で使う Lean のバージョンの上書き |
| `elan override list` | ディレクトリ上書き設定の一覧 |
| `elan override unset` | 現在のディレクトリの上書き設定の解除 |

`elan default` は既定のバージョンを変える操作であり、プロジェクトの `lean-toolchain` を書き換えない。ディレクトリ上書きもローカルの設定で、通常は `~/.elan/settings.toml` に保存される。

## Lake によるプロジェクト管理とビルド

### プロジェクトの設定

通常はプロジェクトのルートで `lake` を実行する。設定ファイルには次の二つの形式がある。

| ファイル | 内容 |
| --- | --- |
| `lakefile.toml` | パッケージ名、依存関係、ビルド対象などを TOML で記述 |
| `lakefile.lean` | 同様の設定を Lean で記述。独自のビルド処理なども定義可能 |

`lakefile.lean` があれば使用し、なければ `lakefile.toml` を使用する。両方を置いても設定を合成することはない。どちらもなければ、プロジェクト設定を必要とする操作はエラーになる。

`lake-manifest.json` は、解決済みの依存関係と具体的なリビジョンを記録するファイルである。例えば依存先をブランチで指定していても、マニフェストには取得したコミットが記録される。

### Lake の基本操作

| コマンド | 用途 |
| --- | --- |
| `lake new hello` | 新しい `hello/` ディレクトリにプロジェクトを作成 |
| `lake init hello` | 現在のディレクトリにプロジェクトを作成 |
| `lake build` | プロジェクトの既定の対象をビルド |
| `lake update` | 依存関係を解決・取得し、マニフェストを更新 |
| `lake exe hello` | 設定にある実行ファイルの対象 `hello` をビルドして実行 |
| `lake help build` | `build` の詳しい使い方の確認 |

`lake build` はビルド、`lake update` は依存関係の更新を目的とする。依存関係が更新済みなら、通常の編集後は `lake build` でよい。

`lake update` は依存先の指定に応じて使用するコミットを変え、依存先が要求する Lean のバージョンに合わせて `lean-toolchain` を更新する場合もある。

### プロジェクト環境でのコマンド実行

`lake env` は、プロジェクトと依存ライブラリを参照できる環境で、指定したコマンドを実行する操作である。例えば次のコマンドで、使用する Lean のインストール先を表示できる。

```sh
lake env lean --print-prefix
```

一方、`lake exe` は設定に登録された実行ファイルの対象を必要に応じてビルドしてから実行する。例えば mathlib のキャッシュ取得は次の操作になる。

```sh
lake exe cache get
```

`cache` は mathlib が提供する実行ファイルの対象であり、mathlib を依存関係に持つプロジェクトなどで利用できる。

インストール先、設定ファイル、依存ライブラリ、生成物、キャッシュの配置は、[インストール先と設定ファイル](files_and_directories.md)を参照。

参照：[公式リファレンス：elan](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/)、[Lake](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/)。

[Lean のツールと周辺知識に戻る](README.md)
