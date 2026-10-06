# `ext`

`ext` は、外延性の定理を使い、値どうしの等式を成分や入力ごとの等式に変えるタクティクスである。

関数では `funext` と同じように、入力を導入できる。

```lean
example (f g : Nat → Nat) (h : ∀ n, f n = g n) : f = g := by
  ext n
  exact h n
```

構造体についても、外延性の定理が登録されていれば各成分の等式に分解できる。

```lean
@[ext] structure Point where
  x : Nat
  y : Nat

example (a b : Point) (hx : a.x = b.x) (hy : a.y = b.y) : a = b := by
  ext
  · exact hx
  · exact hy
```

`ext1` は外延性を一段階だけ適用する。`apply_ext_theorem` はその段階で使う外延性の定理の適用に使う。`ext` は必要に応じてさらに分解するので、分解が進みすぎるときは `ext1` を使う。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`ext`](https://lean-lang.org/doc/api/Init/Ext.html#Lean.Elab.Tactic.Ext.ext)。

[タクティクス一覧に戻る](README.md)
