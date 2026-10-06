# `fail_if_success`

`fail_if_success` は、内側のタクティクスが失敗することを確認するタクティクスである。

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

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`fail_if_success`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.failIfSuccess)。

[タクティクス一覧に戻る](README.md)
