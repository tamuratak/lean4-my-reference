# 式の `have`

`have h : P := 証明; 後続の式` は、**補助的な証明に名前を付け、それを後続の式で使う**構文である。`by` の外でも書ける。

```lean
example (P Q : Prop) (hp : P) (f : P → Q) : Q ∧ P :=
  have hq : Q := f hp
  ⟨hq, hp⟩
```

`f hp` から `Q` の証明を作り、`hq` と呼ぶ。続く `⟨hq, hp⟩` が全体の証明になる。

```text
hp : P
hq : Q
```

これは後続の式で使える名前と型の説明である。式の `have` は、タクティクスのようにゴールを操作する命令を並べる書き方ではない。

名前を省略すると `this` になる。

```lean
example (P Q : Prop) (hp : P) (f : P → Q) : Q :=
  have : Q := f hp
  this
```

`have` は命題以外の値にも使えるが、[`let`](let.md) と計算上の扱いが違う。`let` は名前を本体へ展開できる局所定義を作り、`have` の後続の式では、その値の具体的な本体に頼らず型から使う。

```lean
example : (let n : Nat := 3; n = 3) := rfl
```

この例の `n = 3` は `let` の値を展開することで証明できる。同様に `have n : Nat := 3; (rfl : n = 3)` としても、後続の式の確認時に `n` を `3` へ展開できない。

証明状態に仮定を追加する説明は、[タクティクスの `have`](../tactics/have.md)を参照。

参照：[公式 API ドキュメント：式の `have`](https://lean-lang.org/doc/api/Lean/Parser/Term.html#Lean.Parser.Term.have)。

[文法要素の一覧に戻る](README.md)
