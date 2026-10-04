# `contradiction`

`contradiction` は、**仮定の中にある明らかな矛盾を見つけて、ゴールを閉じる**タクティクスである。

例えば `hp : P` と `hnp : ¬ P` が揃っていれば、矛盾からゴールを証明できる。

```lean
example (P Q : Prop) (hp : P) (hnp : ¬ P) : Q := by
  contradiction

example (Q : Prop) (h : False) : Q := by
  contradiction
```

異なるコンストラクターの等式なども扱える。

```lean
example (n : Nat) (h : Nat.succ n = 0) : False := by
  contradiction
```

一般的な算術の矛盾をすべて解くわけではない。`n < n` のような算術的な条件では `omega` などを使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`contradiction`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.contradiction)。

[タクティクス一覧に戻る](README.md)
