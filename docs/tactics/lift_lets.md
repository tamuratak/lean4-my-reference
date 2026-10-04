# `lift_lets`

`lift_lets` は、**式の内部の `let` を、式の外側へ移す**タクティクスである。

関数の引数の中などに埋め込まれた `let` を整理する。

```lean
example (f : Nat → Nat) : f (let n := 3; n) = f 3 := by
  lift_lets
  rfl
```

`lift_lets at h` で仮定を対象にできる。`let` を局所定義として取り出したい場合は `extract_lets` を使う。

この操作は、関数の値を計算するのではなく、定義上同じ意味のまま `let` の配置を整える。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
