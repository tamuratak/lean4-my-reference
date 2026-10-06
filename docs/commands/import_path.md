# `#import_path`

`#import_path 宣言名` は、その宣言がどのモジュールから、どのインポートの経路を通じて使えるようになったかを表示するコマンドである。

```lean
import Lean

#import_path Nat.add
```

`Nat.add` を定義しているモジュールと、そのモジュールを現在のファイルへ読み込むまでの経路が表示される。経路には、直接の `import` だけでなく間接的な読み込みも含まれる。

自分で直接読み込んでいない名前が使える場合、その理由を調べる助けになる。

```lean
import Std

#import_path Std.HashMap
```

ここで指定するのは `Std` というモジュール名ではなく、調べたい宣言名 `Std.HashMap` である。表示内容は、現在のファイルのインポートに応じて変わる。

このコマンドは読み込みの経路を表示するだけで、新たにモジュールを読み込むものではない。読み込む方法は [`import`](../syntax/import.md)、宣言の型や本体を確認する方法は [`#check`](check.md)・[`#print`](print.md) を参照。

参照：[公式 API：`#import_path`](https://lean-lang.org/doc/api/Lean/Parser/Command.html#Lean.Parser.Command.importPath)。

[`#` コマンドの一覧に戻る](README.md)
