# `fail_if_success`

`fail_if_success` は、**内側のタクティクスが失敗することを確認する**タクティクスである。

内側が成功したら失敗し、内側が失敗したら成功する。いずれの場合も内側で試した証明状態は引き継がない。

```lean
example (P : Prop) (hp : P) : P := by
  fail_if_success rfl
  exact hp
```

これは証明を進めるためというより、タクティクスの挙動を調べる用途に向いている。

`fail` は明示的に失敗する操作で、`fail "message"` と理由を付けられる。

```lean
example (P : Prop) (hp : P) : P := by
  first
  | fail "Try the next branch"
  | exact hp
```

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
