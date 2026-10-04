# `#check_tactic`・`#check_simp`

`#check_tactic` は、**タクティクスによる式の変形が、期待した結果になることを検査する**コマンドである。主にタクティクスや簡単化規則の動作確認に使う。

```lean
import Lean

#check_tactic (fun n : Nat => n + 0) ~> (fun n : Nat => n) by simp
```

`~>` の左が元の式、右が期待する式である。`by` の後が、検査のために実行するタクティクスになる。ここでは `simp` が関数の本体の `n + 0` を `n` に変えることを確認する。

内部では式の変形を確認するための専用のゴールを作る。普通の定理を証明する `example … := by …` とは使い方が異なり、この検査ではゴールを完全に閉じることも期待された結果とは扱わない。

`#check_simp` は、同じ検査を `simp` に限定した短い書き方である。

```lean
import Lean

#check_simp (fun n : Nat => n + 0) ~> (fun n : Nat => n)
```

タクティクスが失敗することは `#check_tactic_failure`、`simp` が変形できず失敗することは `#check_simp … !~>` で確認できる。

```lean
import Lean

#check_tactic_failure (3 : Nat) by fail
#check_simp (fun n : Nat => n) !~>
```

これらは検査用のトップレベルコマンドであり、既存の定理のゴールをその場で操作する命令ではない。一般的な証明での簡単化は[タクティクスの `simp`](../tactics/simp.md)を参照。

参照：[公式 API：タクティクス検査の構文](https://lean-lang.org/doc/api/Init/Notation.html#Lean.Parser.checkTactic)、[公式 API：CheckTactic](https://lean-lang.org/doc/api/Lean/Elab/CheckTactic.html)。

[`#` コマンドの一覧に戻る](README.md)
