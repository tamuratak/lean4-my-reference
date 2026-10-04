# `symm_saturate`

`symm_saturate` は、**仮定にある対称な関係について、逆向きの事実も追加する**タクティクスである。

元の仮定の向きを変える `symm at h` と違い、元の事実も残す。

```lean
example (a b : Nat) (h : a = b) : b = a := by
  symm_saturate
  assumption
```

この例では `b = a` の事実が追加されるので、`assumption` で閉じる。

```lean
example (a b : Nat) (h : a = b) : a = b ∧ b = a := by
  symm_saturate
  constructor <;> assumption
```

同じ関係を両向きに使いたい場合に役立つ。対称性が登録されていない関係には使えない。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`symm_saturate`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.symmSaturate)。

[タクティクス一覧に戻る](README.md)
