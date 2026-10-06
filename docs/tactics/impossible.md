# `impossible`

`impossible` は、現在のゴールが一般には証明できないことを、反例によって確認するタクティクスである。

これは証明を完成させるためではなく、誤った主張を調べるための操作である。

例えば「すべての自然数がゼロである」という主張に対して、`1` を反例にできる。

```lean-incomplete
example (n : Nat) : n = 0 := by
  impossible by
    intro h
    have bad : (1 : Nat) = 0 := h 1
    contradiction
```

内側では、元の局所変数を全称量化した主張の否定を証明する。この例なら `¬ (∀ n : Nat, n = 0)` を示す。

元のゴールは `sorry` と同様に閉じられるため、上のコードは完成した証明ではない。このページの例は、完成した証明の自動検証から除外している。

矛盾した仮定から正しいゴールを閉じる `contradiction` や `nomatch` とは用途が異なる。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`impossible`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.impossible)。

[タクティクス一覧に戻る](README.md)
