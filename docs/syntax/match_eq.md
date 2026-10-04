# `match h : e with …`

`match h : e with …` は、**分岐前の式 `e` と、その分岐のパターンが等しいという証明に、名前 `h` を付ける**構文である。

```lean
def classified (b : Bool) : {x : Bool // x = false ∨ x = true} :=
  match h : b with
  | false => ⟨b, Or.inl h⟩
  | true => ⟨b, Or.inr h⟩

example : (classified false).val = false := rfl
```

`false` の分岐では `h : b = false`、`true` の分岐では `h : b = true` が使える。この例は元の `b` と、それがどちらかの値に等しいという証明を部分型にまとめる。

```text
false の分岐：h : b = false
true  の分岐：h : b = true
```

パターンが引数を持つ場合も同じである。

```lean
def positiveOrOne (n : Nat) : {k : Nat // k > 0} :=
  match h : n with
  | 0 => ⟨1, by decide⟩
  | k + 1 => ⟨n, by
      rw [h]
      exact Nat.zero_lt_succ k⟩

example : (positiveOrOne 0).val = 1 := rfl
example : (positiveOrOne 3).val = 3 := rfl
```

`k + 1` の分岐で使える等式は `h : n = k + 1` である。これで `n > 0` を `k + 1 > 0` へ書き換え、必要な証明を作る。

普通の [`match`](match.md) でも入力の形に応じた処理を書ける。`h :` を付ける形は、それに加えて元の式とパターンをつなぐ等式を、明示的な証明として使いたい場合に便利である。

ここの `h : n` は「`h` の型が `n`」という通常の型宣言ではない。`match` の構文として、場合分けする式 `n` の等式に名前を付けている。

参照：[公式リファレンス：Pattern Matching / Pattern Equality Proofs](https://lean-lang.org/doc/reference/latest/Terms/Pattern-Matching/)。

[文法要素の一覧に戻る](README.md)
