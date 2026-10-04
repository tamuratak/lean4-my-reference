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
| `⟨…⟩` | 山括弧。期待される型のコンストラクターへ成分を渡す | `exact ⟨hp, hq⟩` | [組とコンストラクター](syntax/anonymous_constructor.md) |
| パターンの `⟨…⟩` | 組や証明の中身を分解する | `rcases h with ⟨x, hx⟩` | [rcases](tactics/rcases.md) |
| `{x : α // P x}` | 部分型。条件を満たす値と、その証明を持つ型 | `{n : Nat // n > 0}` | [部分型](syntax/subtype.md) |
| `{…}`・`{… with …}` | フィールド名を指定して構造体を作る・更新する | `{ p with x := 3 }` | [構造体](syntax/structure.md) |
| `[…]`・`[]` | リストを作る・空リストを表す | `[1, 2, 3]` | [リテラル](syntax/literals.md) |
| `::` | リストの先頭に要素を追加するコンストラクター | `1 :: [2, 3]` | [リテラル](syntax/literals.md) |
| `#[…]` | 配列を作る | `#[1, 2, 3]` | [リテラル](syntax/literals.md) |
| `a[i]` | 添字アクセス。範囲内であることの証明が必要な場合がある | `xs[i]` | [get_elem_tactic](tactics/get_elem_tactic.md) |
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
| `≠` | 不等号。等式の否定 | `a ≠ b` | [論理の記号](syntax/logical_symbols.md)（否定） |

`P → Q` と `∀ x, P x` は、上の[型・定義・関数](#型定義関数)にも載せている。`=` と `:=` は役割が違い、前者は等式の命題、後者は定義の本体を指定する区切りである。

## 穴・省略・分岐・証明状態

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| 式の `_` | アンダースコア。型や値の推論に任せる部分 | `@keep _ (3 : Nat)` | [推論用の穴](syntax/placeholders.md) |
| パターンの `_` | ワイルドカード。成分に名前を付けず受け取る | `match x with \| _ => 0` | [match](syntax/match.md)・[rcases](tactics/rcases.md) |
| `?_` | 後で証明する明示的な穴 | `refine ⟨3, ?_⟩` | [証明の穴](syntax/placeholders.md)・[refine](tactics/refine.md) |
| 式の `·` | 中点。短い匿名関数の引数になる | `(· + 1)` | [匿名関数](syntax/fun.md) |
| タクティクス先頭の `·` | 中点。一つのゴールを選び、そのブロックで証明する | `· exact hp` | [複数ゴールの構文](tactics/semicolon.md) |
| `\|` | 縦棒。パターンや場合分けの枝を区切る | `rcases h with hp \| hq` | [rcases](tactics/rcases.md)・[match](syntax/match.md)・[帰納法](tactics/induction.md) |
| `⊢` | ターンスタイル。現在証明すべきゴールを示す表示 | `⊢ P` | [by と証明状態](syntax/by.md) |

`⊢` は通常、証明状態の表示を読むための記号であり、タクティクスの命令ではない。`?_` を含む証明は、その穴を埋めるまで未完成である。

## 書き換え・計算・タクティクスの制御

| 記号・形 | 呼び名・役割 | 使用例 | 詳細 |
| --- | --- | --- | --- |
| `rw` などの `←` | 左矢印。等式を逆向きに使う | `rw [← h]` | [rw](tactics/rw.md) |
| `do` の `←` | 計算を実行し、その結果を受け取る | `let x ← action` | [do 記法](syntax/do.md) |
| `↑` | コーシオン。型変換を表す表示・記法 | `(↑n : Int)` | [norm_cast](tactics/norm_cast.md) |
| `;` | セミコロン。次のタクティクスへ進む | `constructor; exact hp` | [複数ゴールの構文](tactics/semicolon.md) |
| `<;>` | 左の操作で作られたすべてのゴールに右の操作を行う | `constructor <;> assumption` | [複数ゴールの構文](tactics/semicolon.md) |
| `*` | 対象をまとめて指定する。具体的な対象はタクティクスによる | `simp at *`、`simp [*]` | [simp](tactics/simp.md) |

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
