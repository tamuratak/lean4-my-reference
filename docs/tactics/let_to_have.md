# `let_to_have`

`let_to_have` は、**値を展開する必要がない `let` を、`have` の形に変える**タクティクスである。

式の中で `let` の値への依存が不要な場合に使う。

```lean
example : (let n : Nat := 3; True) := by
  let_to_have
  trivial
```

`let` は定義上の等しさの判定で値を展開できる。一方 `have` はその値に依存しない形で扱える。`let_to_have` は、その変更が可能な場所を変換する。

局所定義の値を消す `clear_value` と関連しているが、こちらはゴールや仮定の式の中にある `let` を対象にする。仮定なら `let_to_have at h` と指定する。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
