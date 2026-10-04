# `Fin n`：範囲が決まった自然数

`Fin n` は、**`n` 未満の自然数を、その範囲条件の証明とともに保持する型**である。例えば `Fin 3` の値は `0`、`1`、`2` に対応する。追加の `import` は不要である。

## 値を作る・取り出す

```lean
def index : Fin 3 := ⟨1, by decide⟩

example : index.val = 1 := rfl
example : index.val < 3 := index.isLt
```

`⟨1, by decide⟩` は自然数 `1` と `1 < 3` の証明を渡す。`.val` で自然数を、`.isLt` で範囲内という証明を取り出せる。`⟨4, …⟩ : Fin 3` を作ろうとしても、必要な `4 < 3` は証明できない。

変数から作る場合も、範囲条件を渡す。

```lean
def makeIndex (n k : Nat) (h : k < n) : Fin n := ⟨k, h⟩

example : (makeIndex 5 2 (by decide)).val = 2 := rfl
```

`n` が型の一部なので、`Fin 3` と `Fin 5` は別の型である。[依存ペア型 `Σ`](../syntax/sigma.md) の `Σ n : Nat, Fin n` は、この上限と範囲内の数を一緒に保持する。

## 数値リテラルと演算は巡回する

```lean
example : (4 : Fin 3).val = 1 := rfl
example : ((2 : Fin 3) + 1).val = 0 := rfl
```

正の上限に対する数値リテラルは上限で割った余りとして解釈されるので、`(4 : Fin 3)` はエラーではなく `1` を表す。加算も上限で巡回する。**`Fin n` のリテラルや演算は、元の数が範囲内か検査して拒否する操作ではない**。元の自然数が範囲内であることを保証したいなら、上の `⟨k, h⟩` を使う。

`Fin 0` には値がない。自然数 `k` と `k < 0` の証明を組にすることができないためである。

参照：[公式リファレンス：Finite Natural Numbers](https://lean-lang.org/doc/reference/latest/Basic-Types/Finite-Natural-Numbers/)。

[基本データ型の一覧に戻る](README.md)
