# 計算をつなぐ `>>=`・`<$>`・`<*>`・`<*`・`*>`・`<|>`

これらは、**`Option` や `IO` などの計算を、結果の受け渡しや順序を指定して組み合わせる**記法である。具体的な動作は型に登録された実装による。ここでは、値があるか失敗するかを表す `Option` で説明する。

## 結果を次の計算に渡す `>>=`

`action >>= f` は、計算 `action` の結果を関数 `f` に渡し、次の計算を行う。

```lean
def addOne (x : Option Nat) : Option Nat := x >>= fun n => some (n + 1)

example : addOne (some 3) = some 4 := rfl
example : addOne none = none := rfl
```

`Option` では `some n` なら `f n` に進み、`none` なら後続を進めず `none` になる。`do` 記法の `let n ← action` に対応するつなぎ方である。

## 結果を変換する `<$>` と、関数を適用する `<*>`

`f <$> action` は、計算の中にある結果へ通常の関数 `f` を適用する。`functions <*> values` は、計算の中にある関数を、別の計算の中にある値に適用する。

```lean
example : ((fun n : Nat => n + 1) <$> some 3) = some 4 := rfl
example : (some (fun n : Nat => n + 1) <*> some 3) = some 4 := rfl
```

`<$>` の左側は普通の関数、`<*>` の左側は `Option` に入った関数である。`>>=` は後続の計算を関数で指定し、`<$>` は結果の値を普通の関数で変える。

## 両方を実行し、片方の結果を残す `<*` と `*>`

```lean
example : ((some 3 : Option Nat) <* some 7) = some 3 := rfl
example : ((some 3 : Option Nat) *> some 7) = some 7 := rfl
example : ((some 3 : Option Nat) <* (none : Option Nat)) = none := rfl
```

`<*` は左の結果、`*>` は右の結果を残す。`Option` では途中で失敗すれば全体が `none` なので、結果を使わない側の計算も重要である。成功した場合は、両方の計算を順に処理する。

## 別の候補を試す `<|>`

`a <|> b` は、先の候補が成功しなかった場合に後の候補を使う。`Option` では、先が `some` ならそれを採用し、`none` なら後を使う。

```lean
example : ((some 3 : Option Nat) <|> some 7) = some 3 := rfl
example : ((none : Option Nat) <|> some 7) = some 7 := rfl
```

任意の `IO` の例外処理をこの `Option` の動作と同一視せず、その型の実装を確認する。`<|>` は [関数適用の `<|` と `|>`](application_shortcuts.md) と異なる記法である。

`>>` は、Lean 本体ではパーサーなどの `AndThen` を持つ型で使う記法で、通常の `Option` にはそのインスタンスがない。結果を捨てて次の `Option` の計算に進むなら `*>` を使う。[パーサーの組み合わせ](parser_combinators.md)を参照。

記号が長く並んで読みにくい場合は [do 記法](do.md)で結果に名前を付けて書くと、処理の流れを追いやすい。

参照：[公式リファレンス：Functors, Monads and do-Notation](https://lean-lang.org/doc/reference/latest/Functors___-Monads-and--do--Notation/)、[公式 API：計算を組み合わせる記法](https://lean-lang.org/doc/api/Init/Notation.html)。

[記号索引に戻る](../symbols.md) · [文法要素の一覧に戻る](README.md)
