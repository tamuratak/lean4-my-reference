# `Prod α β`・`α × β`：ペア

`Prod α β` は、**`α` 型の値と `β` 型の値を両方保持するペアの型**である。通常は `α × β` と書く。追加の `import` は不要である。

## 作る・取り出す

```lean
def entry : Nat × String := (3, "three")

example : entry.1 = 3 := rfl
example : entry.2 = "three" := rfl
example : (Nat × String) = Prod Nat String := rfl
example : (3, "three") = Prod.mk 3 "three" := rfl
```

`(x, y)` は `Prod.mk x y` の記法である。`.1`（`.fst`）で１番目、`.2`（`.snd`）で２番目を取り出す。期待される型が分かるときは `⟨x, y⟩` でも作れる。

## 分解する・３つ以上をまとめる

```lean
def describe (p : Nat × String) : String :=
  match p with
  | (n, text) => s!"{n}: {text}"

example : describe (3, "three") = "3: three" := by decide

def triple : Nat × String × Bool := (3, "three", true)
example : triple.2.1 = "three" := rfl
example : triple.2.2 = true := rfl
```

分解した枝では `n : Nat` と `text : String` の両方を使える。`α × β × γ` は `α × (β × γ)` と読むため、３つの値は入れ子のペアになる。

## 関連する型との違い

[`Sum α β`](sum.md) はどちらか一方の値を保持するが、`Prod α β` は両方を保持する。[依存ペア型 `Σ x : α, β x`](../syntax/sigma.md) では２番目の型が１番目の値によって決まるが、普通のペアの２番目の型は固定である。

命題 `P ∧ Q` も２つの証明をまとめるが、データのペア `α × β` とは別の型である。構築記法の詳細は[組とコンストラクター](../syntax/anonymous_constructor.md)を参照。

参照：[公式リファレンス：Tuples](https://lean-lang.org/doc/reference/latest/Basic-Types/Tuples/)。

[基本データ型の一覧に戻る](README.md)
