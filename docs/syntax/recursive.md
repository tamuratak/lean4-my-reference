# パターンによる関数定義・再帰

`def` の型の後に `| パターン => 本体` を並べると、入力の形ごとに関数の結果を定義することができる。

```lean
def predecessor : Nat → Nat
  | 0 => 0
  | n + 1 => n

example : predecessor 0 = 0 := rfl
example : predecessor 5 = 4 := rfl
```

`n + 1` は、自然数の後者 `Nat.succ n` に対応するパターンである。この形式では、引数に名前を付けて `:= match …` と書く代わりに、分岐を直接並べる。

分岐の中で定義中の関数自身を呼ぶと、再帰的な関数になる。

```lean
def listLength {α : Type} : List α → Nat
  | [] => 0
  | _ :: rest => listLength rest + 1

example : listLength [2, 4, 6] = 3 := rfl
```

再帰呼び出しの入力 `rest` は、元のリストの一部である。Lean はこのように構造が小さくなる再帰を確認し、停止する関数として受け入れる。

停止の理由を明示する `termination_by` を書くこともできる。

```lean
def countDown (n : Nat) : Nat :=
  match n with
  | 0 => 0
  | k + 1 => countDown k + 1
termination_by n

example : countDown 4 = 4 := by
  simp [countDown]
```

`termination_by n` は、再帰で自然数 `n` が小さくなることを停止の基準にする。この例の減少条件は Lean が自動で証明できる。

この指定による定義は整礎再帰として扱われる。前の構造的な再帰の例と違い、具体的な入力の等式でも `rfl` だけで示せるとは限らない。この例では `simp [countDown]` で定義の等式を使って計算する。

`termination_by` は、停止条件を無視してよいという指定ではない。自動で証明できない減少条件には `decreasing_by` で証明を与える必要がある。

式の中の補助関数は [`let rec`](let_rec.md)、定義の後に添える補助関数は [`where`](where.md)、互いを呼び出す複数の関数は [`mutual`](mutual.md) を参照。

参照：[公式リファレンス：Recursive Definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/)。

[文法要素の一覧に戻る](README.md)
