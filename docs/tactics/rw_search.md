# `rw?`

`rw?` は、**ゴールや仮定を書き換えられる補題を探して提案する**タクティクスである。

等式の向きや定理名を思い出せないときに使える。

```lean
example (n : Nat) : 0 + n = n := by
  rw?
```

`rw? at h` で仮定を書き換える候補も探せる。候補が見つかっても常に証明が完了するわけではないので、残ったゴールを確認する。

提案された `rw [Nat.zero_add]` などを採用すると、書き換えの根拠を明示できる。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
