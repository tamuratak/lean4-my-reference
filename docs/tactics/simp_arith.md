# `simp_arith`

`simp_arith` は、算術の簡単化を有効にして、`simp` を行うタクティクスである。

`simp_arith` は Lean 4.35.0-rc3 では非推奨で、エラーになる。通常は `simp +arith` に置き換える。例えば自然数の足し算に関する簡単な式を整理できる。

```lean
example (n : Nat) : n + 1 > n := by
  simp +arith
```

以前は `simp +arith +decide` の略だったが、多くの場合に `+decide` が不要になったため、上の書き方が推奨される。

`simp_arith!`、`simp_all_arith`、`simp_all_arith!` も同様の旧式の名前である。仮定も組み合わせるなら `simp_all +arith`、積極的な展開もするなら `simp! +arith` や `simp_all! +arith` を使う。複数の不等式を使う一般的な線形算術では、`omega` や `grind` が適することもある。

参照：[公式リファレンスマニュアル](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)、[公式 API ドキュメント：`simp_arith`](https://lean-lang.org/doc/api/Init/Meta.html#Lean.Parser.Tactic.simpArith)。

[タクティクス一覧に戻る](README.md)
