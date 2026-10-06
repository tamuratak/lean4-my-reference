# `clear`

`clear` は、この先で不要な局所変数や仮定を取り除くタクティクスである。

証明に関係のない仮定を消すと、状態を読みやすくできる。

```lean
example (P Q : Prop) (hp : P) (hq : Q) : P := by
  clear hq
  exact hp
```

ただし、ゴールや他の仮定が依存しているものは消せない。例えば `n = 0` を証明中に、その式に現れている `n` を `clear n` で消すことはできない。

複数まとめて消すなら `clear h₁ h₂` と書く。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/The-Tactic-Language/)、[公式 API ドキュメント：`clear`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.clear)。

[タクティクス一覧に戻る](README.md)
