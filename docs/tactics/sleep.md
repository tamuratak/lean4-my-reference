# `sleep`

`sleep` は、**指定したミリ秒だけ待ち、証明状態を変えずに進む**タクティクスである。

エディターやタクティクス実行の挙動を調べるための操作である。

```lean
example : True := by
  sleep 1
  trivial
```

`1` は 1 ミリ秒を表す。待つことで命題を証明できるわけではないため、普通の証明では必要ない。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
