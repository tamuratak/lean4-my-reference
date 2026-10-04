# `simpa`

`simpa` は、**ゴールと渡した証明の型を簡単化し、それらを合わせて証明を閉じる**タクティクスである。

`h : n = m` を使って `0 + n = m` を証明したい場合、左辺を簡単化すれば `h` と合う。

```lean
example (n m : Nat) (h : n = m) : 0 + n = m := by
  simpa using h
```

使う補題を絞ることもできる。

```lean
example (n m : Nat) (h : n = m) : 0 + n = m := by
  simpa only [Nat.zero_add] using h
```

`using h` を省略した `simpa` は、ゴールの簡単化などで証明を完了しようとする。`simp` はゴールが残っても成功できるが、`simpa` は証明を閉じるために使う。

`simpa!`、`simpa?`、`simpa?!` は、それぞれ展開や提案を伴う変種である。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
