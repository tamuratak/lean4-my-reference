# `deriving`

`deriving` は、**新しく定義した型について、指定した型クラスのインスタンスを自動生成する**構文である。

```lean
inductive Color where
  | red
  | blue
  deriving Repr, DecidableEq

#eval Color.red
example : Color.red ≠ Color.blue := by decide
```

`Repr` は値の表示に、`DecidableEq` は等しいかどうかの判定に使う。この例では `#eval` でコンストラクターを表示し、`decide` で二つの値が異なることを証明できる。

`structure` にも付けられる。

```lean
structure Point where
  x : Nat
  y : Nat
  deriving Repr, DecidableEq

#eval (Point.mk 2 3)
example : (Point.mk 2 3) = (Point.mk 2 3) := by decide
```

`Point` の各フィールドについて利用可能な実装を使い、`Point` 全体の実装を組み立てる。例えば等値判定を導出するには、成分についても等値判定を用意できる必要がある。

既に定義した型に対しては、別のコマンドとして指定できる。

```lean
inductive Switch where
  | off
  | on

deriving instance Repr, DecidableEq for Switch

#eval Switch.on
example : Switch.off ≠ Switch.on := by decide
```

`deriving` は任意の型クラスを自動実装するものではない。対応する生成処理が用意され、その型に適用できる場合に使える。

実装を自分で選びたいときは [`instance`](class.md) を書く。表示用の `Repr` と、人向けの文字列を作る `ToString` も別の型クラスである。

参照：[公式リファレンス：Deriving Instances](https://lean-lang.org/doc/reference/latest/Type-Classes/Deriving-Instances/)。

[文法要素の一覧に戻る](README.md)
