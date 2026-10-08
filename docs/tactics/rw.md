# `rw`

`rw` は、等式や同値を使って、ゴールや仮定を書き換えるタクティクスである。

`h : a = b` があれば、`rw [h]` は `a` を `b` に書き換える。

```lean
example (a b : Nat) (h : a = b) : a + 1 = b + 1 := by
  rw [h]
```

逆向きには `←` を付ける。仮定を書き換えるには `at` を付ける。

```lean
example (P : Nat → Prop) (a b : Nat) (h : a = b) (ha : P a) : P b := by
  rw [h] at ha
  exact ha

example (a b : Nat) (h : a = b) : b + 1 = a + 1 := by
  rw [← h]
```

複数なら `rw [h₁, h₂]` と書く。`rw` は書き換えの後、定義上の等しさでゴールを閉じることも試す。`rewrite` はその最後の処理を行わない。

## `at h ⊢` による仮定とゴールの同時書き換え

`at` の後には、書き換える仮定名を空白で区切って並べる。そこに `⊢` を加えると、現在のゴールも対象になる。ここでの `⊢` は、状態表示の区切りではなく、コード中で操作対象を指定する記号である。ASCII の `|-` でも同じ意味になる。

| 書き方 | 書き換える対象 |
| --- | --- |
| `rw [hab]` | ゴールのみ |
| `rw [hab] at h₁ h₂` | 指定した仮定のみ |
| `rw [hab] at h₁ h₂ ⊢` | 指定した仮定とゴール |
| `rw [hab] at *` | すべての仮定とゴール |

```lean
example (a b : Nat) (hab : a = b) (h : a = 0) : a = 0 := by
  rw [hab] at h ⊢
  exact h
```

`rw [hab] at h ⊢` により、仮定 `h : a = 0` は `h : b = 0` に、ゴール `a = 0` は `b = 0` に変わる。そのため `exact h` で終わる。

ゴールだけを操作する場合は `at` を省略できるため、`⊢` を書く必要はない。特定の仮定とゴールを一度に操作する場合に、この書き方が役立つ。`rewrite` や `simp` でも、同じように `at h ⊢` で対象を指定できる。

`rwa [h]` は `rw [h]` の後に `assumption` を試す書き方である。`erw` は通常の `rw` より定義の展開を許して書き換える。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`rw`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.rwSeq)。

[タクティクス一覧に戻る](README.md)
