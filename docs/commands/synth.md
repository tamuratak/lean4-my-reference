# `#synth`

`#synth 型クラスの型` は、指定した型クラスのインスタンスを探し、見つかった実装を表示するコマンドである。

```lean
#synth Inhabited Nat
#synth ToString Nat
#synth Decidable (3 < 5)
```

順に、自然数の既定値、自然数を文字列にする処理、`3 < 5` の判定に使うインスタンスを探す。

表示されるのは既定値や文字列の結果ではなく、インスタンスを表す項である。実装を調べたい場合に使う。

```lean
class HasLabel (α : Type) where
  label : α → String

instance natLabel : HasLabel Nat where
  label n := toString n

#synth HasLabel Nat
```

ここでは登録した `natLabel` が選ばれる。

暗黙の引数も含めて表示すると、どの型の実装が組み合わされているかを確認しやすい。

```lean
set_option pp.explicit true in
#synth HAdd Int Int Int
```

`#synth` は任意の型の値を作る命令ではなく、型クラスの探索を行う。インスタンスが見つからなければエラーになる。

型クラスの宣言は [`class`・`instance`](../syntax/class.md)、証明のゴールをインスタンス探索で閉じる操作は[タクティクスの `infer_instance`](../tactics/infer_instance.md)を参照。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
