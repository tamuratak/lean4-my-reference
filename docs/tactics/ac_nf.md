# `ac_nf`

`ac_nf` は、**結合則と交換則を使って、式を共通の標準形に並べ替える**タクティクスである。

項の順序や括弧が異なる式を、同じ形に揃える。

```lean
import Std.Tactic

example (a b c : Nat) : (a + b) + c = c + (b + a) := by
  ac_nf
```

仮定も対象にできる。

```lean
import Std.Tactic

example (a b c : Nat) (h : a + b = c) : b + a = c := by
  ac_nf at *
```

[`ac_rfl`](ac_rfl.md) はそのような等式を証明するために使い、`ac_nf` は式の正規化にも使う。分配法則による多項式の展開には `grobner` などを使う。

`ac_nf` は正規化の後、`trivial` によるゴールの解決を試す。仮定も正規化した結果、その仮定でゴールを閉じられる場合もある。二つ目の例では追加の `assumption` は不要である。

## `ac_nf0`：後処理を省いて正規化する

`ac_nf0` は `ac_nf` と同じ正規化を行うが、最後の `trivial` を行わない。

```lean
import Std.Tactic

example (a b c : Nat) : (a + b) + c = c + (b + a) := by
  ac_nf0
  rfl
```

この例では `ac_nf0` の後に、両辺が同じ標準形になった等式が残る。それを `rfl` で閉じる。`ac_nf` なら最後の `trivial` がこの等式を証明する。

参照：[公式 API：`ac_nf`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticAc_nf_)、[公式 API：`ac_nf0`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.acNf0)。

[タクティクス一覧に戻る](README.md)
