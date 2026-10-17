# 自分用 Lean 4 リファレンス

## Disclaimer

GPT-6.1 Sol (Medium〜Extra High) に生成させたものです。正しさは一切保証されません。
[記号索引](docs/symbols.md) および  [mathlib の記号索引](docs/mathlib/symbols.md) が便利です。

## 概要

- [記号索引](docs/symbols.md)：`⟨…⟩`、`?_`、`·`、`<;>` など、記号の形や呼び名から説明を探す。
- [文法要素の一覧](docs/syntax/README.md)：宣言、式、型、名前空間など、Lean のコードの読み方と書き方。
- [基本データ型の一覧](docs/basic-types/README.md)：数値・文字列・コレクション・商型などの作り方と基本操作。ハッシュマップや順序付き集合も扱う。
- [確認・実行・検査用の `#` コマンド](docs/commands/README.md)：型、計算結果、宣言内容、動作の確認。
- [属性の一覧](docs/attributes/README.md)：`@[simp]` など、宣言の登録や追加の扱い。
- [標準タクティクスの一覧](docs/tactics/README.md)：仮定やゴールを操作する証明の命令。
- [Leanでのプログラム検証の概要](docs/tactics/program_verification.md)：`mstart`・`mintro`・`mvcgen` などの用途、記法、関連タクティクスへの索引。
- [追加ライブラリのタクティクス](docs/library-tactics/README.md)：mathlib の算術・論理・式変形と、Aesop の証明探索。

### Lean の周辺ツール

- [elan と lake の役割と基本操作](docs/ecosystem/elan_lake.md)：Lean のバージョン選択、プロジェクト設定、ビルドと依存関係の更新。
- [インストール先と設定ファイル](docs/ecosystem/files_and_directories.md)：関係するファイルの保存場所、設定の参照順。


### コンパイル・実行時処理・バインディング

- [Lean のネイティブコンパイルと最適化](docs/compiler/native_compilation.md)：C を経由するコンパイル、代表的な最適化。
- [C 関数のバインディング](docs/compiler/c_bindings.md)：`@[extern]`、C 側の型と所有権、Lake によるビルドとリンク。
- [Lean コンパイラの最適化パスの拡張](docs/compiler/lcnf_optimization.md)：独自の最適化の追加、中間表現、パスの登録、変換の確認。
- [タスク・スレッドと共有状態の同期](docs/compiler/tasks_threads.md)：タスクの作成、参照カウントと不変な値の共有。

### mathlib

- [mathlib のリファレンス](docs/mathlib/README.md)：多変数・多次元の微分積分を中心に、級数、行列・基底、ノルム・内積、コンパクト性、関数列と極限の交換など。
- [mathlib の記号索引](docs/mathlib/symbols.md)：線形写像、ノルム、内積、近傍、勾配、積分、有限和など。

### ブラウン運動・確率解析

- [Brownian Motion のリファレンス](docs/brownian-motion/README.md)：ガウス過程、ブラウン運動の構成、停止時刻、マルチンゲール、二次変分、確率積分の定義と主な定理。

### Lean 4 の型と証明の基礎

- [Lean 4 の型システムの基礎](docs/foundations/type_system.md)：依存型、帰納型、宇宙階層、証明の無関連性、停止性、商型、公理の概観。
- [カリー・ハワード対応と Lean の命題・証明](docs/foundations/curry_howard.md)：命題と証明の型、証明の関数としての表現、タクティクスと型検査の関係。
- [Lean の型による数学的対象の構成と証明](docs/foundations/mathematical_constructions.md)：自然数から実数までの構成、条件の証明を持つ値、構成後の性質の利用。
- [証明項と基本的な証明の一覧](docs/foundations/proof_terms.md)：証明項の定義、標準の論理・等式の基本宣言、既存定理の利用と型の確認。
- [タクティクスの仕組みと利点](docs/foundations/tactics.md)：ゴールからの証明項の構成、メタ変数、メタプログラミング、型の書き換えと検査。
- [ゴールと証明状態](docs/foundations/proof_states.md)：ゴール、証明状態、`⊢`など。

## コード例の検証方法

mathlib・Aesop の例には、このリポジトリで宣言した追加ライブラリが必要である。通常の編集では、リポジトリのルートで変更した記事だけを検証する。

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
