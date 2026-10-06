# `induction`

`induction` は、帰納型の値について場合分けし、再帰的な成分について帰納法の仮定を作るタクティクスである。

自然数では、ゼロの場合と後者の場合に分かれる。後者の場合には、小さい自然数についての結論を使える。

```lean
import Std.Tactic

example (n : Nat) : 0 + n = n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    change Nat.succ (0 + n) = Nat.succ n
    rw [ih]
```

`succ` の場合の `ih` は `0 + n = n` の証明である。これを使って `n + 1` の場合を示す。

`cases` との違いは、この `ih` が手に入ることである。

## `generalizing`：他の引数にも使える帰納法の仮定を作る

`induction n generalizing m` は、ローカル変数 `m` を固定せず、すべての `m` についての命題に帰納法を適用する。例えば、再帰呼び出しのたびに第二引数を増やす加算を考える。

```lean
import Std.Tactic

def addAcc : Nat → Nat → Nat
  | 0, m => m
  | n + 1, m => addAcc n (m + 1)

example (n m : Nat) : addAcc n m = n + m := by
  induction n generalizing m with
  | zero => simp only [addAcc, Nat.zero_add]
  | succ n ih =>
    simpa only [addAcc, Nat.succ_add, Nat.add_succ] using ih (m + 1)
```

`succ` の場合の帰納法の仮定は、指定の有無で次のように変わる。

```text
induction n:
  ih : addAcc n m = n + m

induction n generalizing m:
  ih : ∀ (m : Nat), addAcc n m = n + m
```

再帰呼び出しは `addAcc n (m + 1)` なので、固定した `m` についての仮定だけでは合わない。一般化すると `ih (m + 1)` を使え、その型は `addAcc n (m + 1) = n + (m + 1)` になる。`generalizing` の後には、このように帰納法の仮定で別の値へ適用したい変数名を指定する。指定した変数に依存する仮定も、必要に応じて一緒に一般化される。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`induction`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.induction)。

[タクティクス一覧に戻る](README.md)
