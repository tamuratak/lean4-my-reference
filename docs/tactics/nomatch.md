# `nomatch`

`nomatch` は、**コンストラクターの形から不可能な値を排除する**タクティクスである。

`Empty` にはコンストラクターがない。したがって、その値 `e` がある場合はどんなゴールも閉じられる。

```lean
example (e : Empty) : False := by
  nomatch e

example (n : Nat) (h : Nat.succ n = 0) : False := by
  nomatch h
```

二つ目では、異なる自然数のコンストラクターが等しいという等式に、可能なケースがないことを使う。

`nofun` は、不可能な引数を受け取る関数を作るための関連した書き方である。

```lean
example : Empty → Nat := by
  nofun
```

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
