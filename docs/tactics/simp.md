# `simp`

`simp` は、**登録された等式や同値を使い、式や命題を簡単な形にする**タクティクスである。

例えば自然数の `0 + n` を `n` に簡単化できる。

```lean
import Std.Tactic

example (n : Nat) : 0 + n = n := by
  simp
```

`simp [h]` で手元の事実を追加し、`at h` で仮定を簡単化できる。

```lean
import Std.Tactic

example (P : Prop) (hp : P) : P ∧ True := by
  simp [hp]

example (n : Nat) (h : 0 + n = 3) : n = 3 := by
  simp at h
  exact h
```

`simp only [Nat.zero_add]` は使う補題を指定したものに絞る。`simp [定義名]` はその定義を展開して簡単化する。

`simp at h₁ h₂ ⊢` は、指定した仮定とゴールを簡単化する。`⊢` は ASCII の `|-` でも書ける。`simp at *` はすべての仮定とゴールを対象にする。`at` の後の記号の読み方は [`rw` の対象指定](rw.md)を参照。

`simp [*]` と `simp at *` では、`*` の役割が違う。

| 書き方 | 仮定の使い方 | 簡単化の対象 |
| --- | --- | --- |
| `simp [*]` | ローカルの仮定を簡単化の材料に追加する | ゴール |
| `simp at *` | 通常の簡単化ルールを使う | すべての仮定とゴール |
| `simp [*] at *` | ローカルの仮定を材料に追加する | すべての仮定とゴール |

```lean
import Std.Tactic

example (P Q : Prop) (hp : P) (h : P → Q) : Q ∧ True := by
  simp [*]

example (n : Nat) (h : 0 + n = 3) : n = 3 := by
  simp at *
  exact h
```

一つ目は `hp` と `h` を材料としてゴールを証明する。二つ目は仮定を `h : n = 3` に簡単化するが、その仮定をゴールの簡単化ルールとして追加する指定はないため、残ったゴールを `exact h` で閉じる。

`rw` は指定した書き換えを順に行うが、`simp` は簡単化のルールを繰り返し使う。`simp` が成功しても、ゴールが残ることはある。

`simp!` は条件付き定義などの展開を積極的に行う変種で、`simp?` は使った補題に基づく書き方を提案する。組み合わせた `simp?!` もある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`simp`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.simp)。

[タクティクス一覧に戻る](README.md)
