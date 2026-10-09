# 文法要素の日本語リファレンス

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
| [依存ペア型：`Σ`](sigma.md) | １番目の値に応じて２番目の型が決まるペア |

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

## 参照資料

各ページから公式リファレンスの該当項目へリンクしている。`latest` は固定バージョンより新しい内容を含み得るため、動作確認は `lean-toolchain` のバージョンを基準にする。

- [Lean 公式リファレンス：Definitions](https://lean-lang.org/doc/reference/latest/Definitions/)
- [Lean 公式リファレンス：Terms](https://lean-lang.org/doc/reference/latest/Terms/)
- [Lean 公式リファレンス：The Type System](https://lean-lang.org/doc/reference/latest/The-Type-System/)
- [Lean 公式 API ドキュメント](https://lean-lang.org/doc/api/)

[リポジトリの案内に戻る](../../README.md)
