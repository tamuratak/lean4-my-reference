# 添字アクセスの `xs[i]`・`xs[i]'h`・`xs[i]?`・`xs[i]!`

これらは、**コレクションから添字に対応する要素を取り出す**記法である。範囲内であることの証明を使うか、範囲外を計算で扱うかが異なる。

| 記法 | 範囲の扱い | 配列 `Array α` での結果の型 |
| --- | --- | --- |
| `xs[i]` | 範囲内の証明を自動で補う | `α` |
| `xs[i]'h` | 範囲内の証明 `h` を明示する | `α` |
| `xs[i]?` | 範囲内なら `some`、範囲外なら `none` | `Option α` |
| `xs[i]!` | 範囲内なら要素、範囲外なら実行時にパニック | `α`（`Inhabited α` が必要） |

## 証明を使うアクセス

配列では添字が `0` から始まり、通常は `i < xs.size` を証明する必要がある。

```lean
example : (#[10, 20, 30] : Array Nat)[1] = 20 := rfl
```

この範囲条件は自動で証明される。変数を使う場合などは、アポストロフィの後に証明を渡せる。

```lean
def first (xs : Array Nat) (h : 0 < xs.size) : Nat := xs[0]'h

example : first #[7] (by decide) = 7 := rfl
```

`'h` は添字とは別に、アクセスが有効であることを保証する証明である。自動処理については [get_elem_tactic](../tactics/get_elem_tactic.md) を参照。

## 範囲外も扱うアクセス

`?` を付けると、範囲内であることを呼び出し側で証明せず、結果を `Option` として受け取れる。

```lean
example : (#[10, 20] : Array Nat)[1]? = some 20 := rfl
example : (#[10, 20] : Array Nat)[2]? = none := rfl
```

`!` は、呼び出し側が要素を直接必要とする場合の記法である。

```lean
example : (#[10, 20] : Array Nat)[1]! = 20 := rfl
```

範囲外の `!` は実行時にパニックを起こす。Lean の論理上は既定値を返す定義を持つため、範囲内の証明を得られる操作ではない。範囲外を通常の分岐として扱いたいなら `?` を使う。

添字の型や有効条件はコレクションの `GetElem`・`GetElem?` インスタンスによって決まる。`?`・`!` も、どの関数名にも自由に追加できる一般的な構文ではない。

参照：[公式 API：GetElem と添字アクセス](https://lean-lang.org/doc/api/Init/GetElem.html)、[公式リファレンス：Arrays](https://lean-lang.org/doc/reference/latest/Basic-Types/Arrays/)。

[記号索引に戻る](../symbols.md) · [文法要素の一覧に戻る](README.md)
