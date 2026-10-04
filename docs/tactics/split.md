# `split`

`split` は、**`if` や `match` を含む式を、その分岐に沿って場合分けする**タクティクスである。

ゴールにある `if` を分けると、各場合に条件またはその否定が仮定に加わる。

```lean
example (P : Prop) [Decidable P] : (if P then 1 else 2 : Nat) ≤ 2 := by
  split
  · decide
  · decide
```

仮定に含まれる分岐なら `split at h` と指定できる。

```lean
example (P : Prop) [Decidable P]
    (h : (if P then 1 else 2 : Nat) = 1) : P := by
  split at h
  · assumption
  · contradiction
```

`by_cases` では命題を自分で選ぶが、`split` では式に書かれている分岐を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`split`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.split)。

[タクティクス一覧に戻る](README.md)
