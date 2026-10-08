# `try?`

`try?` は、複数の証明方法を自動で試し、成功した証明を提案するタクティクスである。

使うタクティクスが決まっていないときの候補探しに使える。

```lean
import Std.Tactic

example (n : Nat) : n + 0 = n := by
  try?
```

成功するとゴールを閉じ、採用できる証明スクリプトを提案する。`try` は失敗を無視するための組合せだが、`try?` は証明を探すための操作である。

候補探しの後は、提案された `rfl` や `exact ...` を採用すると、使った方法が明示される。

## `suggestions`：提案エンジンの登録と定理候補の表示

`suggestions` は、現在のゴールに関連するライブラリの定理を表示する。候補を表示しただけではゴールを閉じない。提案エンジンの登録が必要であり、`import Std.Tactic` だけではエラーになる。Lean の標準エンジンを使うには `import Lean.LibrarySuggestions.Default` を追加する。

```lean
import Std.Tactic

example (n : Nat) : n + 0 = n := by
  fail_if_success suggestions
  rfl
```

この例は、提案エンジンを登録していないと `suggestions` が失敗することを検査する。次の例は別のファイルとして実行する。

```lean
import Lean.LibrarySuggestions.Default

example (n : Nat) : n + 0 = n := by
  suggestions
  rfl
```

`suggestions` の後にも `n + 0 = n` が残るので、この例では `rfl` で証明を完成させる。表示される候補はインポートや登録されたエンジンによって変わる。

## 証明終了記号の記法

`∎`（エディターで `\qed` と入力）は、証明探索を実行する記法である。タクティクスの位置では `try?` に、式の位置では `by try? (wrapWithBy := true)` に展開される。後者の設定は、提案に `by` を付けるためのものである。

```lean
import Std.Tactic

example (n : Nat) : n + 0 = n := by
  ∎

example (n : Nat) : n + 0 = n := ∎
```

どちらも `try?` で証明を探し、成功すればゴールを閉じる。書くだけで任意の証明が完了する記号ではない。

参照：[公式 API：`try?` と証明終了記号](https://lean-lang.org/doc/api/Init/Try.html)、[公式 API：`suggestions`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.suggestions)、[公式 API：標準の提案エンジン](https://lean-lang.org/doc/api/Lean/LibrarySuggestions/Default.html)。

[タクティクス一覧に戻る](README.md)
