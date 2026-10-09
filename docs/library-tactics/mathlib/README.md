# mathlib のタクティクス

追加ライブラリ mathlib を通じて使う、代表的なタクティクスの一覧。各ページには必要なインポートと、短い証明例を載せる。全タクティクスの網羅的な一覧ではなく、用途別に学べる入口である。

多変数の微分積分など、数学の定義・定理の使い方は [mathlib の数学リファレンス](../../mathlib/README.md)を参照。

## 数値計算・代数・不等式

| ページ | 何をするか | 関連する操作 |
| --- | --- | --- |
| [norm_num](norm_num.md) | 具体的な数の計算と等式・不等式を証明する | `norm_num at h` |
| [ring](ring.md) | 多項式の両辺を整理して等式を証明する | [ring_nf](ring_nf.md) |
| [ring_nf](ring_nf.md) | 仮定やゴールの多項式を標準形にする | `ring_nf at h` |
| [linarith](linarith.md) | 線形な等式・不等式を組み合わせて証明する | `linarith only` |
| [nlinarith](nlinarith.md) | 積・平方の補助条件も利用して算術を証明する | `nlinarith only` |
| [positivity](positivity.md) | 正・非負・非零を式の構造から証明する | — |
| [field_simp](field_simp.md) | 分母の非零を確認して、分母を払う | `field_simp at h` |
| [abel](abel.md) | 可換な加法の式を整理して等式を証明する | `abel_nf` |
| [linear_combination](linear_combination.md) | 指定した等式の線形結合でゴールを証明する | — |

まず数値だけなら `norm_num`、多項式の等式なら `ring`、不等式の仮定を使うなら `linarith` を考える。平方や積が重要なら `nlinarith`、正であることだけが必要なら `positivity` が候補になる。

## 論理・背理法

| ページ | 何をするか | 関連する操作 |
| --- | --- | --- |
| [push_neg](push_neg.md) | 否定を内側へ押し込み、仮定やゴールを整理する | `push_neg at h` |
| [by_contra](by_contra.md) | ゴールの否定を仮定して矛盾を示す | `by_contra!` |
| [contrapose](contrapose.md) | 仮定とゴールを否定して入れ替える | `contrapose!` |
| [tauto](tauto.md) | 命題論理の構造を分解して証明する | — |

`by_contra` は Batteries 由来で、mathlib のインポートからも利用できる。規則を登録して論理の探索を広げる Aesop は[別の一覧](../aesop/README.md)で扱う。

## 式の一致・単調性

| ページ | 何をするか | 関連する操作 |
| --- | --- | --- |
| [convert](convert.md) | 証明の型とゴールの差を、等式のゴールとして残す | `convert ←` |
| [congr!](congr_exclamation.md) | 等式を対応する部分式の等式へ分解する | 深さの指定 |
| [gcongr](gcongr.md) | 不等式などを単調性で部分式の関係へ分解する | — |

## 有限な場合分け・証人の選択

| ページ | 何をするか |
| --- | --- |
| [fin_cases](fin_cases.md) | 有限型の値を列挙して場合分けする |
| [interval_cases](interval_cases.md) | 自然数・整数の上下限から値を列挙する |
| [choose](choose.md) | 入力ごとの存在証人を、関数とその性質として取り出す |

[依存の準備・検証状況](../README.md#例の実行と検証)を確認してから例を実行する。

[追加ライブラリの一覧に戻る](../README.md) · [Lean 本体の一覧](../../tactics/README.md)
