# `theorem`・`example`

`theorem` は、**命題の証明に名前を付け、後で使える定理として登録する**構文である。

```text
theorem 名前 (引数 : 型) : 命題 := 証明
```

命題は `Prop` 型の値で、その命題を型として持つ項が証明になる。`h : P` は「命題 `P` の証明を `h` と呼ぶ」という意味である。

```lean
theorem keepProof (P : Prop) (h : P) : P := h

example (Q : Prop) (hq : Q) : Q := keepProof Q hq
```

ここでは `h` 自体が必要な証明なので、`:= h` で定理を完成できる。登録した `keepProof` は、関数と同じように引数を渡して使う。

`example` は、**名前を登録せず、証明や定義が正しいか確認する**。短い練習や動作確認に向いている。

```lean
example (n : Nat) : n = n := rfl

example : Nat := 3
```

最初は証明、次は値の確認である。`example` の結果を、後から定理名で呼び出すことはできない。

証明をタクティクスで書くときは [`by`](by.md) を使う。

```lean
theorem swapAnd (P Q : Prop) (h : P ∧ Q) : Q ∧ P := by
  exact ⟨h.2, h.1⟩
```

`theorem` と [`def`](def.md) はどちらも名前を登録するが、`theorem` の結果は命題であり、証明の本体は定義上の等しさを判定する計算では展開されない。

参照：[公式リファレンス：Theorems](https://lean-lang.org/doc/reference/latest/Definitions/Theorems/)。

[文法要素の一覧に戻る](README.md)
