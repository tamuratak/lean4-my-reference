# `Vector α n`：長さが型に含まれる配列

`Vector α n` は、**要素の型が `α`、長さがちょうど `n` の配列**である。長さを型に含めることで、決まった個数の要素を要求できる。標準の `import Init.Data.Vector` を使う。

## 決まった長さで作る

```lean
import Init.Data.Vector

def triple : Vector Nat 3 := #v[10, 20, 30]

example : triple.toArray = #[10, 20, 30] := rfl
example : triple.toList = [10, 20, 30] := rfl
example : triple.toArray.size = 3 := triple.size_toArray
```

`#v[…]` は `Vector` の記法である。内部の配列を `.toArray`、リストを `.toList` で取り出せる。`.size_toArray` は、内部の配列の長さが型に指定した `n` と等しいという証明である。

`Array Nat` は任意の長さを保持するが、`Vector Nat 3` は３要素を要求する。`#v[10, 20]` を `Vector Nat 3` として渡すことはできない。

## `Fin n` で要素を取り出す

```lean
import Init.Data.Vector

def readAt {n : Nat} (xs : Vector Nat n) (i : Fin n) : Nat := xs.get i

example : readAt #v[10, 20, 30] ⟨1, by decide⟩ = 20 := rfl
```

`.get` は [`Fin n`](fin.md) の添字を受け取るため、範囲内であることが添字の型に含まれる。添字は０から数えるので、`1` は２番目の要素を指す。

## 配列から作る

```lean
import Init.Data.Vector

def pair : Vector Nat 2 := (#[10, 20] : Array Nat).toVector

def wrap (xs : Array Nat) (h : xs.size = 3) : Vector Nat 3 := ⟨xs, h⟩

example : pair.toList = [10, 20] := rfl
example : (wrap #[10, 20, 30] rfl).toArray = #[10, 20, 30] := rfl
```

配列 `xs` の `.toVector` は `Vector α xs.size` を返す。指定した長さの型として包む場合は、`⟨xs, h⟩` で長さの等式の証明も渡す。

数学のベクトル空間そのものを定義する型ではなく、ここでは長さ付きのデータ列を表す。[`Array`](array.md)と[依存ペア型](../syntax/sigma.md)も参照。

参照：[公式 API：Vector](https://lean-lang.org/doc/api/Init/Data/Vector/Basic.html#Vector)。

[基本データ型の一覧に戻る](README.md)
