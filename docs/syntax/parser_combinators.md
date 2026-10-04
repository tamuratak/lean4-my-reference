# パーサーの `>>` と、構文定義の `<|>`

`>>` は、**その型に登録された `AndThen` などの実装に従って、処理を順に組み合わせる**記法である。Lean のパーサーでは、左のパーサーの後に右のパーサーで入力を読む。

```lean
import Lean

def greetingParser : Lean.Parser.Parser :=
  Lean.Parser.symbol "hello" >> Lean.Parser.symbol "!"

#check greetingParser
```

この値は `hello` に続いて `!` を読むパーサーである。定義しただけでは、新しい構文として登録されるわけではない。ここではパーサーを表す値の組み合わせを示している。

`>>` は型ごとの実装を必要とし、通常の `Option` や `IO` に一律に使えるモナドの記法ではない。例えば結果を捨てて次の `Option` の計算に進むには [*>](monad_operators.md) を使う。

構文定義の中の `<|>` は、**入力を読むための候補を選ぶ**記法である。

```lean
import Lean

syntax "yesno(" ("yes" <|> "no") ")" : term

macro_rules
  | `(yesno(yes)) => `(true)
  | `(yesno(no)) => `(false)

example : yesno(yes) = true := rfl
example : yesno(no) = false := rfl
```

`("yes" <|> "no")` により、その位置には `yes` または `no` を書ける。これは `syntax` の文法を指定するための `<|>` であり、式の [Option の候補選択](monad_operators.md)とは書く場所と処理する対象が異なる。

通常の Lean の証明を読む段階では、まず [関数適用のパイプ記法](application_shortcuts.md)や [do 記法](do.md)を押さえればよい。このページの記号は、構文拡張やタクティクスの実装を読むときに参照する。

参照：[公式リファレンス：Defining New Syntax](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/Defining-New-Syntax/)、[公式 API：Lean のパーサー](https://lean-lang.org/doc/api/Lean/Parser/Basic.html)。

[記号索引に戻る](../symbols.md) · [文法要素の一覧に戻る](README.md)
