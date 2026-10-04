# 真偽値の `==`・`!=`・`!`・`&&`・`||`

これらは、**`Bool` の `true`・`false` を計算する演算子**である。命題を表す `=`・`≠`・`¬`・`∧`・`∨` と区別する。

## 比較の `==` と `!=`

`a == b` は、型に登録された `BEq` の比較を使い、真偽値を返す。`a != b` はその比較結果を反転する。

```lean
#check ((3 : Nat) == 3)
#check ((3 : Nat) = 3)

example : ((3 : Nat) == 3) = true := rfl
example : ((3 : Nat) != 4) = true := rfl
```

最初の式の型は `Bool`、次の式の型は `Prop` である。`a = b` は等しさという命題であり、`a == b` は比較の計算である。

任意の型の `BEq` が数学的な等しさと一致するとは限らない。その対応が保証される型では比較結果を等式の証明に結び付けられるが、一般に `==` を `=` と同一視してはいけない。

## 真偽値を組み合わせる `!`・`&&`・`||`

| 記法 | 計算 | 命題側の対応する記号 |
| --- | --- | --- |
| `!b` | 真偽値を反転する | `¬ P` |
| `a && b` | 両方が真なら真 | `P ∧ Q` |
| `a \|\| b` | どちらかが真なら真 | `P ∨ Q` |

```lean
example : (!true) = false := rfl
example : (true && false) = false := rfl
example : (false || true) = true := rfl
```

`&&` と `||` は短絡評価を使い、左側で結果が決まる場合には右側の計算を実行しない。

```lean
def isThree (n : Nat) : Bool := n == 3

example : (if isThree 3 then 10 else 20) = 10 := rfl
```

`if` の条件には命題も真偽値も書けるが、それぞれの型は異なる。命題の論理結合子は [論理の記号](logical_symbols.md)、条件分岐は [if](if.md) を参照。名前の末尾の `simp!` や添字アクセスの `xs[i]!` は、この前置の否定演算子とは別である。

参照：[公式リファレンス：Booleans](https://lean-lang.org/doc/reference/latest/Basic-Types/Booleans/)。

[記号索引に戻る](../symbols.md) · [文法要素の一覧に戻る](README.md)
