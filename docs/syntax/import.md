# `import`

`import` は、**別のモジュールにある定義、定理、構文などを読み込む**コマンドである。通常はファイルの先頭に書く。

```lean
import Std.Tactic

example (n : Nat) : n ≤ n + 1 := by
  omega
```

この例は `Std.Tactic` を読み込んだファイルとして実行できる。`Nat` や基本的な構文は通常の Lean ファイルで既に使えるが、ここでは標準タクティクスも明示的に読み込んでいる。

モジュール名の `.` は、モジュール探索用のディレクトリの区切りに対応する。例えば `Std.Tactic` は `Std/Tactic.lean` に対応するモジュールである。Lean は設定された探索パス上のコンパイル済みモジュールを読み込む。

読み込むモジュールは、必要に応じて複数行で指定できる。

```lean
import Std
import Lean

#check Lean.Expr
```

`import` はファイルを読み込む単位、[`namespace`](namespace.md) は宣言名を整理する単位である。モジュール名と、その中で定義される名前空間が一致するとは限らない。

また、`import` してもすべての名前が接頭辞なしで使えるわけではない。例えば `Lean.Expr` を短く `Expr` と書きたい場合は、`open Lean` などで名前空間を開く。

この文法リファレンスの完成例は、コードブロックごとに独立している。必要な追加インポートは、それぞれのコードブロックに記載する。

参照：[公式リファレンス：Source Files and Modules](https://lean-lang.org/doc/reference/latest/Source-Files-and-Modules/)。

[文法要素の一覧に戻る](README.md)
