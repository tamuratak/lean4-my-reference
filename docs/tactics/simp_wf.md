# `simp_wf`

`simp_wf` は、**整礎再帰の停止性のゴールを簡単化する**タクティクスである。

Lean が構造的な再帰と判断できない定義では、再帰呼出しで測度が小さくなることを示す必要がある。

```lean
def down (n : Nat) : Nat :=
  if h : n = 0 then 0 else down (n - 1)
termination_by n
decreasing_by
  simp_wf
  omega
```

`decreasing_by` の中で `simp_wf` により停止性に使う関係の表現を簡単化し、その後の `omega` で減少を示す。

`simp_wf` だけでどんな停止性でも証明できるわけではない。測度を明示するのが `termination_by`、減少の証明を書くのが `decreasing_by` である。

`decreasing_trivial` などは、Lean が停止性を自動で証明するときに使う関連タクティクスである。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
