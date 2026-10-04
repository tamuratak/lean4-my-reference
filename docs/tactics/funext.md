# `funext`

`funext` は、**関数どうしの等式を、任意の入力での値の等式に変える**タクティクスである。

関数 `f` と `g` が等しいことを示すには、どの入力でも結果が等しいことを示せばよい。

```lean
example (f g : Nat → Nat) (h : ∀ n, f n = g n) : f = g := by
  funext n
  exact h n
```

`funext n` の後は次の状態になる。

```text
n : Nat
⊢ f n = g n
```

引数が複数ある関数なら `funext x y` とまとめて導入できる。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`funext`](https://lean-lang.org/doc/api/Init/NotationExtra.html)。

[タクティクス一覧に戻る](README.md)
