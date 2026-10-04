# `delta`

`delta` は、**指定した定数を、その定義本体に置き換える**タクティクスである。

定義を直接開く操作である。

```lean
def twice (n : Nat) : Nat := n + n

example (n : Nat) : twice n = n + n := by
  delta twice
  rfl
```

`delta twice at h` で仮定の中を展開できる。

`unfold` は定義に対応する等式を利用するが、`delta` は定数の定義本体を直接展開する。再帰関数の内部表現まで開くと式が読みにくくなることがあるので、通常の証明では先に `unfold` や `simp [定義名]` を使うとよい。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
