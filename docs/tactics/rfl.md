# `rfl`

`rfl` は、定義に従って計算すると同じになる等式などを証明するタクティクスである。

両辺の見た目が同じでなくても、定義を展開した結果が同じなら使える。

```lean
example (n : Nat) : n = n := by
  rfl

example (n : Nat) : n + 0 = n := by
  rfl
```

Lean の自然数の加算は右の引数について再帰的に定義されているため、`n + 0` は計算すると `n` になる。

一方、`0 + n = n` は任意の `n` について単に計算するだけでは示せず、定理や帰納法を使う。

`eq_refl` は等式の反射性を使い、`apply_rfl` は登録された反射性の定理も利用する。通常は両者などを試す `rfl` から使えばよい。`rfl'` はより強く定義を展開して試す変種である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`rfl`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticRfl)。

[タクティクス一覧に戻る](README.md)
