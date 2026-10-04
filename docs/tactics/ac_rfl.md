# `ac_rfl`

`ac_rfl` は、**結合則と交換則による並べ替えで等しい式を証明する**タクティクスである。

括弧や項の順番だけが違う式に使える。

```lean
example (a b c : Nat) : (a + b) + c = c + (b + a) := by
  ac_rfl
```

ここでは加算の結合則と交換則を使う。一般の多項式を展開したり、分配法則を使ったりするタクティクスではない。

`ac_nf` はそのような式を共通の標準形に並べ替えるために使う。仮定も対象にするなら `ac_nf at h` と書く。`ac_nf0` はこの正規化の基本処理を行う変種である。

```lean
example (a b c : Nat) : (a + b) + c = c + (b + a) := by
  ac_nf
```

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`ac_rfl`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.acRfl)。

[タクティクス一覧に戻る](README.md)
