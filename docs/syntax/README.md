# 文法要素の日本語リファレンス

Lean のコードに出てくる宣言、式、型、記法を、短い具体例で説明する。各ページは「何を書く構文か → どんな値・型・使える名前になるか → 実行できる例」を中心にしている。

記号の名前がわからない場合は、[記号索引](../symbols.md)から形や使用箇所で探せる。

文法のページはすべて `docs/syntax/` 直下に置き、分類はこの一覧の中で行う。仮定やゴールを操作する命令は、別ディレクトリの[タクティクス一覧](../tactics/README.md)にまとめる。型や計算結果などを確認する `#check`・`#eval` などは、[確認・実行・検査用コマンド](../commands/README.md)にまとめる。`@[simp]` などの属性を付ける構文と、その働きは、[属性の一覧](../attributes/README.md)にまとめる。

## 対象と例の実行方法

対象は **Lean 4.35.0-rc3 の基本的な文法と、標準で使える記法**である。mathlib などの追加ライブラリには依存しない。通常の定義や証明を読み書きするための項目に加えて、相互再帰や構文拡張の基本も扱う。構文木を操作する一般的なメタプログラムや、再帰の高度な停止性の証明などはまだ扱わない。

各 `lean` コードブロックは、それぞれ独立した完成例である。そのまま `.lean` ファイルにコピーして実行でき、追加のインポートが必要な例ではブロック内に `import` を記載している。直前のブロックの定義を引き継ぐ必要はない。

- `lean`：完成した証明・定義・確認コマンド。自動検証の対象。
- `text`：構文のひな形、型・状態・出力の説明用表示。実行対象ではない。
- `lean-incomplete`：未解決の穴を含む途中の例。完成例の検証から除外する。

## まず押さえる区別

**コマンド**は、ファイルに宣言を追加したり、設定や読み込みを行ったりする。`def`・`theorem`・`import` などが該当する。

**項**（**式**）は、型を持つ値を表す。`3`・`f x`・`fun x => x` などであり、命題もその証明も項として扱う。

**タクティクス**は、`by` の中でゴールを操作して項を作るための命令である。

```lean
def addOne (n : Nat) : Nat := n + 1

example : addOne 3 = 4 := by
  rfl
```

`def` は定義を登録するコマンド、`n + 1` はその本体の式、`by` はタクティクスによって項を作る文法である。`rfl` がタクティクスに当たる。

同じ名前でも、書く位置によって役割が違う。式の `let`・`have`・`match`・`if`・`show`・`calc` と、`by` 内の同名の操作は、それぞれのページで区別する。文法の例に証明のためのタクティクスが登場することはあるが、タクティクス自体の説明は別の一覧で行う。

## 最初に読むページ

1. [`def`](def.md)・[`theorem`・`example`](theorem.md)：宣言の `:` と `:=` を読む。
2. [関数の型](function_types.md)・[引数の括弧](binders.md)：入力と結果の型を読む。
3. [関数適用](application.md)・[`fun`](fun.md)：関数に値を渡す・関数を作る。
4. [`⟨…⟩`](anonymous_constructor.md)・[論理の記号](logical_symbols.md)：証明の形を読む。
5. [`let`](let.md)・[`if`](if.md)・[`match`](match.md)：途中の値と分岐を書く。
6. [`by`](by.md)：タクティクスによる証明とのつながりを理解する。

## 宣言・引数・型

| ページ | 何を表すか |
| --- | --- |
| [`def`・`abbrev`](def.md) | 値や関数の定義、展開しやすい別名 |
| [`private`・`protected`](visibility.md) | 宣言名の使える範囲、名前空間を開く際の扱い |
| [`noncomputable`](noncomputable.md) | 実行用のコード生成から除外する定義 |
| [`opaque`・`axiom`](opaque_axiom.md) | 本体を展開しない定義、値や命題を仮定する宣言 |
| [`theorem`・`example`](theorem.md) | 名前のある定理と、名前を残さない確認用の宣言 |
| [引数の括弧](binders.md) | 明示的・暗黙・インスタンス・厳密な暗黙の引数 |
| [引数の既定値](default_parameters.md) | `(x : α := e)`、タクティクスで補う自動引数 |
| [関数の型：`→`・`∀`](function_types.md) | 関数、含意、依存関数、全称命題 |
| [`Prop`・`Type`・`Sort`・`universe`](universes.md) | 命題とデータ型の違い、型の階層 |
| [論理の記号](logical_symbols.md) | `∧`・`∨`・`¬`・`↔`・`∃` と証明の形 |
| [部分型：`{x : α // P x}`](subtype.md) | 条件を満たす値と、その条件の証明 |

## 式の組み立て・証明の記法

| ページ | 何を表すか |
| --- | --- |
| [関数適用](application.md) | `f x`、名前付き引数、`@`、ドットでの適用 |
| [関数適用の省略・パイプ・関数合成](application_shortcuts.md) | `..`、`\|>`、`<\|`、`∘` |
| [`fun … => …`・`(· + 1)`](fun.md) | その場で作る関数と、その短い記法 |
| [パターンを使う `fun`](fun_patterns.md) | 引数の成分を取り出す関数、分岐を並べる関数 |
| [式の `let`](let.md) | 本体を展開できる局所定義 |
| [`let rec`](let_rec.md) | 式の途中に置く再帰的な補助関数 |
| [式の `have`](have.md) | 後続の式で使う補助的な証明や値 |
| [式の `haveI`・`letI`](local_instances.md) | 後続の式で使う局所インスタンス |
| [`by`](by.md) | タクティクスで作る項 |
| [式の `calc`](calc.md) | 等式・不等式などの段階的な証明 |
| [式の `if`](if.md) | 条件に応じて値を返す分岐 |
| [`if let`](if_let.md) | パターンへの一致に応じた分岐と成分の取り出し |
| [式の `match`](match.md) | 値のコンストラクターごとの分岐 |
| [`match h : e with …`](match_eq.md) | 分岐前の式とパターンをつなぐ等式の証明 |
| [非アクセス可能パターン](inaccessible_patterns.md) | 他のパターンや型から値が決まる部分を示す `.(式)` |
| [型の指定](type_ascription.md) | `(e : α)`、`show α from e`、`show α by …` |
| [`⟨…⟩`・`(x, y)`](anonymous_constructor.md) | コンストラクターによる構築、ペアと成分の取り出し |
| [仮定から証明を取り出す `‹…›`](assumption_terms.md) | 仮定の名前ではなく型を指定して証明を取り出す |
| [推論用の `_` と未完成の `?_`](placeholders.md) | 推論に任せる部分と、証明途中の穴 |
| [数値・文字列・リスト・配列](literals.md) | `3`、`"hello"`、`'a'`、`[…]`、`#[…]`、`::` |
| [真偽値の比較・演算](boolean_operators.md) | `==`、`!=`、`!`、`&&`、`\|\|` と命題の記号の違い |
| [添字アクセス](indexing.md) | `xs[i]`、`xs[i]'h`、`xs[i]?`、`xs[i]!` |
| [`do`・`←`・`return`](do.md) | 計算の結果を受け取り、次の計算につなぐ |
| [計算をつなぐ演算子](monad_operators.md) | `>>=`、`<$>`、`<*>`、`<*`、`*>`、`<\|>` |
| [`do` 内の更新と繰り返し](do_control.md) | `let mut`、`for`、`while`、`break`、`continue` |

## 型と関数の定義

| ページ | 何を表すか |
| --- | --- |
| [`structure`](structure.md) | 名前付きのフィールドを持つ型、構築と更新 |
| [`structure … extends …`](extends.md) | 親のフィールドを引き継ぐ構造体と親への射影 |
| [`inductive`](inductive.md) | コンストラクターを列挙して作る型 |
| [パターンによる関数定義・再帰](recursive.md) | `| … => …`、再帰呼び出し、`termination_by` |
| [補助定義の `where`](where.md) | 主要な定義の後に添える補助関数や値 |
| [`mutual … end`](mutual.md) | 互いを参照する関数や型の定義 |
| [`class`・`instance`](class.md) | 型クラスの要求と、探索で補う実装 |
| [`deriving`](deriving.md) | 型クラスのインスタンスの自動生成 |

## ファイル・名前・記法の整理

| ページ | 何を表すか |
| --- | --- |
| [`import`](import.md) | 別モジュールの読み込み |
| [`namespace`・`open`・`end`](namespace.md) | 名前の整理と、短い名前で使う範囲 |
| [特殊な名前の記法](identifiers.md) | 期待される型から名前を補う `.名前`、予約語などを囲む `«…»` |
| [`section`・`variable`・`include`](section.md) | 共通変数や設定の範囲、宣言に加える引数 |
| [`set_option`・設定の `in`](set_option.md) | 設定の変更と、その有効範囲 |
| [`notation`・`infix`・`scoped`](notation.md) | 既存の式に付ける記法と、その有効範囲 |
| [`syntax`・`macro`・`macro_rules`](syntax_macros.md) | 新しい構文の宣言と、既存の構文への展開 |
| [パーサーの組み合わせ](parser_combinators.md) | パーサーの `>>`、構文定義の `<\|>` |
| [コメント・字下げ](comments.md) | 行・ブロック・ドキュメントコメント、複数行の範囲 |

## 例の検証

リポジトリのルートで実行する。`lean-toolchain` が指定する Lean 4.35.0-rc3 を使い、文法とタクティクスの完成例をすべて確認する。

```sh
python3 scripts/check_examples.py
```

一つの文法ページだけを検証することもできる。

```sh
python3 scripts/check_examples.py docs/syntax/match.md
```

文法の例には共通インポートを補わず、記載されたコードを検証する。既存のタクティクスの例には、そちらの一覧に記載した共通インポート `Std.Tactic` を補う。`sorry` を含む例や Lean のエラーは失敗として扱う。

## 参照資料

各ページから公式リファレンスの該当項目へリンクしている。`latest` は固定バージョンより新しい内容を含み得るため、動作確認は `lean-toolchain` のバージョンを基準にする。

- [Lean 公式リファレンス：Definitions](https://lean-lang.org/doc/reference/latest/Definitions/)
- [Lean 公式リファレンス：Terms](https://lean-lang.org/doc/reference/latest/Terms/)
- [Lean 公式リファレンス：The Type System](https://lean-lang.org/doc/reference/latest/The-Type-System/)
- [Lean 公式 API ドキュメント](https://lean-lang.org/doc/api/)

[リポジトリの案内に戻る](../../README.md)
