# `symm`

`symm` は、**等式など、対称な関係の向きを反転する**タクティクスである。

ゴールが `a = b` のとき、`symm` で `b = a` に変えられる。

```lean
example (a b : Nat) (h : b = a) : a = b := by
  symm
  exact h
```

`at h` を付けると、仮定の向きを反転する。

```lean
example (a b : Nat) (h : a = b) : b = a := by
  symm at h
  exact h
```

`≤` のように対称でない関係を逆にすることはできない。`symm_saturate` は仮定にある対称な関係の逆向きの事実を追加するための関連タクティクスである。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
