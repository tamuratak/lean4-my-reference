# `rewrite`

`rewrite` は、**等式や同値による書き換えだけを行う**タクティクスである。

`rw` と違い、書き換えの後に反射性でゴールを閉じる処理を行わない。

```lean
example (a b : Nat) (h : a = b) : a + 1 = b + 1 := by
  rewrite [h]
  rfl
```

`rewrite [h]` の後には `b + 1 = b + 1` が残る。そのため、続けて `rfl` と書いている。

逆向きには `rewrite [← h]`、仮定を対象にするなら `rewrite [h] at ha` と書く。通常は `rw` を使い、書き換え後の状態をあえて残したいときに `rewrite` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`rewrite`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.rewriteSeq)。

[タクティクス一覧に戻る](README.md)
