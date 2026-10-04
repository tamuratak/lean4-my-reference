# 引数の括弧：`(…)`・`{…}`・`[…]`

引数を囲む括弧は、**呼び出し時に引数をどう渡すか**を指定する。

| 書き方 | 引数の渡し方 |
| --- | --- |
| `(x : α)` | 明示的な引数。通常は呼び出す側が渡す |
| `{x : α}` | 暗黙の引数。他の引数や期待される型から Lean が推論する |
| `[C α]` | インスタンス引数。型クラスのインスタンス探索で補う |
| `⦃x : α⦄` | 厳密な暗黙の引数。後続の明示的な引数を渡すまで、自動挿入を待つ |

例えば、型だけを暗黙にし、値を明示的に受け取れる。

```lean
def keep {α : Type} (x : α) : α := x

#check keep 3
example : keep 3 = 3 := rfl
example : keep (α := Nat) 3 = 3 := rfl
```

`keep 3` では、値 `3` から `α` が `Nat` と決まる。推論だけでは決まらない場合は `(α := Nat)` のように引数名で指定できる。

インスタンス引数は、単なる型の推論とは別に、登録済みの実装を探して補う。

```lean
def render {α : Type} [ToString α] (x : α) : String := toString x

#eval render (12 : Nat)
```

`[ToString α]` は「`α` を文字列にする実装が使える」という要求である。ここでは `Nat` の実装が選ばれ、出力は `"12"` になる。詳しくは [`class`・`instance`](class.md) を参照。

同じ型の明示的な引数は `(x y : Nat)` とまとめられる。`{…}` で囲んでも引数がなくなるわけではなく、呼び出し時の指定を省けるだけである。

省略時の値を指定する `(x : α := e)` と、タクティクスで補う引数は[引数の既定値](default_parameters.md)を参照。

## 厳密な暗黙引数

暗黙引数の「自動挿入」は、**具体的な型をすぐに決めて入れることではない**。まず未確定の引数を入れ、他の引数や期待される型から、その中身を決める。

```lean
def ordinaryKeep {α : Type} (x : α) : α := x

example : ordinaryKeep (3 : Nat) = 3 := rfl
example : Nat → Nat := ordinaryKeep
```

通常の暗黙引数では、`ordinaryKeep` を式として使うと、Lean は概念的に次のように扱う。

```text
ordinaryKeep (α := ?α)
```

`?α` は「あとで決める型」を表す説明用の記号である。値 `3` を渡す例では、その値から `α = Nat` と決まる。**引数の挿入は先にしても、型の決定はあとでよい**。

明示的な引数を待たないのは、値を渡さなくても型が決まる場合があるからである。上の `example : Nat → Nat := ordinaryKeep` では、関数に値を渡していない。しかし、「ここには `Nat → Nat` 型の関数が必要」という情報から `α = Nat` と決まる。

一方、厳密な暗黙引数 `⦃α : Type⦄`（`{{α : Type}}` とも書ける）は、**後続の明示的な引数を渡すまで、未確定の引数の自動挿入を待つ**。

```lean
def strictKeep ⦃α : Type⦄ (x : α) : α := x

example : strictKeep (3 : Nat) = 3 := rfl
```

`strictKeep` だけを使う段階では `α` を補わず、`⦃α : Type⦄` が引数として残る。`strictKeep (3 : Nat)` と値を渡すと、その時点で `α` を自動挿入し、`Nat` と推論する。

つまり、値を渡して呼び出す場合の使い方は同じで、違いは**値を渡す前に、暗黙引数を補い始めるかどうか**にある。

### 厳密な暗黙引数だとエラーになる例

後続に明示的な引数がない場合は、通常の暗黙引数の方が使いやすい。例えば、空リストを返す定義で比較できる。

```lean
def empty {α : Type} : List α := []
def strictEmpty ⦃α : Type⦄ : List α := []

example : List Nat := empty
example : List Nat := strictEmpty (α := Nat)
```

`empty` は、期待される型 `List Nat` から `α = Nat` を推論できる。一方、`strictEmpty` を型の指定なしで使うと、次はエラーになる。

```text
example : List Nat := strictEmpty

Type mismatch
  strictEmpty
has type
  ⦃α : Type⦄ → List α
but is expected to have type
  List Nat
```

`strictEmpty` には後続の明示的な引数がないため、自動挿入を始めるきっかけがない。`α` が引数として残り、リストそのものではなく「型を受け取ってリストを返す関数」になっている。上の成功例のように `(α := Nat)` を指定すれば使えるが、通常の暗黙引数ならこの指定は不要である。

このため、すべての暗黙引数を厳密にするのではなく、`⦃…⦄` は後続に明示的な引数がある場合に使うのが基本である。

参照：[公式リファレンス：Functions / Implicit Parameters](https://lean-lang.org/doc/reference/latest/Terms/Functions/)。

[文法要素の一覧に戻る](README.md)
