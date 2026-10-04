# `erw`

`erw` は、**通常の `rw` より定義の展開を許して書き換える**タクティクスである。

型の別名や定義の内部を照合するために、より強い展開が必要なときに使う。

```lean
example (a b : Nat) (h : a = b) : a + 1 = b + 1 := by
  erw [h]
```

基本の構文は `rw` と同じで、`erw [← h]` や `erw [h] at ha` と書ける。

この単純な例では `rw` でも証明できる。`erw` を必要とする証明は、定義の実装に強く依存する場合がある。まず `rw` を試し、照合に必要な展開が足りない場合に使うとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
