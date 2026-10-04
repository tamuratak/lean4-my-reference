# コメント・字下げ

`--` は、**その位置から行末までをコメントにする**。`/- … -/` は複数行にも使えるブロックコメントで、入れ子にできる。

```lean
-- Double a natural number.
def double (n : Nat) : Nat := n + n

/- A block comment.
   /- A nested comment. -/
-/
example : double 3 = 6 := rfl
```

コメントは式の値や証明の内容には影響しない。

`/-- … -/` は、直後の宣言に説明を付けるドキュメントコメントである。

```lean
/-- Add one to a natural number. -/
def addOne (n : Nat) : Nat := n + 1
```

エディタで宣言の説明として表示するなどの用途に使われる。`/-! … -/` はモジュールの説明や、ファイル内の文章の区切りとして使うドキュメントコメントである。

Lean の字下げは、複数行の式やタクティクスの範囲を示す。単なる見た目の調整ではない。

```lean
def choose (b : Bool) : Nat :=
  if b then
    1
  else
    2

example : choose true = 1 := by
  rfl
```

定義の本体は宣言より深く、分岐の中身は `if` より深く、タクティクスは `by` より深く置く。このリファレンスでは通常、段階ごとに二つの空白を使う。

一行にまとめる場合と複数行に分ける場合では、`;` や括弧が必要になることもある。例をコピーするときは改行と字下げも含めてコピーする。

参照：[公式リファレンス：Source Files and Modules](https://lean-lang.org/doc/reference/latest/Source-Files-and-Modules/)。

[文法要素の一覧に戻る](README.md)
