# `Array α`：配列

`Array α` は、**`α` 型の要素を順序付きで保持し、添字で取り出す配列の型**である。長さは型に含まれず、空の配列も作れる。追加の `import` は不要である。

## 値と要素数

```lean
def values : Array Nat := #[10, 20, 30]
def empty : Array Nat := #[]

example : values.size = 3 := rfl
example : empty.size = 0 := rfl
```

`#[…]` は配列、`[…]` はリストの記法である。要素数は `.size` で取り出す。空の場合は、必要なら `(#[] : Array Nat)` のように要素型を指定する。

## 添字で取り出す

```lean
example : (#[10, 20] : Array Nat)[0] = 10 := rfl
example : (#[10, 20] : Array Nat)[1]? = some 20 := rfl
example : (#[10, 20] : Array Nat)[2]? = none := rfl

def readAt (xs : Array Nat) (i : Nat) (h : i < xs.size) : Nat :=
  xs[i]'h
```

添字は０から始まる。`xs[i]` は範囲内であることの証明を必要とし、単純な場合は Lean が補う。`xs[i]'h` は証明を明示して渡す。`xs[i]?` は証明を要求せず、範囲内なら `some`、範囲外なら `none` を返す。詳細は[添字アクセス](../syntax/indexing.md)を参照。

## 追加と変換

```lean
example : (#[1, 2] : Array Nat).push 3 = #[1, 2, 3] := rfl
#eval (#[1, 2] : Array Nat).map (fun n => n + 1)
example : (#[1, 2] : Array Nat).toList = [1, 2] := rfl
example : ([1, 2] : List Nat).toArray = #[1, 2] := rfl
```

`.push` は末尾に要素を加えた配列、`.map` は各要素を変換した配列を返す。上の `#eval` の出力は `#[2, 3]` になる。元の変数の値を代入によって変更する記法ではない。リストとの変換には `.toList`・`.toArray` を使う。

[`List`](list.md) は先頭と残りに分解する処理に向いている。配列は実行時に添字アクセスを効率よく行うための表現を使う。基本操作を選ぶ際は、この構造の違いと、`.length`・`.size` などの操作名の違いに注意する。

参照：[公式リファレンス：Arrays](https://lean-lang.org/doc/reference/latest/Basic-Types/Arrays/)。

[基本データ型の一覧に戻る](README.md)
