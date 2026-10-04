# `Prop`・`Type`・`Sort`・`universe`

`Prop` は、**命題が属する型**である。`P : Prop` が命題で、`h : P` がその証明になる。

```lean
example (P : Prop) (h : P) : P := h

#check (3 = 3)
#check (rfl : 3 = 3)
```

`3 = 3` の型は `Prop`、`rfl` の型はその命題 `3 = 3` である。命題と証明は、同じものではない。

`Type` は、自然数などのデータ型が属する型である。

```lean
#check Nat
#check (3 : Nat)
#check Type
```

`Nat : Type`、`3 : Nat` と読む。さらに `Type` 自身の型は `Type 1` であり、型には階層がある。

```text
Prop   = Sort 0
Type   = Type 0 = Sort 1
Type 1 = Sort 2
```

ここでの `=` は表記の対応を示す説明である。`Sort` は、命題の階層とデータ型の階層を共通の記法で表す。

`universe u` を使うと、特定の階層に限定しない定義を書ける。

```lean
universe u

def keep {α : Type u} (x : α) : α := x

example : keep (3 : Nat) = 3 := rfl
example : keep Nat = Nat := rfl
```

`Nat` の値だけでなく、型である `Nat` 自体も渡せる。`{α : Type}` と書いた場合は `α` が `Type 0` に限定されるので、型を値として渡すこの二つ目の用途には足りない。

参照：[公式リファレンス：The Type System](https://lean-lang.org/doc/reference/latest/The-Type-System/)。

[文法要素の一覧に戻る](README.md)
