# `String`・`Char`：文字列と文字

`String` は文字列の型、`Char` は１つの Unicode スカラー値を表す型である。文字列は二重引用符、文字は単一引用符で書く。追加の `import` は不要である。

## 値を作る・つなぐ

```lean
def greeting : String := "こんにちは"
def letter : Char := 'あ'

example : "Hello" ++ " Lean" = "Hello Lean" := by decide
example : "Lea".push 'n' = "Lean" := by decide
example : String.singleton letter = "あ" := by decide
```

`"あ" : String` と `'あ' : Char` は別の型である。`++` は文字列どうしを連結し、`.push` は末尾に１文字を加える。`String.singleton` は１文字から文字列を作る。

## 長さと文字のリスト

```lean
example : "Lean".length = 4 := by decide
example : "あい".length = 2 := by decide
example : "Lean".toList = ['L', 'e', 'a', 'n'] := by decide
example : String.ofList ['あ', 'い'] = "あい" := by decide
```

`.length` は Unicode スカラー値の数を返す。UTF-8 のバイト数ではなく、複数のスカラー値からなる見た目の１文字とも必ずしも一致しない。`.toList` は `List Char` を返し、`String.ofList` は逆に文字列を作る。

文字列は [`List Char`](list.md) そのものではないので、リストの操作をそのまま適用する場合は変換が必要になる。

## 数値を読み取る

```lean
#eval "123".toNat?
#eval "abc".toNat?
#eval "-3".toInt?
```

出力は順に `some 123`、`none`、`some (-3)` になる。`.toNat?` は自然数として読めれば `some n`、読めなければ `none` を返す。整数には `.toInt?` を使う。結果は [`Option`](option.md) なので、失敗した場合も扱える。

値を文字列に変える `toString` は、読み取りとは逆方向の操作である。

```lean
example : toString (123 : Nat) = "123" := by decide
example : s!"count={(3 : Nat)}" = "count=3" := by decide
```

`s!"…{式}…"` は式の値を文字列へ埋め込む記法である。変換には `ToString` 型クラスの実装を使う。[型クラス](../syntax/class.md)と[リテラルの記法](../syntax/literals.md)も参照。

参照：[公式リファレンス：Strings](https://lean-lang.org/doc/reference/latest/Basic-Types/Strings/)、[Characters](https://lean-lang.org/doc/reference/latest/Basic-Types/Characters/)。

[基本データ型の一覧に戻る](README.md)
