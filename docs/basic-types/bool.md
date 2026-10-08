# `Bool`：真偽値

`Bool` は、`true` と `false` の２つの値を持つデータ型である。計算による判定結果やフラグを表す。追加の `import` は不要である。

## 真偽値による分岐

```lean
def label (enabled : Bool) : String :=
  match enabled with
  | true => "on"
  | false => "off"

example : label true = "on" := rfl
example : label false = "off" := rfl
```

２つの値はコンストラクターであり、`match` で分けられる。`if enabled then … else …` と書くこともできる。

## `Bool` と `Prop` の違い

```lean
def isThree (n : Nat) : Bool := n == 3

example : isThree 3 = true := rfl
example : (if isThree 4 then 10 else 20) = 20 := rfl
example : decide (3 < 5) = true := rfl
```

`n == 3` は `Bool` を返す比較の計算、`n = 3` は `Prop` に属する命題である。`true : Bool` という値と、命題 `True : Prop` も別のものである。

`decide P` は、命題 `P` を判定する実装があるとき、その結果を `Bool` として返す。命題が真であることを証明したい場合は、真偽値そのものではなく `h : P` が必要になる。

## 真偽値の演算

```lean
example : (!true) = false := rfl
example : (true && false) = false := rfl
example : (false || true) = true := rfl
```

`!` は反転、`&&` は両方が真か、`||` はどちらかが真かを計算する。比較や命題との対応の詳細は[真偽値の演算子](../syntax/boolean_operators.md)、命題の記号は[論理の記号](../syntax/logical_symbols.md)を参照。

参照：[公式リファレンス：Booleans](https://lean-lang.org/doc/reference/latest/Basic-Types/Booleans/)。

[基本データ型の一覧に戻る](README.md)
