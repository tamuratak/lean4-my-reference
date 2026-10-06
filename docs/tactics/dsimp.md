# `dsimp`

`dsimp` は、**定義上の等しさを保つ計算や展開によって、式を簡単にする**タクティクスである。

`let` や関数適用を計算したいときに使える。

```lean
import Std.Tactic

example (n : Nat) : (fun x : Nat => x) n = n := by
  dsimp

example (n m : Nat) (h : n = m) : (let x := n; x) = m := by
  dsimp
  exact h
```

`simp` は一般の等式の定理も使うが、`dsimp` は定義上の等しさによる簡単化に使う。

`dsimp [定義名]` と展開する定義を指定したり、`dsimp at h` と仮定を指定したりできる。

| 書き方 | 通常の `dsimp` との違い |
| --- | --- |
| `dsimp!` | 条件やパターンが決まる関数定義の展開を積極的に試す |
| `dsimp?` | 簡単化を実行し、同じ処理に使える `dsimp only [...]` を提案する |
| `dsimp?!` | `dsimp!` の展開と、使った定義などに基づく提案を組み合わせる |

```lean
import Std.Tactic

def choose (n : Nat) : Nat :=
  match n with
  | 0 => 7
  | k + 1 => k

example (n m : Nat) (h : n = m) : choose (n + 1) = m := by
  fail_if_success dsimp
  guard_target =ₛ choose (n + 1) = m
  dsimp!
  guard_target =ₛ n = m
  exact h
```

この例では通常の `dsimp` だけでは `choose` を展開しない。`fail_if_success` で `dsimp` が失敗することを確認し、`guard_target =ₛ ...` でゴールの構文上の形を検査している。`dsimp!` は後者のパターンを使い、ゴールを `n = m` にする。`dsimp [choose]` と展開する定義を明示する方法もある。

```lean
import Std.Tactic

example (n m : Nat) (h : n = m) : (let x := n; x) = m := by
  dsimp?
  exact h
```

この例では `dsimp only` が提案され、ゴールは `n = m` になる。`?` は証明探索を追加する記号ではなく、簡単化に使える書き方の提案を追加する。`dsimp!` と `dsimp?!` も、定義上の等しさを保つという点は通常の `dsimp` と同じである。

参照：[公式 API：`dsimp`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.dsimp)、[公式 API：`dsimp?`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.dsimpTrace)。

[タクティクス一覧に戻る](README.md)
