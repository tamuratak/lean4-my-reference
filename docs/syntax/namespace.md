# `namespace`・`open`・`end`

`namespace N` は、**宣言の名前に `N.` を付けてまとめる**構文である。対応する `end N` でその範囲を閉じる。

```lean
namespace Counter

def start : Nat := 0
def next (n : Nat) : Nat := n + 1

end Counter

example : Counter.next Counter.start = 1 := rfl
```

登録される名前は `Counter.start` と `Counter.next` である。名前空間の中では、同じ名前空間の名前を接頭辞なしで使える。

`open N` は、名前に `N.` を付けずに使えるようにする。

```lean
namespace Counter

def start : Nat := 0
def next (n : Nat) : Nat := n + 1

end Counter

open Counter in
example : next start = 1 := rfl
```

`open … in` は次の一つのコマンドだけに効く。通常の `open Counter` は現在のセクションや名前空間の範囲で効き、ファイルの最上位なら後続部分で使える。

`open Counter (start)` とすれば、指定した名前だけを短く使える。`open` は定義を読み込む [`import`](import.md) とは違い、既にある名前の呼び方を変える。

`open scoped N` は、`N` に結び付いたスコープ付き記法やインスタンスなどだけを有効にする。普通の名前を接頭辞なしにする `open N` と区別する。[記法のページ](notation.md)に例がある。

名前に接頭辞を付けず、変数などの範囲だけを区切る場合は [`section`](section.md) を使う。

参照：[公式リファレンス：Namespaces and Sections](https://lean-lang.org/doc/reference/latest/Namespaces-and-Sections/)。

[文法要素の一覧に戻る](README.md)
