# `Thunk α`：必要になるまで計算を遅らせる

`Thunk α` は、`α` 型の値を作る計算を、値が必要になるまで遅らせる型である。実行時には、一度計算した結果を保存して再利用する。追加の `import` は不要である。

## 計算を包む・結果を取り出す

```lean
def delayed : Thunk Nat := Thunk.mk (fun () => 2 + 3)

example : delayed.get = 5 := rfl
```

`Thunk.mk` に `Unit → α` の関数を渡す。関数の引数 `()` に情報はなく、本体が遅らせる計算になる。`.get` で値を要求すると、実行時には未計算なら計算し、計算済みなら保存した結果を返す。

## 既にある値を包む

```lean
def ready : Thunk Nat := Thunk.pure 5

example : ready.get = 5 := rfl
```

`Thunk.pure` は既にある値を包む。`Thunk.pure (f x)` では、引数 `f x` の計算そのものを遅らせることにはならない。遅らせたいなら `Thunk.mk (fun () => f x)` と書く。

## 普通の関数との違い

```lean
def makeValue : Unit → Nat := fun () => 2 + 3
def delayedValue : Thunk Nat := Thunk.mk makeValue

example : makeValue () = delayedValue.get := rfl
```

論理上は同じ結果を返すが、普通の関数の型 `Unit → α` 自体は結果を保存する仕組みを持たない。`Thunk` の再利用は実行時の仕組みであり、上の等式の証明は計算回数を検証するものではない。

`Option α` は値の有無を表すが、`Thunk α` は必要になれば得られる値の計算を包む。入出力や状態を変える操作を表す `IO α` とも異なる。[`Unit`](unit_empty.md)と[関数型](../syntax/function_types.md)も参照。

参照：[公式リファレンス：Lazy Computations](https://lean-lang.org/doc/reference/latest/Basic-Types/Lazy-Computations/)。

[基本データ型の一覧に戻る](README.md)
