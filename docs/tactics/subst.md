# `subst`

`subst` は、等式で結ばれた変数を置き換え、不要になった変数と等式を取り除くタクティクスである。

`h : a = b` のもとで `subst a` と書くと、`a` を `b` に置き換える。

```lean
example (P : Nat → Prop) (a b : Nat) (h : a = b) (ha : P a) : P b := by
  subst a
  exact ha
```

ここでは `ha` も `P b` に変わる。`rw` は指定した場所を書き換えるのに対し、`subst` は変数を証明全体から消すために使う。

`subst h` のように等式の名前を指定することもできる。`subst_vars` は置換可能な変数をまとめて置換し、`subst_eqs` も仮定にある等式による置換をまとめて試す。

```lean
example (a b c : Nat) (h₁ : a = b) (h₂ : b = c) : a = c := by
  subst_vars
  rfl
```

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`subst`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.subst)。

[タクティクス一覧に戻る](README.md)
