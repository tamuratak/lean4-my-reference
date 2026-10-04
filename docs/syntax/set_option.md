# `set_option`・設定の `in`

`set_option 名前 値` は、**Lean の表示や処理に関する設定を変更する**コマンドである。

```lean
set_option pp.universes true in
#check List
```

`pp.universes` を有効にすると、型の階層に関する引数も表示する。この `in` は、設定の変更を直後の一つのコマンドだけに適用する。

`in` がなければ、現在のセクションや名前空間の範囲で、後続のコマンドに設定が効く。

```lean
section

set_option autoImplicit false

def keep {α : Type} (x : α) : α := x

end

example : keep (3 : Nat) = 3 := rfl
```

`autoImplicit false` は、宣言の型にある未宣言の名前を、暗黙の引数として自動追加する機能を無効にする。この例では `α` を明示的に宣言しているので、その設定でも定義できる。

例えば、この範囲で次の断片を書くと、`α` が未宣言なのでエラーになる。

```text
def keep (x : α) : α := x
```

一つの宣言だけに適用するなら、次のように書ける。

```lean
set_option autoImplicit false in
def keep {α : Type} (x : α) : α := x

example : keep true = true := rfl
```

`end` の後は外側の設定に戻る。ファイルの最上位で `in` を付けなければ、通常はファイルの残りの部分で有効になる。

`in` で次のコマンドだけに範囲を限定する書き方は [`open … in`](namespace.md) にもあるが、変更する内容はそれぞれのコマンドによって異なる。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)、[公式リファレンス：Namespaces and Sections](https://lean-lang.org/doc/reference/latest/Namespaces-and-Sections/)。

[文法要素の一覧に戻る](README.md)
