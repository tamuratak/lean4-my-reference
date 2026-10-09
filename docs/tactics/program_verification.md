# Leanでのプログラム検証の概要

`mstart`・`mintro`・`mexact` などは、プログラムの状態についての条件や、プログラムの仕様を証明するためのタクティクスである。

プログラム検証も Lean による数学的な証明である。通常の定理証明との違いは、主に扱う対象と、それを表す論理・記法にある。自然数の等式や一般の命題を証明するだけなら、まず [`intro`](intro.md)・[`exact`](exact.md)・[`rcases`](rcases.md) などを学べばよく、この一群を同時に覚える必要はない。

## プログラムの状態と証明状態の違い

ここでの状態は、検証するプログラムが保持する値である。例えばカウンターの現在値や、更新するデータなどが該当する。「カウンターが５以上」という条件は、その状態によって真偽が変わる。

Lean が表示する仮定とゴールの「証明状態」とは区別する。`mstart` はプログラムを実行したり、カウンターを変更したりする操作ではなく、状態についての条件を証明するためのモードを開始する。

## プログラム検証の基本記法

| 記法 | 意味 |
| --- | --- |
| `P : Prop` | 通常の命題 |
| `P : SPred σs` | 状態に応じて成り立つ条件。`σs` は状態の型を並べたもの |
| `P ⊢ₛ Q` | どの状態でも、条件 `P` が成り立てば条件 `Q` も成り立つ |
| `⊢ₛ Q` | どの状態でも条件 `Q` が成り立つ |
| `⌜R⌝` | 通常の命題 `R : Prop` を、状態に依存しない条件として埋め込む |
| `⦃P⦄ program ⦃Q⦄` | 前提 `P` のもとでプログラムを実行すると、事後条件 `Q` が成り立つという仕様 |
| `⇓ x => …` | プログラムの返り値を `x` と呼んで事後条件を書く |

`P ⊢ₛ Q` は同じ状態での条件どうしの関係を表す。例えば「カウンターが10以上なら５以上でもある」という関係であり、状態の更新は表していない。実行前後の条件を結び付ける仕様は `⦃P⦄ program ⦃Q⦄` で表す。

仕様を囲む `⦃…⦄` は、引数の厳密な暗黙の括弧 `⦃x : α⦄` とは別の記法である。[記号索引](../symbols.md)も参照。

## 通常の命題と状態述語における論理積の証明

通常の命題で「`P` と `Q` が成り立つなら `Q`」を証明する例は、次のようになる。追加のインポートは不要である。

```lean
example (P Q : Prop) : P ∧ Q → Q := by
  intro h
  rcases h with ⟨hP, hQ⟩
  exact hQ
```

状態についての条件でも、同じ論理の流れを使える。こちらは標準の `Std.Tactic.Do` をインポートし、`Std.Do` の名前を使う。

```lean
import Std.Tactic.Do
open Std.Do

example (σs : List Type) (P Q : SPred σs) : P ∧ Q ⊢ₛ Q := by
  mstart
  mintro h
  mcases h with ⟨hP, hQ⟩
  mexact hQ
```

`mstart` は `P ∧ Q ⊢ₛ Q` を、前提を導入できる形にする。`mintro h` が前提に名前を付け、`mcases` が２つの条件に分解し、`mexact hQ` が取り出した `Q` を使って閉じる。

このモード内の `hP`・`hQ` は、状態についての仮定に付けた名前である。通常の局所仮定と同じように `exact` で扱うのではなく、対応する `m…` の操作を使う。`mintro` は必要ならモードの開始も行うため、上の `mstart` は省略できる。

## `mvcgen` による仕様からの証明条件の生成

```lean
import Std.Tactic.Do
open Std.Do

example : ⦃⌜True⌝⦄ (pure 3 : Id Nat) ⦃⇓ n => ⌜n = 3⌝⦄ := by
  mvcgen
```

この仕様は「前提は `True`、プログラムは３を返し、その返り値 `n` は３と等しい」と読む。状態を更新しない簡単な例だが、仕様の記法の形を確認できる。

`mvcgen` は実行の構造に従って証明条件を生成する。この例では自動で閉じる。より複雑なプログラムでは条件が残り、その条件を `m…` のタクティクスや通常のタクティクスで証明する。ループでは不変条件が必要になることもある。

## 最初に読む順番

1. [`mstart`](mstart.md)・[`mintro`](mintro.md)・[`mexact`](mexact.md)：モードを始め、前提を取り出し、それを使う。
2. [`mcases`](mcases.md)・[`mconstructor`](mconstructor.md)：条件を分解する・組み立てる。
3. [`mpure`](mpure.md)・[`mpure_intro`](mpure_intro.md)・[`mleave`](mleave.md)：通常の命題の証明との行き来を理解する。
4. [`mvcgen`](mvcgen.md)・[`mspec`](mspec.md)：プログラムの仕様から証明を進める。

## 用途別のリンク一覧

### モードの開始と終了

| ページ | 用途 |
| --- | --- |
| [`mstart`](mstart.md) | 状態についての証明モードを開始する |
| [`mstop`](mstop.md) | モードを停止し、そこで付けた仮定名を忘れる |
| [`mleave`](mleave.md) | 条件を通常の Lean の命題へ展開し、通常のタクティクスへ移る |

`mstop` は、条件を通常の命題へ展開する操作ではない。`simp`・`grind` などで残った条件を証明したいときは、`mleave` を検討する。

### 仮定の利用と整理

| ページ | 用途 |
| --- | --- |
| [`mintro`](mintro.md) | 前提を導入して名前を付ける |
| [`mexact`](mexact.md) | ゴールに合う証明を渡す |
| [`massumption`](massumption.md) | ゴールに合う仮定を探す |
| [`mhave`](mhave.md) | 補助的な事実を証明して追加する |
| [`mspecialize`](mspecialize.md) | 全称命題や含意の仮定に引数を渡して具体化する |
| [`mreplace`](mreplace.md) | 仮定を新しく証明した事実に置き換える |
| [`mclear`](mclear.md) | 不要な仮定を取り除く |
| [`mdup`](mdup.md) | 仮定に複製した別名を付ける |
| [`mrevert`](mrevert.md) | 仮定をゴールの前提へ戻す |
| [`mrename_i`](mrename_i.md) | 内部的に付いた仮定名を使いやすい名前にする |

### 論理構造の分解と構築

| ページ | 用途 |
| --- | --- |
| [`mcases`](mcases.md) | 仮定をパターンで分解する |
| [`mconstructor`](mconstructor.md) | 論理積などのゴールを分ける |
| [`mleft`](mleft.md)・[`mright`](mright.md) | 論理和のどちら側を証明するか選ぶ |
| [`mexists`](mexists.md) | 存在条件を満たす証人を指定する |
| [`mrefine`](mrefine.md) | 証明の形を指定し、穴を新しいゴールにする |
| [`mexfalso`](mexfalso.md) | 偽を示すゴールに変え、矛盾から証明する |

### 状態に依存しない条件と通常の命題の間の移行

| ページ | 用途 |
| --- | --- |
| [`mpure`](mpure.md) | 指定した状態に依存しない仮定を、通常の仮定として取り出す |
| [`mpure_intro`](mpure_intro.md) | ゴールの `⌜R⌝` を、通常の命題 `R` の証明へ移す |
| [`mframe`](mframe.md) | 状態に依存しない仮定を探して、通常の仮定へ移す |
| [`mspecialize_pure`](mspecialize_pure.md) | 通常の局所仮定にある事実を、モード内の仮定などで具体化する |

状態に依存する条件を、すべて `mpure` で通常の仮定にできるわけではない。`mpure_intro` は状態についての前提を捨てて純粋な命題を証明するため、必要な純粋な仮定は先に取り出しておく。

### プログラムの仕様の利用

| ページ | 用途 |
| --- | --- |
| [`mvcgen`・`mvcgen?`](mvcgen.md) | プログラムから証明条件を生成する。不変条件の候補を表示する変種もある |
| [`mspec`](mspec.md) | 操作の仕様を表す定理を使い、前提や事後条件の確認へ進む |

この一覧は、このリファレンスに専用ページがある `Std.Do` 関連の操作をまとめたものである。`match` など、単に名前が `m` で始まるタクティクスすべてが、この証明モード用というわけではない。

参照：[公式 API：Std.Tactic.Do.Syntax](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html)、[公式 API：mstart](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mstart)、[公式 API：mvcgen](https://lean-lang.org/doc/api/Std/Tactic/Do/Syntax.html#Lean.Parser.Tactic.mvcgen)。

[タクティクス一覧に戻る](README.md) · [リファレンスの入口に戻る](../../README.md)
