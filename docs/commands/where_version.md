# `#where`・`#version`

`#where` は、**現在の名前空間や共通変数、開いた名前空間、変更した設定などを表示する**コマンドである。

```lean
namespace Demo

variable (n : Nat)
open List
set_option pp.universes true

#where

end Demo
```

表示には、例えば次のような現在の範囲の情報が含まれる。

```text
namespace Demo
open List
variable (n : Nat)
set_option pp.universes true
```

上の表示は必要な部分を抜き出した説明である。実際には外側の範囲の設定や、実行環境に由来する情報が含まれることもある。

`#where` は宣言の補助関数を定義する [`where`](../syntax/where.md) とは別のコマンドである。また、現在の範囲を変える命令ではなく、その情報を表示する。

`#version` は、使っている Lean のバージョンと実行環境の情報を表示する。

```lean
#version
```

このリファレンスでは Lean 4.35.0-rc3 を指定している。別の環境で例の振る舞いが違う場合、実際に使われているバージョンを確認する助けになる。

個々の宣言は [`#print`](print.md)、名前空間や設定の指定方法は [`namespace`](../syntax/namespace.md) と [`set_option`](../syntax/set_option.md) を参照。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
