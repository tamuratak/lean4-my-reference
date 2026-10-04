# 非アクセス可能パターン `.(式)`

`.(式)` は、**他のパターンや型から値が決まる部分を指定する**パターンである。英語では inaccessible pattern と呼ぶ。型の整合性を確認するために使い、その部分を調べて実行時の分岐を選ぶものではない。

例えば、自然数 `n` を型の添字に持つ値を考える。

```lean
inductive Tagged : Nat → Type where
  | mk (n : Nat) : Tagged n

def tagValue : (n : Nat) → Tagged n → Nat
  | .(n), .mk n => n

example : tagValue 3 (.mk 3) = 3 := rfl
```

`.mk n` が `Tagged n` 型の値を分解すると、最初の引数も同じ `n` でなければならない。そこで最初の引数を `.(n)` と書く。この部分は独立に場合分けする対象ではない。

`.mk` のドットは[期待される型から名前を補う記法](identifiers.md)であり、`.(n)` のドットとは役割が異なる。

通常のパターンでは、変数で値を受け取るか、コンストラクターで値の形を調べる。

```lean
def isZero : Nat → Bool
  | 0 => true
  | _ => false

example : isZero 0 = true := rfl
example : isZero 3 = false := rfl
```

この `0` は実際に分岐を選ぶパターンである。`.(式)` は「任意の式と比較して分岐する」ための記法ではなく、すでに型などから決まっている部分を記す。最初は通常の [match](match.md) を理解し、型の添字がある場合にこの記法を参照するとよい。

参照：[公式リファレンス：Pattern Matching](https://lean-lang.org/doc/reference/latest/Terms/Pattern-Matching/)。

[記号索引に戻る](../symbols.md) · [文法要素の一覧に戻る](README.md)
