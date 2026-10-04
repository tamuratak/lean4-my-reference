# `Nat`：自然数

`Nat` は、**０から始まる自然数 `0, 1, 2, …` の型**である。個数や長さ、添字などに使う。負の数は含まれず、型として固定の上限はない。追加の `import` は不要である。

## 値と基本計算

```lean
def count : Nat := 3

example : count + 2 = 5 := rfl
example : (3 : Nat) * 4 = 12 := rfl
example : (7 : Nat) / 2 = 3 := rfl
example : (7 : Nat) % 2 = 1 := rfl
```

`+` は加算、`*` は乗算、`/` は自然数の商、`%` は余りである。自然数の割り算は小数を返さない。数値リテラルは他の型にも使えるため、型を明確にしたい場合は `(3 : Nat)` と書く。

## 引き算は０で止まる

```lean
example : (5 : Nat) - 2 = 3 := rfl
example : (2 : Nat) - 5 = 0 := rfl
```

`Nat` に負の数はないので、引く数が大きい場合は結果が `0` になる。負の結果も扱いたいなら [`Int`](int.md) を使う。自然数では `(a - b) + b = a` が無条件に成立するわけではない。

## ０と後続の数に分ける

`Nat` のコンストラクターは `Nat.zero` と `Nat.succ n` である。後者は `n + 1` を表す。

```lean
def predecessor (n : Nat) : Nat :=
  match n with
  | 0 => 0
  | Nat.succ k => k

example : predecessor 0 = 0 := rfl
example : predecessor 4 = 3 := rfl
```

`Nat.succ k` の枝では、１つ小さい自然数 `k : Nat` が使える。標準の `Nat.pred` もこの直前の数を返す。自然数についての証明を０と後続の数に分ける方法は、[帰納法](../tactics/induction.md)を参照。

参照：[公式リファレンス：Natural Numbers](https://lean-lang.org/doc/reference/latest/Basic-Types/Natural-Numbers/)。

[基本データ型の一覧に戻る](README.md)
