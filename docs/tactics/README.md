# 標準タクティクスの日本語リファレンス

各ページは「何をするか」「仮定やゴールがどう変わるか」「短い証明例」を中心に説明する。Markdown はすべてこのディレクトリの直下に置いている。

`·`、`<;>`、`←` など、記号から探したい場合は[記号索引](../symbols.md)を参照。

## 対象と例の実行方法

対象は **Lean 4.35.0-rc3 に同梱されるタクティクス**。Lean 本体と標準ライブラリ `Std` を使い、mathlib などの追加ライブラリには依存しない。バージョンはルートの `lean-toolchain` で固定している。

各ページの `lean` コードブロックは、原則として次の行をファイルの先頭に加えると、それぞれ独立に実行できる。

```lean
import Std.Tactic
```

`run_tac` の例は、コード内に書いた `import Lean` も必要である。`open Std.Do` はプログラム検証用の例に明記している。

- `lean`：完成した証明・定義。自動検証の対象。
- `text`：仮定やゴールの表示、説明用の断片。単独で実行するコードではない。
- `lean-incomplete`：`sorry` に相当する穴を残す、開発中の操作例。完成した証明の検証から除外。

タクティクスとは、`by` の中で仮定やゴールを操作し、証明を組み立てるための命令である。状態表示の `⊢ P` は「いま `P` を証明する必要がある」という意味を表す。`hp : P` は「`P` の証明を `hp` という名前で使える」という意味である。

論理学では `Γ ⊢ P` は「仮定 `Γ` から `P` を導出できる」ことを表す。Lean の状態表示は、これから解決する課題を示しており、表示だけでは証明できることを保証しない。詳しくは [`by` のページの「`⊢` と証明状態の読み方」](../syntax/by.md)を参照。

```lean
example (P : Prop) : P → P := by
  intro hp
  exact hp
```

## 最初に読むページ

1. [intro](intro.md)：ゴールから変数や前提を取り出す。
2. [exact](exact.md)・[apply](apply.md)・[refine](refine.md)：証明や定理を使う。
3. [constructor](constructor.md)・[rcases](rcases.md)：論理の構造を作る・分解する。
4. [rw](rw.md)・[simp](simp.md)：式を書き換える・簡単にする。
5. [cases](cases.md)・[induction](induction.md)：場合分け・帰納法を使う。
6. [複数ゴールの構文](semicolon.md)：`·`、`;`、`<;>` を読む。

## やりたいことから選ぶ

| やりたいこと | 候補 |
| --- | --- |
| 手元にゴールの証明がある | [exact](exact.md)、[assumption](assumption.md) |
| 定理の前提を証明すればよい | [apply](apply.md)、[refine](refine.md) |
| 存在命題の中身を取り出す | [rcases](rcases.md)、[obtain](obtain.md) |
| 存在命題の証人を決める | [exists](exists.md)、[refine](refine.md) |
| 論理積を証明する | [constructor](constructor.md)、[and_intros](and_intros.md) |
| 論理和の片側を証明する | [left](left.md)、[right](right.md) |
| 等式を使って変形する | [rw](rw.md)、[subst](subst.md) |
| 仮定も含めて簡単化する | [simp_all](simp_all.md) |
| 関数どうしの等しさを示す | [funext](funext.md)、[ext](ext.md) |
| 自然数や整数の線形算術を解く | [omega](omega.md)、[lia](lia.md) |
| 多項式の等式を解く | [grobner](grobner.md) |
| 定理名や証明方法を探す | [exact?](exact_search.md)、[try?](try_search.md) |

## 用途別一覧

関連する変種や別名は代表ページにまとめている。独立したページがあるものは、その名前で探せる。内部実装用の補助構文、ユーザー定義タクティクス、属性や設定の全項目、`conv`・`grind` 内部の専用言語の全命令までは一覧化しない。

### 証明の基本

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [intro](intro.md) | ゴールの引数や仮定を、名前を付けて取り出す | — |
| [exact](exact.md) | ゴールそのものの証明を渡して、そのゴールを閉じる | — |
| [apply](apply.md) | 結論がゴールに合う定理を使い、その前提を新しいゴールにする | — |
| [refine](refine.md) | 証明の形を指定し、`?_` の部分を新しいゴールとして残す | `refine'` |
| [assumption](assumption.md) | 現在の仮定から、ゴールをそのまま証明できるものを探す | — |
| [have](have.md) | 途中で使う補助的な事実を証明し、仮定に追加する | `have'` |
| [let](let.md) | 証明の途中で、値を持つ局所的な定義を作る | `let'`、`let rec` |
| [suffices](suffices.md) | 本来のゴールを証明するために十分な、別の命題を提示する | — |
| [intros](intros.md) | 導入できる引数や仮定をまとめて導入する | — |

### 論理

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [constructor](constructor.md) | ゴールの帰納型のコンストラクターを適用し、その引数をゴールにする | — |
| [left](left.md) | 論理和のゴールで、左側を証明する方針を選ぶ | — |
| [right](right.md) | 論理和のゴールで、右側を証明する方針を選ぶ | — |
| [exists](exists.md) | 存在命題のゴールで、具体的な証人を指定する | — |
| [by_cases](by_cases.md) | 命題が成り立つ場合と、成り立たない場合に分ける | — |
| [classical](classical.md) | 古典論理に基づく判定可能性などを、後続の証明で使えるようにする | — |
| [exfalso](exfalso.md) | 現在のゴールを `False` に変え、矛盾から証明する形にする | — |
| [contradiction](contradiction.md) | 仮定の中にある明らかな矛盾を見つけて、ゴールを閉じる | — |
| [false_or_by_contra](false_or_by_contra.md) | ゴールの形に応じて仮定を導入し、最終的に `False` を示す形にする | — |
| [and_intros](and_intros.md) | ゴールに入れ子で現れる論理積を、まとめて分解する | — |

### 分解・場合分け・帰納法

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [cases](cases.md) | 帰納型の値を、コンストラクターごとに場合分けする | — |
| [rcases](rcases.md) | 仮定にある帰納型の値を、パターンに従ってまとめて分解する | `rcases?` |
| [rintro](rintro.md) | `intro` と `rcases` を組み合わせ、導入した仮定をその場で分解する | `rintro?` |
| [obtain](obtain.md) | 事実を受け取り、パターンに従ってその中身を取り出す | — |
| [induction](induction.md) | 帰納型の値について場合分けし、再帰的な成分について帰納法の仮定を作る | — |
| [injection](injection.md) | 同じコンストラクターで作った値の等式から、引数どうしの等式を取り出す | `injections` |
| [split](split.md) | `if` や `match` を含む式を、その分岐に沿って場合分けする | — |
| [nomatch](nomatch.md) | コンストラクターの形から不可能な値を排除する | `nofun` |
| [fun_induction](fun_induction.md) | 再帰関数の定義に沿った帰納法を行う | — |
| [fun_cases](fun_cases.md) | 関数の定義に沿って場合分けする | — |

### 等式・外延性

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [rfl](rfl.md) | 定義に従って計算すると同じになる等式などを証明する | `rfl'`、`eq_refl`、`apply_rfl` |
| [rw](rw.md) | 等式や同値を使って、ゴールや仮定を書き換える | — |
| [subst](subst.md) | 等式で結ばれた変数を置き換え、不要になった変数と等式を取り除く | `subst_vars`、`subst_eqs` |
| [symm](symm.md) | 等式など、対称な関係の向きを反転する | — |
| [calc](calc.md) | 中間の式を並べ、等式や不等式を推移性でつなぐ | — |
| [congr](congr.md) | 同じ関数などの等式を、対応する引数の等式に分解する | — |
| [funext](funext.md) | 関数どうしの等式を、任意の入力での値の等式に変える | — |
| [ext](ext.md) | 外延性の定理を使い、値どうしの等式を成分や入力ごとの等式に変える | — |
| [ac_rfl](ac_rfl.md) | 結合則と交換則による並べ替えで等しい式を証明する | — |
| [rewrite](rewrite.md) | 等式や同値による書き換えだけを行う | — |
| [rwa](rwa.md) | `rw` で書き換えた後、仮定でゴールを閉じる | — |
| [erw](erw.md) | 通常の `rw` より定義の展開を許して書き換える | — |
| [symm_saturate](symm_saturate.md) | 仮定にある対称な関係について、逆向きの事実も追加する | — |
| [ext1](ext1.md) | 外延性の定理を一段階だけ適用する | — |
| [apply_ext_theorem](apply_ext_theorem.md) | ゴールに合う外延性の定理を適用する | — |
| [ac_nf](ac_nf.md) | 結合則と交換則を使って、式を共通の標準形に並べ替える | `ac_nf0` |

### 書き換え・簡単化・型変換

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [simp](simp.md) | 登録された等式や同値を使い、式や命題を簡単な形にする | `simp!`、`simp?`、`simp?!` |
| [simpa](simpa.md) | ゴールと渡した証明の型を簡単化し、それらを合わせて証明を閉じる | `simpa!`、`simpa?`、`simpa?!` |
| [simp_all](simp_all.md) | ゴールと仮定を、互いの情報を使って繰り返し簡単化する | `simp_all!`、`simp_all?`、`simp_all?!` |
| [dsimp](dsimp.md) | 定義上の等しさを保つ計算や展開によって、式を簡単にする | `dsimp!`、`dsimp?`、`dsimp?!` |
| [unfold](unfold.md) | 指定した定義を、その定義式に従って展開する | — |
| [delta](delta.md) | 指定した定数を、その定義本体に置き換える | — |
| [norm_cast](norm_cast.md) | 型変換が絡む式を、登録された補題で整理する | `norm_cast0` |
| [conv](conv.md) | 式の特定の部分を選び、その部分だけを書き換える | — |
| [simp_arith](simp_arith.md) | 算術の簡単化を有効にして、`simp` を行う | `simp_arith!`、`simp_all_arith`、`simp_all_arith!` |
| [push_cast](push_cast.md) | 型変換を演算の内側へ移して、変換後の演算に揃える | — |
| [exact_mod_cast](exact_mod_cast.md) | 型変換を整理し、渡した証明をゴールに合わせる | `apply_mod_cast`、`rw_mod_cast`、`assumption_mod_cast` |

### 仮定とゴールの整理

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [change](change.md) | ゴールや仮定を、定義上等しい別の書き方に変える | — |
| [show](show.md) | 証明したいゴールを、型を書いて選び直す | — |
| [revert](revert.md) | 局所変数や仮定を、ゴールの引数や前提へ戻す | — |
| [clear](clear.md) | この先で不要な局所変数や仮定を取り除く | — |
| [rename_i](rename_i.md) | Lean が内部的に付けた、直接使いにくい名前を付け直す | `rename` |
| [specialize](specialize.md) | 全称命題や含意の仮定に引数を渡し、具体化した仮定に置き換える | — |
| [generalize](generalize.md) | 式を新しい変数に置き換え、必要なら元の式との等式を残す | — |
| [replace](replace.md) | 新しい事実を追加し、同じ名前の古い仮定が不要なら取り除く | — |
| [clear_value](clear_value.md) | 局所定義の値を忘れ、名前と型だけを残す | — |
| [extract_lets](extract_lets.md) | 式の中にある `let` を、局所定義として外へ取り出す | — |
| [lift_lets](lift_lets.md) | 式の内部の `let` を、式の外側へ移す | — |
| [let_to_have](let_to_have.md) | 値を展開する必要がない `let` を、`have` の形に変える | — |

### 自動化・計算

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [trivial](trivial.md) | 仮定、反射性、簡単化などで閉じられる簡単なゴールを試す | — |
| [decide](decide.md) | 命題の判定手続きを計算して、真であることを証明する | — |
| [native_decide](native_decide.md) | 命題の判定手続きをコンパイルして実行し、その結果から証明する | — |
| [omega](omega.md) | 自然数や整数の線形な等式・不等式を使って、算術的なゴールを証明する | — |
| [grind](grind.md) | 等式、論理的な仮定、算術などを組み合わせて自動で証明を探す | `grind?`、`grind =>` |
| [solve_by_elim](solve_by_elim.md) | 仮定や指定した補題を後ろ向きに適用し、残る前提も再帰的に証明する | — |
| [apply_assumption](apply_assumption.md) | ゴールに合う仮定を適用し、必要な前提を新しいゴールにする | — |
| [apply_rules](apply_rules.md) | 指定した補題や仮定を繰り返し適用して、ゴールを小さな課題へ分ける | — |
| [exact?](exact_search.md) | ライブラリや仮定から、ゴールを閉じる証明を探して提案する | — |
| [bv_decide](bv_decide.md) | 固定ビット幅の演算や論理を、SAT ソルバーを使って証明する | `bv_normalize`、`bv_decide?`、`bv_check` |
| [bv_omega](bv_omega.md) | ビットベクトルの算術を自然数の条件に変換し、`omega` で解く | — |
| [cbv](cbv.md) | 式を値の計算として評価し、ゴールや仮定を簡単にする | `decide_cbv` |
| [lia](lia.md) | `grind` の整数線形算術の機能に絞って証明する | `cutsat` |
| [grobner](grobner.md) | 可換な環や半環上の多項式の等式を証明する | — |
| [try?](try_search.md) | 複数の証明方法を自動で試し、成功した証明を提案する | `suggestions`、`∎` |
| [grind_order](grind_order.md) | `grind` の順序についての推論に絞って証明する | — |
| [apply?](apply_search.md) | 適用できる補題を探し、残る前提も確認できるようにする | — |
| [rw?](rw_search.md) | ゴールや仮定を書き換えられる補題を探して提案する | — |
| [grind_linarith](grind_linarith.md) | `grind` の線形算術の機能に絞って証明する | — |

### 複数ゴールと制御

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [case](case.md) | 名前の付いたゴールを選び、その場合の証明を書く | `case'` |
| [next](next.md) | 次のゴールを選び、必要ならその仮定に名前を付けて証明する | — |
| [all_goals](all_goals.md) | 現在あるすべてのゴールに、同じタクティクスを適用する | — |
| [any_goals](any_goals.md) | 現在あるゴールのうち、指定したタクティクスが成功するものを処理する | — |
| [focus](focus.md) | 現在の先頭のゴールにだけ注目して、内側の証明を進める | — |
| [first](first.md) | 複数の候補を順番に試し、最初に成功したものを採用する | — |
| [try](try.md) | 指定したタクティクスを試し、失敗したら何もせず先へ進む | — |
| [repeat](repeat.md) | 指定したタクティクスを、失敗するまで繰り返す | `repeat'`、`repeat1'` |
| [solve](solve.md) | 候補を順番に試し、対象のゴールをすべて閉じるものを採用する | — |
| [rotate_left](rotate_left.md) | ゴールの順番を左へ回し、次のゴールを先頭にする | `rotate_right` |
| [skip](skip.md) | 証明状態を変えずに成功する | — |
| [done](done.md) | 未解決のゴールが残っていないことを確認する | — |
| [fail_if_success](fail_if_success.md) | 内側のタクティクスが失敗することを確認する | `fail` |
| [`;`・`<;>`・`·`](semicolon.md) | タクティクスを組み合わせ、作られたゴールを続けて処理する | — |
| [match](match.md) | 値の形ごとに、タクティクスの証明を分ける | — |
| [if](if.md) | 判定可能な条件に応じて、証明の分岐を選ぶ | — |

### 確認・高度な操作・開発中の穴

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [guard_target](guard_target.md) | ゴールが想定した型になっていることを確認する | `guard_hyp`、`guard_expr` |
| [trace_state](trace_state.md) | 現在の仮定とゴールをメッセージに表示する | `trace`、`dbg_trace` |
| [show_term](show_term.md) | タクティクスが作った証明項を表示する | — |
| [infer_instance](infer_instance.md) | 型クラスのインスタンスを探して、ゴールを閉じる | `haveI`、`letI` |
| [as_aux_lemma](as_aux_lemma.md) | 内側のタクティクスで作る証明を、補助的な定理にまとめる | — |
| [with_reducible](with_reducible.md) | 内側のタクティクスで、定義の展開の強さを制限する | `with_reducible_and_instances`、`with_unfolding_all`、`with_unfolding_none` |
| [expose_names](expose_names.md) | 仮定の内部名を、証明から参照できる名前にする | `unhygienic` |
| [run_tac](run_tac.md) | タクティクスの実装用の Lean コードを、証明の途中で実行する | — |
| [simp_wf](simp_wf.md) | 整礎再帰の停止性のゴールを簡単化する | `decreasing_trivial`、`decreasing_trivial_pre_omega` |
| [get_elem_tactic](get_elem_tactic.md) | 添字アクセスに必要な、添字が範囲内にあるという条件を証明する | `get_elem_tactic_trivial`、`get_elem_tactic_extensible` |
| [impossible](impossible.md) | 現在のゴールが一般には証明できないことを、反例によって確認する | — |
| [sorry](sorry.md) | まだ書けていない証明を、仮の穴として受け入れさせる | `admit`、`stop` |
| [sleep](sleep.md) | 指定したミリ秒だけ待ち、証明状態を変えずに進む | — |
| [sym](sym.md) | 共有された式の表現を使う証明モードで、簡単化や推論を実行する | — |

### プログラム検証と状態を扱う論理

用途や記法が分からない場合は、[プログラム検証の案内：`mstart` と関連タクティクス](program_verification.md)から読む。通常の証明との関係、短い例、読む順番、用途別のリンクをまとめている。

| ページ | 何をするか | 関連する変種・別名 |
| --- | --- | --- |
| [mstart](mstart.md) | 状態を扱う命題の証明モードを開始する | — |
| [mintro](mintro.md) | 状態を扱う証明モードで、前提を名前付きの仮定として取り出す | — |
| [mexact](mexact.md) | 状態を扱う証明モードで、ゴールに合う証明を渡す | — |
| [massumption](massumption.md) | 状態を扱う仮定から、ゴールに合うものを探す | — |
| [mconstructor](mconstructor.md) | 状態を扱うゴールの論理積などを分ける | — |
| [mleft](mleft.md) | 状態を扱う論理和のゴールで、左側を選ぶ | — |
| [mright](mright.md) | 状態を扱う論理和のゴールで、右側を選ぶ | — |
| [mcases](mcases.md) | 状態を扱う仮定を、パターンで分解する | — |
| [mclear](mclear.md) | 状態を扱う証明モードから、不要な仮定を取り除く | — |
| [mdup](mdup.md) | 状態を扱う仮定に、複製した別名を付ける | — |
| [mspecialize](mspecialize.md) | 状態を扱う全称命題や含意の仮定を具体化する | — |
| [mhave](mhave.md) | 状態を扱う証明モードに、補助的な事実を追加する | — |
| [mreplace](mreplace.md) | 状態を扱う仮定を、新しく証明した事実に置き換える | — |
| [mexists](mexists.md) | 状態を扱う存在命題のゴールに、証人を渡す | — |
| [mrefine](mrefine.md) | 状態を扱う証明の形を指定し、穴をゴールとして残す | — |
| [mexfalso](mexfalso.md) | 状態を扱うゴールを、偽を示す形に変える | — |
| [mpure_intro](mpure_intro.md) | 状態を扱うゴールが純粋な命題なら、普通の命題の証明へ移る | — |
| [mpure](mpure.md) | 状態によらない仮定を、普通の Lean の仮定として取り出す | — |
| [mframe](mframe.md) | 状態によらない仮定を見つけ、普通の仮定へ移す | — |
| [mrevert](mrevert.md) | 状態を扱う仮定を、ゴールの前提へ戻す | — |
| [mrename_i](mrename_i.md) | 状態を扱う仮定の内部名に、使いやすい名前を付ける | — |
| [mstop](mstop.md) | 状態を扱う証明モードを止め、そのモードで付けた仮定の名前を忘れる | — |
| [mleave](mleave.md) | 状態を扱う証明モードを抜け、普通の Lean の命題へ展開する | — |
| [mspecialize_pure](mspecialize_pure.md) | 普通の局所仮定にある事実を、状態を扱う仮定などで具体化する | — |
| [mvcgen](mvcgen.md) | プログラムの仕様を証明するための条件を、実行の構造に従って生成する | `mvcgen?` |
| [mspec](mspec.md) | プログラムの仕様を表す定理を適用し、前提や事後条件の確認をゴールにする | — |

## 標準に含まれるか迷ったとき

`rcases`、`rintro`、`obtain`、`omega`、`grind`、`norm_cast` はこのバージョンの Lean 本体に含まれる。一方、一般の証明モードで使う `aesop`、`linarith`、`nlinarith`、`ring`、`norm_num`、`by_contra`、`push_neg` などは、このリファレンスの対象の標準インポートだけでは使えない。

名前が似ていても、`grind_linarith` と `linarith` は別の操作である。また、`grind` の内部言語にある `by_contra` と、一般の `by` 証明で使うタクティクスも区別する。

これらの追加タクティクスは、[追加ライブラリの一覧](../library-tactics/README.md)から読む。[mathlib4](../library-tactics/mathlib/README.md) と [Aesop](../library-tactics/aesop/README.md) の解説は別ディレクトリに置いている。

## 例の検証

リポジトリのルートで次を実行する。Python 3 と、`lean-toolchain` が指定する Lean を用意しておく。

```sh
python3 scripts/check_examples.py
```

このスクリプトは Markdown の各 `lean` ブロックに共通インポートを補い、独立した一時ファイルとして Lean に渡す。エラーや `sorry` を含む完成例は失敗として扱う。出力や警告を意図的に表示する例もあるため、メッセージが出ること自体は失敗ではない。

引数なしの実行は追加ライブラリの例も含むため、その依存環境の準備が必要になる。このディレクトリの標準例だけなら `python3 scripts/check_examples.py docs/tactics/*.md` で、追加ライブラリなしに検証できる。

一つのページだけを確認する場合はファイルを指定できる。

```sh
python3 scripts/check_examples.py docs/tactics/rcases.md
```

## 参照資料

説明と例は、インストール済み Lean 4.35.0-rc3 の構文・実装とコンパイル結果を確認して作成した。公式リファレンスの `latest` は将来の変更を含み得るため、このリファレンスの動作確認は固定したバージョンを基準にする。

- [Lean 公式リファレンス：Tactic Reference](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)
- [Lean 公式リファレンス：The Tactic Language](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)
- [Lean 公式 API ドキュメント](https://lean-lang.org/doc/api/)
