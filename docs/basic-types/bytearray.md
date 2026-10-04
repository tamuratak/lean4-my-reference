# `ByteArray`：バイト列

`ByteArray` は、**`UInt8` の値を並べたバイト列の型**である。ファイルの内容や通信データなど、文字列とは限らないデータを扱う。追加の `import` は不要である。

## 作る・読み取る

```lean
def bytes : ByteArray := ByteArray.empty.push 65 |>.push 66

#guard bytes.size == 2
#guard bytes[0].toNat == 65
#guard bytes.toList == ([65, 66] : List UInt8)
#guard (bytes.push 67).size == 3
```

`ByteArray.empty` は空のバイト列、`.push` は末尾に１バイトを加えた列を返す。`.size` はバイト数、添字アクセスはその位置の `UInt8` を返す。`.toList` で `List UInt8` に変換できる。[配列](array.md)と似た操作を使うが、`ByteArray` はバイト専用の型である。

## 文字列との違い

```lean
def textBytes : ByteArray := "あ".toUTF8

#guard "あ".length == 1
#guard textBytes.size == 3
#guard String.fromUTF8? textBytes == some "あ"
#guard String.fromUTF8? (ByteArray.empty.push 255) == none
```

`.toUTF8` は文字列を UTF-8 のバイト列へ変換する。`"あ"` は１つの Unicode スカラー値だが、UTF-8 では３バイトになる。

任意のバイト列が正しい UTF-8 とは限らないので、`String.fromUTF8?` は読み取れれば `some text`、不正なら `none` を返す。文字を扱うなら [`String`・`Char`](string_char.md)、個々のバイトの計算は[固定幅整数](fixed_width.md)を参照。

参照：[公式リファレンス：Byte Arrays](https://lean-lang.org/doc/reference/latest/Basic-Types/Byte-Arrays/)。

[基本データ型の一覧に戻る](README.md)
