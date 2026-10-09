# 作成方針

- 自分で読み返して理解しやすい、Lean の日本語リファレンスを作る。
- 概要は必要なら plan.md を参照する。
- 記事タイトルと各セクションの見出しは、内容を的確に表す名詞句にする。「〜を表す」「〜を証明する」のような動詞で終わる文章ではなく、「〜の表現」「〜の証明」のように名詞で終える。
- `rcases_example.md` を説明量と具体例の基準にする。「何をするか → 仮定やゴールがどう変わるか → 短い具体例」を中心に、似た操作との違いも必要な範囲で説明する。
- 記事や節の冒頭では、説明対象の意味・用途・基本的な挙動を説明する。対象の説明より先に「〜ではない」という否定や、別の項目との区別・参照案内を置かない。混同しやすい記法との違い、制約、例外などの注意は、基本説明や具体例の後に独立した段落や内容を示す見出しで見つけやすく示す。
- mathlib の数学リファレンス（`docs/mathlib/`）は `mathlib_deriv_example.md` を説明の形式と説明量の基準にする。数学の概念・数式を mathlib でどう表すかを中心に、「数学の対象 → 数学と Lean の対応表 → 表現の意味と成立条件」を説明する。
- README.md は作業記録用のファイルではない。README.md は特に指示がない場合には編集しない。
- 参照リンクには公式リファレンスマニュアル（https://lean-lang.org/doc/reference/latest/）または公式 API ドキュメント（https://lean-lang.org/doc/api/）を使う。可能なら該当項目へ直接リンクし、ソースコードへのリンクは使わない。
- 例は短く、コピーして実行できる形にする。必要なインポートを明示し、`lean-toolchain` のバージョンで確認する。通常の編集では `python3 scripts/check_examples.py --changed` または編集したファイルのパスを指定し、変更した記事だけを検証する。全件検証はユーザーが求めた場合、または検証スクリプト・`lean-toolchain`・Lake の依存設定など共通の検証条件を変更した場合に行う。
- 完成した例は `lean`、状態表示や説明用の断片は `text`、仮の穴を含む例は `lean-incomplete` のコードブロックに分ける。未完成の例を完成した証明として扱わない。
- チャットと解説は日本語、コード内のコメントは英語で書く。提案は無条件に肯定せず、実現可能性と効率を客観的に評価する。
- 数学記号は Unicode の字形を直接出さず、LaTeX コマンドで表す。例：`\alpha`、`\beta`、`\forall`、`\in`。
- 数学字体も Unicode の字形を直接出さず、LaTeX コマンドで表す。例：`\mathbb{R}`、`\mathbf{x}`、`\mathcal{F}`。
- 特別な理由がない限り 強調 ** を使わない。

- README や解説記事には、読者が Lean を理解・利用するための情報を書く。
- 作業報告や検証結果はチャットで伝えるか memo.md に書く。README や解説記事に追加しない。

## その他

- When searching in `.lake/`, exclude `*.ilean` and `*.olean` files from search. They are compiled files and not human-readable. They are noise for your context window. Focus on `.lean` files for source code.
