# `@[simp]`：簡単化の規則に登録する

`@[simp]` は、**定理や定義を、通常の `simp` が使う簡単化の規則に登録する**属性である。後に書く証明の `simp` でも、登録された規則が使われる。

```lean
def wrap (n : Nat) : Nat := n

@[simp] theorem wrap_eq (n : Nat) : wrap n = n := rfl

example (n : Nat) : wrap (wrap n) = n := by
  simp
```

規則 `wrap n = n` が内側と外側の `wrap` に使われ、ゴールは `n = n` に簡単化されて閉じる。登録がなければ、この定理を `simp [wrap_eq]` のように明示する方法がある。

## 定義に付ける

```lean
@[simp] def twice (n : Nat) : Nat := n + n

example (n : Nat) : twice n = n + n := by
  simp
```

定義に付けると、その定義を簡単化するときに展開するための規則が登録される。この例では `twice n` が `n + n` に置き換わる。

## `simp`・`simp [h]` との違い

| 書き方 | 役割 |
| --- | --- |
| `@[simp] theorem h ...` | 後の簡単化でも使う規則として登録する |
| `simp` | 登録済みの規則などを使い、今のゴールを簡単化する |
| `simp [h]` | 今回の簡単化に `h` も追加する |
| `simp only [h]` | 通常の登録済み規則を使わず、指定した規則で簡単化する |
| `simp [-h]` | 今回の簡単化から `h` を除く |

`simp only` でも、基本的な計算による簡約は行われる。

どんな等式でも登録すればよいわけではない。`wrap n = n` のように、一定の形へ整理する規則が向いている。交換則のような規則は並べ替えとして特別に扱われることがあり、書いた向きのまま使われるとは限らない。

一つの証明だけで必要なら `simp [h]`、一つのセクションだけで必要なら `attribute [local simp] h` を使うと、他の証明への影響を抑えられる。タクティクスの詳しい使い方は [`simp`](../tactics/simp.md)を参照。

参照：[公式リファレンス：Simp Normal Forms](https://lean-lang.org/doc/reference/latest/The-Simplifier/Simp-Normal-Forms/)、[Invoking the Simplifier](https://lean-lang.org/doc/reference/latest/The-Simplifier/Invoking-the-Simplifier/)。

[属性の一覧に戻る](README.md)
