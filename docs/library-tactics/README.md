# 追加ライブラリのタクティクス

- [mathlib のタクティクス](mathlib/README.md)：数値計算、多項式、不等式、論理、式変形、有限な場合分け。
- [Aesop のタクティクス](aesop/README.md)：論理の操作や補題の適用を組み合わせる証明探索と、探索規則の追加。

## 証明の目的別のタクティクス候補

| やりたいこと | 提供元と候補 |
| --- | --- |
| 数値だけの等式・不等式を計算する | mathlib：[norm_num](mathlib/norm_num.md) |
| 多項式の等式を展開・整理して証明する | mathlib：[ring](mathlib/ring.md) |
| 仮定やゴールの多項式を標準形にする | mathlib：[ring_nf](mathlib/ring_nf.md) |
| 線形な等式・不等式を組み合わせる | mathlib：[linarith](mathlib/linarith.md) |
| 平方や積も利用して不等式を証明する | mathlib：[nlinarith](mathlib/nlinarith.md) |
| 式が正・非負・非零であることを示す | mathlib：[positivity](mathlib/positivity.md) |
| 分母を払ってから等式を証明する | mathlib：[field_simp](mathlib/field_simp.md) |
| 論理構造を自動で分解して証明する | mathlib：[tauto](mathlib/tauto.md)、Aesop：[aesop](aesop/aesop.md) |
| 補題を登録して探索に使わせる | Aesop：[規則の追加](aesop/rules.md) |

- [Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)
- [Lean 公式 API ドキュメント](https://lean-lang.org/doc/api/)

[リファレンスの入口に戻る](../../README.md)
