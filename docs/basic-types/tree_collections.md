# `Std.TreeMap`・`Std.TreeSet`：順序付きのマップと集合

`Std.TreeMap α β` は**キーの順序を使う対応表**、`Std.TreeSet α` は**要素の順序を使う集合**である。ハッシュ値ではなく比較関数を使い、木構造で保持する。標準ライブラリの各モジュールをインポートする。

## `TreeMap`：キー順に値を管理する

```lean
import Std.Data.TreeMap

def entries : Std.TreeMap Nat String :=
  ({} : Std.TreeMap Nat String).insert 3 "three" |>.insert 1 "one"

#guard entries.get? 3 == some "three"
#guard entries.get? 2 == none
#guard entries.toList == [(1, "one"), (3, "three")]
#guard entries.minEntry? == some (1, "one")
#guard (entries.insert 3 "THREE").size == 2
```

`.insert`・`.get?`・`.erase` の基本用途は [`HashMap`](hashmap.md) と同じである。`.toList` はキー順に列挙し、`.minEntry?` は最小のキーと値のペアを返す。同じキーへの `.insert` は対応する値を置き換える。

## `TreeSet`：要素を順序付きで管理する

```lean
import Std.Data.TreeSet

def numbers : Std.TreeSet Nat :=
  ({} : Std.TreeSet Nat).insert 3 |>.insert 1 |>.insert 3

#guard numbers.contains 1
#guard numbers.size == 2
#guard numbers.toList == [1, 3]
#guard (numbers.erase 1).toList == [3]
```

重複する要素を入れても増えず、`.toList` は比較関数に従う順序で返す。要素の有無だけを管理する点は [`HashSet`](hashset.md) と同じである。

## 順序は比較関数で決まる

通常の `Std.TreeMap α β`・`Std.TreeSet α` は、`Ord α` 型クラスの `compare` を既定の比較関数として使う。`Nat` なら数の小さい順、`String` なら文字列の比較順になる。明示的な比較関数も指定できる。

```lean
import Std.Data.TreeSet

def descending : Std.TreeSet Nat (fun a b => compare b a) :=
  ({} : Std.TreeSet Nat (fun a b => compare b a)).insert 1 |>.insert 3

#guard descending.toList == [3, 1]
```

比較結果が `.eq` になるキーは同じキーとして扱う。自作の比較関数では、順序が一貫するようにする必要がある。単に検索する用途にはハッシュ版、順序付きの列挙や最小・最大の取得にはツリー版という違いがある。

参照：[公式 API：TreeMap](https://lean-lang.org/doc/api/Std/Data/TreeMap/Basic.html#Std.TreeMap)、[TreeSet](https://lean-lang.org/doc/api/Std/Data/TreeSet/Basic.html#Std.TreeSet)。

[基本データ型の一覧に戻る](README.md)
