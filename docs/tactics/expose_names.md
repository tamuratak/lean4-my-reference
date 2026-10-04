# `expose_names`

`expose_names` は、**仮定の内部名を、証明から参照できる名前にする**タクティクスである。

名前を付けずに導入した仮定を、後から参照したいときに使う。

```lean
example (P : Prop) : P → P := by
  intro
  expose_names
  assumption
```

生成された名前はエディターの証明状態で確認できる。自分で分かりやすい名前を選びたい場合は `rename_i hp` の方が適している。

`unhygienic` は内側のタクティクスで名前の衛生性の設定を変える関連操作である。通常の証明では `intro hp` や `rename_i` で明示的に名前を付ければ十分である。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
