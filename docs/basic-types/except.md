# `Except ε α`：成功の値か失敗の理由

`Except ε α` は、成功した場合の `α` 型の値か、失敗した場合の `ε` 型の情報を保持する型である。第１引数がエラーの型、第２引数が成功の型になる。追加の `import` は不要である。

## 成功・失敗の結果の作成

```lean
def parseCount (text : String) : Except String Nat :=
  match text.toNat? with
  | some n => Except.ok n
  | none => Except.error "not a natural number"

#eval parseCount "12"
#eval parseCount "abc"
```

出力は順に `Except.ok 12`、`Except.error "not a natural number"` になる。`Except.ok value` は成功の値、`Except.error reason` は失敗の情報を渡すコンストラクターである。[`Option`](option.md) の `none` は理由を持たないが、`Except` は失敗理由をデータとして保持できる。

## 成功値とエラーのパターンによる場合分け

```lean
def describe (result : Except String Nat) : String :=
  match result with
  | Except.ok n => s!"count={n}"
  | Except.error message => "error: " ++ message

example : describe (Except.ok 3) = "count=3" := by decide
example : describe (Except.error "missing") = "error: missing" := by decide
```

成功の枝では `n : Nat`、失敗の枝では `message : String` が使える。単なる文字列に限らず、自作のエラー型を `ε` に使うこともできる。

## `do` による成功値の受け渡しとエラーの伝播

```lean
def addOne (input : Except String Nat) : Except String Nat := do
  let n ← input
  return n + 1

example : addOne (Except.ok 3) = Except.ok 4 := rfl
example : addOne (Except.error "missing") = Except.error "missing" := rfl
```

`ok` なら中身を受け取って次の計算へ進み、`error` なら後続を進めず、そのエラーを返す。`Except.error` の値を作るだけで、外側の `IO` に例外を投げるわけではない。[`do` 記法](../syntax/do.md)と[直和型](sum.md)も参照。

参照：[公式 API：Except](https://lean-lang.org/doc/api/Init/Control/Except.html)。

[基本データ型の一覧に戻る](README.md)
