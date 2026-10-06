# `private`・`protected`

`private` と `protected` は、宣言した名前の使える範囲や、名前空間を開いたときの扱いを指定する修飾子である。

`private` は、そのモジュールの外から元の名前で使えない宣言を作る。

```lean
namespace Arithmetic

private def double (n : Nat) : Nat := n + n

def four : Nat := double 2

end Arithmetic

example : Arithmetic.four = 4 := rfl
example : Arithmetic.double 3 = 6 := rfl
```

この例は一つのファイルなので、非公開の `Arithmetic.double` も参照できる。別のモジュールがこのファイルを読み込んだ場合、`Arithmetic.four` は使えるが、非公開の補助定義を `Arithmetic.double` という名前では呼べない。

`protected` は公開を禁止するのではなく、通常の `open` で短い名前を使えるようにする対象から外す。

```lean
namespace Counter

protected def advance (n : Nat) : Nat := n + 1

end Counter

open Counter
example : Counter.advance 3 = 4 := rfl
```

`open Counter` の後も、`advance` という短い名前はこの宣言を指さない。`Counter.advance` と明示すれば使える。

特定の名前を指定して開く場合は、`protected` の宣言も短く使える。

```lean
namespace Counter

protected def advance (n : Nat) : Nat := n + 1

end Counter

open Counter (advance) in
example : advance 3 = 4 := rfl
```

`namespace` は名前を整理するだけなので、それだけでは非公開にならない。`private` はモジュールの境界、`protected` は名前空間を開くときの振る舞いに関する指定である。

参照：[公式リファレンス：Modifiers](https://lean-lang.org/doc/reference/latest/Definitions/Modifiers/)、[公式リファレンス：Namespaces and Sections](https://lean-lang.org/doc/reference/latest/Namespaces-and-Sections/)。

[文法要素の一覧に戻る](README.md)
