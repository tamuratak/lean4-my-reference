# `solve`

`solve` は、**候補を順番に試し、対象のゴールをすべて閉じるものを採用する**タクティクスである。

`first` と違い、ゴールが残る候補は採用しない。

```lean
example (P : Prop) (hp : P) : P := by
  solve
  | skip
  | exact hp
```

最初の `skip` は操作として成功するが、ゴールを閉じないので次の候補へ進む。

候補を一つだけにして、処理が確実に証明を完了したことを確認する用途にも使える。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
