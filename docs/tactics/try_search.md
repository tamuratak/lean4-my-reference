# `try?`

`try?` は、**複数の証明方法を自動で試し、成功した証明を提案する**タクティクスである。

使うタクティクスが決まっていないときの候補探しに使える。

```lean
example (n : Nat) : n + 0 = n := by
  try?
```

成功するとゴールを閉じ、採用できる証明スクリプトを提案する。`try` は失敗を無視するための組合せだが、`try?` は証明を探すための操作である。

`suggestions` はエディター上の候補表示に関わる関連操作であり、`∎` も証明提案を利用するための書き方である。候補探しの後は、提案された `rfl` や `exact ...` を採用すると、使った方法が明示される。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`try?`](https://lean-lang.org/doc/api/Init/Try.html#Lean.Parser.Tactic.tryTrace)。

[タクティクス一覧に戻る](README.md)
