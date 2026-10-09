# Aesop の規則の追加・登録と種類

Aesop の探索に補題を使わせたいときは、その呼び出しだけで規則を追加する `add`、または宣言を登録する `@[aesop ...]` を使う。

```lean
import Aesop

example (α : Type) (P Q : α → Prop) (step : ∀ x, P x → Q x)
    (a : α) (ha : P a) : Q a := by
  aesop (add safe apply step)
```

`apply step` に対応する規則は、ゴール `Q a` を `P a` に変える。残るゴールを仮定 `ha` で閉じられる。この追加は、その `aesop` 呼び出しだけに作用する。

同じ補題を繰り返し使わせたい場合は、属性で登録できる。

```lean
import Aesop

@[aesop unsafe 50% apply]
theorem pairSwap (P Q : Prop) : P ∧ Q → Q ∧ P := by
  rintro ⟨hp, hq⟩
  exact ⟨hq, hp⟩

example (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
  aesop
```

属性は後続の探索に規則を登録する。`apply` は補題の結論をゴールに合わせ、その前提を新しいゴールにする規則の作り方である。論理積の交換は Aesop の組み込み規則でも解けるが、この例では補題の登録構文も示している。

規則の種類は次のように使い分ける。

| 種類 | 探索での扱い | 選ぶ目安 |
| --- | --- | --- |
| `norm` | 探索前に状態を整理する | 簡単化や不要な構造の除去 |
| `safe` | 適用後、元の状態へ戻って別の規則を試さない | 適用しても証明できる可能性を失わない操作 |
| `unsafe` | 他の候補も試す探索の分岐になる | 証明方針の選択が必要な操作 |

`unsafe 50%` の割合は、探索の優先順位を決めるための重みである。実測の成功確率や、証明の信頼性を表す数ではない。`unsafe` という名前でも、完成した証明は通常の Lean の証明として検査される。

`safe` を単に「よく使う補題」という意味で指定すると、必要な別の証明方針を試せなくなる場合がある。補題の適用が選択を含むなら、まず `unsafe` を検討する。規則を増やしすぎると探索量も増えるため、狭い用途なら `add` から始めるとよい。

参照：[Lean 公式リファレンス：属性](https://lean-lang.org/doc/reference/latest/Attributes/)（属性一般の説明）。

[Aesop タクティクス一覧に戻る](README.md)
