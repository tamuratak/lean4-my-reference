# `convert`

`convert e` は、証明 `e` の型をゴールに合わせ、食い違っている式の等しさを新しいゴールとして残すタクティクスである。定義上は同じでないため `exact e` が使えない場合に役立つ。

```lean
import Mathlib.Tactic.Convert

example (P : Nat → Prop) (n : Nat) (h : P (n + 1)) : P (1 + n) := by
  convert h using 1
  exact Nat.add_comm 1 n
```

`using 1` は、一致を調べるために式を分解する深さを指定する。この例では次の等式が残る。

```text
⊢ 1 + n = n + 1
```

渡した証明の結論と、いま証明したい結論をつなぐ等式である。

```lean
import Mathlib.Tactic.Convert
import Mathlib.Tactic.Ring

example (P : Int → Prop) (x : Int) (h : P (2*x)) : P (x + x) := by
  convert h using 1
  ring
```

簡単化で型を合わせられる場合は Lean 本体の [simpa](../../tactics/simpa.md) が短い。`convert` は、合わせるための等式を自分で証明したい場合に使う。`convert ← e` は残る等式の向きを逆にする。

参照：[Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)（Lean 本体との比較用）。

[mathlib タクティクス一覧に戻る](README.md)
