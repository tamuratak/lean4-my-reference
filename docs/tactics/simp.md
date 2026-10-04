# `simp`

`simp` は、**登録された等式や同値を使い、式や命題を簡単な形にする**タクティクスである。

例えば自然数の `0 + n` を `n` に簡単化できる。

```lean
example (n : Nat) : 0 + n = n := by
  simp
```

`simp [h]` で手元の事実を追加し、`at h` で仮定を簡単化できる。

```lean
example (P : Prop) (hp : P) : P ∧ True := by
  simp [hp]

example (n : Nat) (h : 0 + n = 3) : n = 3 := by
  simp at h
  exact h
```

`simp only [Nat.zero_add]` は使う補題を指定したものに絞る。`simp [定義名]` はその定義を展開して簡単化する。

`rw` は指定した書き換えを順に行うが、`simp` は簡単化のルールを繰り返し使う。`simp` が成功しても、ゴールが残ることはある。

`simp!` は条件付き定義などの展開を積極的に行う変種で、`simp?` は使った補題に基づく書き方を提案する。組み合わせた `simp?!` もある。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
