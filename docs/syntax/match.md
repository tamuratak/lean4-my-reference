# 式の `match`

`match` は、**値の形をパターンで分け、各場合の結果を返す**構文である。

```lean
def valueOrZero (x : Option Nat) : Nat :=
  match x with
  | none => 0
  | some n => n

example : valueOrZero none = 0 := rfl
example : valueOrZero (some 7) = 7 := rfl
```

`none` なら `0`、`some n` なら中身を `n` と呼んで返す。`|` が分岐の開始、`=>` がパターンと結果の区切りである。

`some`・`none` と型そのものの意味は [`Option α`](../basic-types/option.md)、リストの構造は [`List α`](../basic-types/list.md) を参照。

リストのような再帰的な型にも使える。

```lean
def firstOrZero (xs : List Nat) : Nat :=
  match xs with
  | [] => 0
  | n :: _ => n

example : firstOrZero [4, 5] = 4 := rfl
```

`[]` は空リスト、`n :: _` は先頭 `n` と残りのリストがある形である。パターンの `_` は、ここでは使わない成分を表す。

複数の値を同時に分けることもできる。

```lean
def both (a b : Bool) : Bool :=
  match a, b with
  | true, true => true
  | _, _ => false

example : both true false = false := rfl
```

分岐は上から順に使われ、最後の `_, _` は先の行で扱わなかった場合を受け取る。通常の `match` はすべての場合を覆い、各分岐が全体の型に合う項を返す必要がある。

`by` の中で証明を分ける場合は、[タクティクスの `match`](../tactics/match.md)を参照。

分岐前の式とパターンが等しいという証明を使う場合は [`match h : e with …`](match_eq.md) を参照。

型や他のパターンから値が決まる箇所を示す `.(式)` は[非アクセス可能パターン](inaccessible_patterns.md)を参照。

参照：[公式リファレンス：Pattern Matching](https://lean-lang.org/doc/reference/latest/Terms/Pattern-Matching/)。

[文法要素の一覧に戻る](README.md)
