# 定義の展開を指定する属性

`reducible` などの属性は、**型の照合や自動処理で、定義の本体をどこまで展開できるか**を指定する。定理を登録する `simp` 属性とは違う働きである。

## `reducible`：別名として展開しやすくする

```lean
@[reducible] def Label := String

#synth ToString Label
#eval toString ("hello" : Label)
```

インスタンス探索が `Label` を `String` に展開できるので、既存の `ToString String` を使える。表示結果は `"hello"` である。

この用途では `abbrev Label := String` と書く方法もある。`abbrev` は、通常、`reducible` な定義を作る。

## 通常の `def` との違い

```lean
def Label := String

def greeting : Label := "hello"
#check_failure (inferInstance : ToString Label)
```

通常のこの `def` は `semireducible` である。値の型を照合するときは本体を展開できるので `greeting` は定義できるが、インスタンス探索ではその別名を展開せず、`ToString Label` は見つからない。

`#check_failure` は、その式の型の確認が失敗することを検査するコマンドである。

## `irreducible`：通常の照合では展開させない

```lean
@[irreducible] def Secret := String

#check_failure ("hello" : Secret)

example : Secret = String := by
  unfold Secret
  rfl
```

通常の型の照合では `Secret` を `String` に展開しないため、文字列をそのまま `Secret` として渡すことはできない。一方、`unfold Secret` と明示すれば、証明の中で本体を展開できる。

`irreducible` は定義の本体を削除する設定ではない。`opaque` 宣言との違いは、[`opaque`・`axiom`](../syntax/opaque_axiom.md)を参照。

## 関連する設定

| 属性 | 主な用途 |
| --- | --- |
| `reducible` | 定義を別名のように広く展開できるようにする |
| `instance_reducible` | インスタンスの本体を、インスタンス探索などで展開できるようにする |
| `implicit_reducible` | 暗黙引数の型の照合などで展開できるようにする |
| `semireducible` | 通常の型の照合では展開するが、探索などでは展開を制限する |
| `irreducible` | 通常の型の照合では展開を抑える |

どの設定が使われるかは処理側の透明性設定にも依存する。この表は主な用途の目安である。全定義を `reducible` にすると、展開や探索が増えることがあるため、一律に付けるものではない。

`@[inline]` は実行コードのコンパイル時のインライン化に関わる別の属性であり、型の照合のための `reducible` と同じものではない。

参照：[公式リファレンス：Controlling Reduction](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/#reducibility)。

[属性の一覧に戻る](README.md)
