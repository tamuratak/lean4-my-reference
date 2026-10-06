# `lia`

`lia` は、`grind` の整数線形算術の機能に絞って証明するタクティクスである。

整数の不等式を組み合わせる例である。

```lean
example (x y : Int) (h : x ≤ y) : x + 2 ≤ y + 3 := by
  lia
```

`lia` は `grind` の線形整数算術ソルバーを使う。論理的な仮定や関数の等式なども広く利用したい場合は `grind` を選ぶ。

`cutsat` は同種の機能の古い名前で、このバージョンでは非推奨である。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`lia`](https://lean-lang.org/doc/api/Init/Grind/Tactics.html#Lean.Parser.Tactic.lia)。

[タクティクス一覧に戻る](README.md)
