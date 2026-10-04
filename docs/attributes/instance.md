# `@[instance]`：型クラスの候補に登録する

`@[instance]` は、**型クラスの値を返す宣言を、インスタンス探索の候補として登録する**属性である。登録すると、`[Inhabited α]` などのインスタンス引数に、その宣言を自動で使える。

```lean
structure Token where
  value : Nat

@[instance, instance_reducible]
def tokenDefault : Inhabited Token := ⟨⟨7⟩⟩

#synth Inhabited Token
#eval (default : Token).value
```

`#synth` は登録された `Inhabited Token` を見つける。`default` はそのインスタンスを通じて既定値を取り出し、最後の結果は `7` になる。

`instance_reducible` は、この定義の本体をインスタンス探索などで展開できるようにする属性である。型クラスの値を `def` で定義する場合にも適切な展開設定が必要になるため、この例では併記している。

## 通常は `instance` 宣言を使う

```lean
structure Token where
  value : Nat

instance tokenDefault : Inhabited Token := ⟨⟨7⟩⟩

#eval (default : Token).value
```

新しくインスタンスを書くなら、この形の方が簡潔である。`instance` 宣言は、探索への登録に加え、インスタンス用の展開設定も行う。

`@[instance]` は登録の指定、`instance` は宣言の構文、`[Inhabited Token]` はインスタンス引数なので、役割を区別する。

## 既存の定義を局所的に登録する

```lean
structure Token where
  value : Nat

@[instance_reducible]
def tokenDefault : Inhabited Token := ⟨⟨7⟩⟩

section
attribute [local instance] tokenDefault
#synth Inhabited Token
end
```

`tokenDefault` は最初から名前で指定して使える値だが、探索の候補になるのは `attribute` の後、このセクションの中だけである。セクションが終わっても定義自体は残る。

型クラスでない型の値を、無条件にインスタンスとして登録できるわけではない。型クラスや `instance` 宣言の書き方は、[`class`・`instance`](../syntax/class.md)も参照。

参照：[公式リファレンス：Instance Declarations](https://lean-lang.org/doc/reference/latest/Type-Classes/Instance-Declarations/)。

[属性の一覧に戻る](README.md)
