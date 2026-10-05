# 作成方針

- 自分で読み返して理解しやすい、Lean の日本語リファレンスを作る。
- `rcases_example.md` を説明量と具体例の基準にする。「何をするか → 仮定やゴールがどう変わるか → 短い具体例」を中心に、似た操作との違いも必要な範囲で説明する。
- mathlib の数学リファレンス（`docs/mathlib/`）は `mathlib_deriv_example.md` を説明の形式と説明量の基準にする。数学の概念・数式を mathlib でどう表すかを中心に、「数学の対象 → 数学と Lean の対応表 → 表現の意味と成立条件」を説明する。
- 参照リンクには公式リファレンスマニュアル（https://lean-lang.org/doc/reference/latest/）または公式 API ドキュメント（https://lean-lang.org/doc/api/）を使う。可能なら該当項目へ直接リンクし、ソースコードへのリンクは使わない。
- 例は短く、コピーして実行できる形にする。必要なインポートを明示し、`lean-toolchain` のバージョンで `python3 scripts/check_examples.py` を実行して確認する。
- 完成した例は `lean`、状態表示や説明用の断片は `text`、仮の穴を含む例は `lean-incomplete` のコードブロックに分ける。未完成の例を完成した証明として扱わない。
- チャットと解説は日本語、コード内のコメントは英語で書く。提案は無条件に肯定せず、実現可能性と効率を客観的に評価する。
- 数学記号は Unicode の字形を直接出さず、LaTeX コマンドで表す。例：`\alpha`、`\beta`、`\forall`、`\in`。
- 数学字体も Unicode の字形を直接出さず、LaTeX コマンドで表す。例：`\mathbb{R}`、`\mathbf{x}`、`\mathcal{F}`。

## その他

- When searching in `.lake/`, exclude `*.ilean` and `*.olean` files from search. They are compiled files and not human-readable. They are noise for your context window. Focus on `.lean` files for source code.
