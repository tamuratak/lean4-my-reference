# 関数の型：`→`・`∀`

`α → β` は、**`α` 型の値を受け取り、`β` 型の値を返す関数の型**である。

```lean
def addOne : Nat → Nat := fun n => n + 1

example : addOne 4 = 5 := rfl
```

`Nat → Nat → Nat` は `Nat → (Nat → Nat)` と読む。最初の自然数を渡すと、もう一つ自然数を受け取る関数が返る。

```lean
def add : Nat → Nat → Nat := fun x y => x + y

def addTwo : Nat → Nat := add 2
example : addTwo 3 = 5 := rfl
```

返す型が引数によって変わるときは、引数に名前を付ける。

```lean
def keep : (α : Type) → α → α := fun α x => x

example : keep Nat 3 = 3 := rfl
example : keep Bool true = true := rfl
```

`α` に `Nat` を渡すと残りは `Nat → Nat`、`Bool` を渡すと `Bool → Bool` になる。これを依存関数型という。

命題でも同じ仕組みを使う。`P → Q` は「`P` の証明を受け取り、`Q` の証明を返す」、つまり含意を表す。`∀ x : α, P x` は、任意の `x` について `P x` の証明を返す型である。

```lean
example (P : Prop) : P → P := fun h => h

example : ∀ n : Nat, n = n := fun n => rfl
```

`∀ x : α, P x` と `(x : α) → P x` は同じ依存関数型の書き方である。

参照：[公式リファレンス：Function Types](https://lean-lang.org/doc/reference/latest/Terms/Function-Types/)。

[文法要素の一覧に戻る](README.md)
