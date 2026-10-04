# 記号索引

**コードに出てきた記号から、その意味と詳しい説明を探すための索引**。ページ内検索で記号そのもの、または「暗黙引数」「穴」「中点」などの呼び名を検索できる。

対象は、このリファレンスで説明している主な記号と記法である。表の使用例は書く位置を示す断片であり、単独で実行するコードではない。実行できる完成例はリンク先に載せている。

同じ記号でも、**式・引数・パターン・タクティクス・状態表示のどこに現れるか**によって意味が変わる。特に `·`、`←`、`_`、括弧は、使用例の形も見て選ぶ。

## 型・定義・関数

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `:` | コロン。宣言する名前の型を指定する | `def n : Nat := 3` | [定義](syntax/def.md) |
| `(… : …)` | 型指定。式をどの型として読むか指定する | `(3 : Int)` | [型の指定](syntax/type_ascription.md) |
| `:=` | 定義や局所定義の本体を指定する | `let n := 3` | [定義](syntax/def.md)・[let](syntax/let.md) |
| `(名前 := 値)` | 名前付き引数。引数名を指定して値を渡す | `keep (α := Nat) 3` | [関数適用](syntax/application.md) |
| `→` | 関数型、または命題の含意 | `Nat → Nat`、`P → Q` | [関数の型](syntax/function_types.md) |
| `∀` | 全称量化。入力ごとの証明を表す依存関数型 | `∀ n : Nat, n = n` | [関数の型](syntax/function_types.md) |
| `=>`・`↦` | 関数の入力やパターンと、その本体を区切る | `fun x => x + 1` | [匿名関数](syntax/fun.md)・[match](syntax/match.md) |
| `@` | 暗黙の引数も位置順に渡す関数適用 | `@keep Nat 3` | [関数適用](syntax/application.md) |
| `.` | 名前空間の区切り、フィールドの取り出し、ドットによる関数適用 | `Nat.add_comm`、`p.x`、`xs.length` | [名前空間](syntax/namespace.md)・[構造体](syntax/structure.md)・[関数適用](syntax/application.md) |
| `.1`・`.2` | 組などの成分を取り出す射影 | `pair.1`、`h.2` | [組とコンストラクター](syntax/anonymous_constructor.md) |
| 先頭の `.名前` | 期待される型の名前空間から名前を探す | `(.some 3 : Option Nat)` | [特殊な名前の記法](syntax/identifiers.md) |
| `«…»` | ギュメ。予約語や特殊な文字を含む名前を囲む | `Demo.«a+b»` | [特殊な名前の記法](syntax/identifiers.md) |
| 関数適用の `..` | 二つのピリオド。残りの引数を推論に任せる | `Nat.add_comm ..` | [関数適用の省略](syntax/application_shortcuts.md) |
| `\|>`・`<\|` | パイプ記法。入力を左に置く・右の式全体を引数にする | `3 \|> f`、`f <\| g 3` | [関数適用のパイプ](syntax/application_shortcuts.md) |
| `∘` | 関数合成。右の関数の後に左の関数を適用する | `f ∘ g` | [関数合成](syntax/application_shortcuts.md) |

## 括弧・組・コレクション

括弧は、形だけでなく**宣言の引数なのか、値を作る式なのか**を区別する。

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `(x : α)` | 丸括弧で囲む明示的な引数 | `def f (n : Nat) := n` | [引数の括弧](syntax/binders.md) |
| `{x : α}` | 波括弧で囲む暗黙の引数 | `def keep {α : Type} (x : α) := x` | [引数の括弧](syntax/binders.md) |
| `[C α]` | 角括弧で囲むインスタンス引数 | `[ToString α]` | [引数の括弧](syntax/binders.md)・[型クラス](syntax/class.md) |
| `⦃x : α⦄` | 厳密な暗黙の引数 | `⦃α : Type⦄` | [引数の括弧](syntax/binders.md) |
| `(…)` | 式をまとめ、結び付く順序を指定する | `double (2 + 3)` | [関数適用](syntax/application.md) |
| `(x, y)` | ペアを作る | `(3, "three")` | [組とコンストラクター](syntax/anonymous_constructor.md) |
| `×` | ペアの型、直積型 | `Nat × String` | [組とコンストラクター](syntax/anonymous_constructor.md) |
| `Σ` | シグマ。依存ペア型、依存和型 | `Σ n : Nat, Fin n` | [依存ペア型](syntax/sigma.md) |
| `(x : α) × β x` | １番目の値に名前を付ける依存ペア型 | `(n : Nat) × Fin n` | [依存ペア型](syntax/sigma.md) |
| `⟨…⟩` | 山括弧。期待される型のコンストラクターへ成分を渡す | `exact ⟨hp, hq⟩` | [組とコンストラクター](syntax/anonymous_constructor.md) |
| パターンの `⟨…⟩` | 組や証明の中身を分解する | `rcases h with ⟨x, hx⟩` | [rcases](tactics/rcases.md) |
| `{x : α // P x}` | 部分型。条件を満たす値と、その証明を持つ型 | `{n : Nat // n > 0}` | [部分型](syntax/subtype.md) |
| `{…}`・`{… with …}` | フィールド名を指定して構造体を作る・更新する | `{ p with x := 3 }` | [構造体](syntax/structure.md) |
| `[…]`・`[]` | リストを作る・空リストを表す | `[1, 2, 3]` | [リテラル](syntax/literals.md) |
| `::` | リストの先頭に要素を追加するコンストラクター | `1 :: [2, 3]` | [リテラル](syntax/literals.md) |
| `#[…]` | 配列を作る | `#[1, 2, 3]` | [リテラル](syntax/literals.md) |
| `a[i]` | 添字アクセス。範囲内であることの証明を自動で補う | `xs[i]` | [添字アクセス](syntax/indexing.md) |
| `a[i]'h` | アポストロフィの後に、範囲内であることの証明を渡す | `xs[i]'h` | [添字アクセス](syntax/indexing.md) |
| `a[i]?` | 有効な添字なら `some`、そうでなければ `none` を返す | `xs[i]?` | [添字アクセス](syntax/indexing.md) |
| `a[i]!` | 要素を直接取り出す。有効でなければ実行時にパニック | `xs[i]!` | [添字アクセス](syntax/indexing.md) |
| タクティクスの `[…]` | 利用する等式や補題などを列挙する | `rw [h₁, h₂]`、`simp [h]` | [rw](tactics/rw.md)・[simp](tactics/simp.md) |

## 論理・等式

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `∧` | 論理積。「かつ」 | `P ∧ Q` | [論理の記号](syntax/logical_symbols.md) |
| `∨` | 論理和。「または」 | `P ∨ Q` | [論理の記号](syntax/logical_symbols.md) |
| `¬` | 否定。`P → False` の略 | `¬ P` | [論理の記号](syntax/logical_symbols.md) |
| `↔` | 同値。両方向の含意 | `P ↔ Q` | [論理の記号](syntax/logical_symbols.md) |
| `∃` | 存在量化。証人とその条件の証明が必要 | `∃ n : Nat, n = 3` | [論理の記号](syntax/logical_symbols.md) |
| `=` | 等式。両辺が等しいという命題 | `a = b` | [rfl](tactics/rfl.md)・[rw](tactics/rw.md) |
| `≠` | 等しくないという命題。等式の否定 | `a ≠ b` | [論理の記号](syntax/logical_symbols.md)（否定） |
| `‹…›`・`‹_›` | 型を指定して、仮定から証明を取り出す | `‹P›` | [仮定から証明を取り出す](syntax/assumption_terms.md) |

`P → Q` と `∀ x, P x` は、上の[型・定義・関数](#型定義関数)にも載せている。`=` と `:=` は役割が違い、前者は等式の命題、後者は定義の本体を指定する区切りである。

`‹P›` は既存の証明を取り出し、`⟨hp, hq⟩` は成分から証明を組み立てる。括弧の形が似ているので区別する。

## 真偽値の比較・演算

ここでの結果の型は `Bool` であり、上の命題の記号とは異なる。

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `==`・`!=` | 真偽値を返す比較と、その反転 | `n == 3`、`n != 3` | [真偽値の演算](syntax/boolean_operators.md) |
| 前置の `!` | 真偽値の否定 | `!true` | [真偽値の演算](syntax/boolean_operators.md) |
| `&&`・`\|\|` | 真偽値の「かつ」「または」 | `a && b`、`a \|\| b` | [真偽値の演算](syntax/boolean_operators.md) |

前置の `!b`、添字アクセスの `a[i]!`、タクティクス名の `simp!` は別の使い方である。末尾の `!`・`?` の意味は、その構文や宣言ごとに確認する。

## 穴・省略・分岐・証明状態

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| 式の `_` | アンダースコア。型や値の推論に任せる部分 | `@keep _ (3 : Nat)` | [推論用の穴](syntax/placeholders.md) |
| パターンの `_` | ワイルドカード。成分に名前を付けず受け取る | `match x with \| _ => 0` | [match](syntax/match.md)・[rcases](tactics/rcases.md) |
| `?_` | 後で証明する明示的な穴 | `refine ⟨3, ?_⟩` | [証明の穴](syntax/placeholders.md)・[refine](tactics/refine.md) |
| 式の `·` | 中点。短い匿名関数の引数になる | `(· + 1)` | [匿名関数](syntax/fun.md) |
| タクティクス先頭の `·` | 中点。一つのゴールを選び、そのブロックで証明する | `· exact hp` | [複数ゴールの構文](tactics/semicolon.md) |
| `\|` | 縦棒。パターンや場合分けの枝を区切る | `rcases h with hp \| hq` | [rcases](tactics/rcases.md)・[match](syntax/match.md)・[帰納法](tactics/induction.md) |
| `.(式)` | 非アクセス可能パターン。他のパターンや型から決まる部分を指定する | `.(n)` | [非アクセス可能パターン](syntax/inaccessible_patterns.md) |
| `⊢` | ターンスタイル。現在証明すべきゴールを示す表示 | `⊢ P` | [by と証明状態](syntax/by.md) |
| `at` の後の `⊢`・`\|-` | タクティクスの操作対象として、現在のゴールを指定する | `rw [hab] at h ⊢` | [rw の対象指定](tactics/rw.md) |

論理学の `Γ ⊢ P` は「仮定 `Γ` から `P` を導出できる」ことを表すが、Lean の証明状態の `⊢ P` は「これから `P` を証明する必要がある」という課題を表す。表示だけでは、証明できることが確認されたわけではない。詳しくは [`by` のページの「`⊢` と証明状態の読み方」](syntax/by.md)を参照。

状態表示の `⊢` は仮定とゴールの区切りである。コード中では、`at h ⊢` のように操作対象を指定する用途もあるが、`⊢` 単独はタクティクスの命令ではない。`?_` を含む証明は、その穴を埋めるまで未完成である。

## 書き換え・計算・タクティクスの制御

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `rw` などの `←` | 左矢印。等式を逆向きに使う | `rw [← h]` | [rw](tactics/rw.md) |
| `do` の `←` | 計算を実行し、その結果を受け取る | `let x ← action` | [do 記法](syntax/do.md) |
| `↑` | コーシオン。型変換を表す表示・記法 | `(↑n : Int)` | [norm_cast](tactics/norm_cast.md) |
| `;` | セミコロン。次のタクティクスへ進む | `constructor; exact hp` | [複数ゴールの構文](tactics/semicolon.md) |
| `<;>` | 左の操作で作られたすべてのゴールに右の操作を行う | `constructor <;> assumption` | [複数ゴールの構文](tactics/semicolon.md) |
| `*` | 対象をまとめて指定する。具体的な対象はタクティクスによる | `simp at *`、`simp [*]` | [simp](tactics/simp.md) |
| `∎` | 証明終了記号。Lean では証明提案を利用するタクティクスの書き方 | `∎` | [try? と証明提案](tactics/try_search.md) |

## 計算・構文拡張を組み合わせる記法

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `>>=` | バインド。計算の結果を次の計算を返す関数に渡す | `action >>= f` | [計算をつなぐ演算子](syntax/monad_operators.md) |
| `<$>` | マップ。計算の結果に通常の関数を適用する | `f <$> some 3` | [計算をつなぐ演算子](syntax/monad_operators.md) |
| `<*>` | 計算に入った関数を、別の計算に入った値に適用する | `functions <*> values` | [計算をつなぐ演算子](syntax/monad_operators.md) |
| `<*`・`*>` | 計算を順に行い、左・右の結果を残す | `a <* b`、`a *> b` | [計算をつなぐ演算子](syntax/monad_operators.md) |
| 式の `<\|>` | 計算の候補を選ぶ。`Option` では先が `none` なら次を使う | `a <\|> b` | [計算をつなぐ演算子](syntax/monad_operators.md) |
| `>>` | 型に登録された実装で処理を順につなぐ。パーサーなどで使う | `parser₁ >> parser₂` | [パーサーの組み合わせ](syntax/parser_combinators.md) |
| 構文定義の `<\|>` | 入力を読む候補を指定する | `("yes" <\|> "no")` | [パーサーの組み合わせ](syntax/parser_combinators.md) |
| バッククォートと括弧 | 構文引用。式などの書き方を構文として扱う | `` `(x + 1) `` | [構文とマクロ](syntax/syntax_macros.md) |
| `$x`・`$x:term` | アンチクォート。引用へ構文を埋め込む・パターンから取り出す | `` `($x + 1) `` | [構文とマクロ](syntax/syntax_macros.md) |

`<|>`、`<|`、`|>`、`<;>` は互いに異なる記法である。`>>` も、どのモナドにでも使える記法ではない。

## プログラム検証で使う記号

これらは標準ライブラリ `Std.Do` の状態を扱う論理の記法である。通常の引数の括弧や命題の表示とは用途を分ける。

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `⊢ₛ` | 状態についての命題の含意 | `P ⊢ₛ Q` | [mstart](tactics/mstart.md) |
| `⌜…⌝` | 通常の命題を状態についての命題に埋め込む | `⌜True⌝` | [mvcgen](tactics/mvcgen.md) |
| `⦃P⦄ … ⦃Q⦄` | ホーア三つ組。プログラムの前提と事後条件を指定する | `⦃P⦄ program ⦃Q⦄` | [mvcgen](tactics/mvcgen.md) |
| `⇓` | 事後条件で返り値に名前を付ける | `⇓ n => ⌜n = 3⌝` | [mvcgen](tactics/mvcgen.md) |

`⦃α : Type⦄` は厳密な暗黙引数、`⦃P⦄ program ⦃Q⦄` はプログラムの仕様であり、括弧が同じでも意味が違う。

## コマンド・属性・コメント

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `#…` | 型・値・宣言などを確認するコマンド | `#check Nat.add_comm` | [確認用コマンド一覧](commands/README.md) |
| `@[…]` | 属性。宣言へ登録や設定を付ける | `@[simp]` | [属性の基本](attributes/basics.md) |
| `--` | 行コメント | `-- A comment` | [コメント](syntax/comments.md) |
| `/- … -/` | ブロックコメント | `/- A comment -/` | [コメント](syntax/comments.md) |
| `/-- … -/` | 宣言に付けるドキュメントコメント | `/-- A description. -/` | [コメント](syntax/comments.md) |

`@f` は関数適用、`@[simp]` は属性であり、同じ `@` を含んでも用途が違う。`#[…]` は配列なので、確認用の `#` コマンドとも区別する。

## ここにない記号を見つけたとき

Lean ではライブラリやユーザーが記法を追加できるため、この索引がすべての記号を網羅するわけではない。[notation・infix・scoped](syntax/notation.md)で、記法の定義と有効範囲を確認できる。記号の意味は、インポートしたモジュールや、その式の型によっても変わる。

数学ライブラリ固有の記法を調べる際は、Lean 本体の構文と区別する。追加タクティクスについては[mathlib・Aesop の一覧](library-tactics/README.md)を参照。

参照：[公式リファレンス：Terms](https://lean-lang.org/doc/reference/latest/Terms/)、[公式リファレンス：タクティクスの構文](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式リファレンス：Notations and Macros](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/)。

[リファレンスの入口に戻る](../README.md)
