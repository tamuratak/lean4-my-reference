# `Std.HashSet α`：ハッシュ集合

`Std.HashSet α` は、**`α` 型の要素が含まれるかどうかを管理する集合**である。同じ要素を複数回入れても重複して数えない。標準ライブラリの `import Std.Data.HashSet` を使う。

## 要素を入れる・有無を調べる

```lean
import Std.Data.HashSet

def names : Std.HashSet String :=
  ({} : Std.HashSet String).insert "Alice" |>.insert "Bob" |>.insert "Alice"

#guard names.contains "Alice"
#guard !(names.contains "Carol")
#guard names.size == 2
#guard !(names.erase "Alice").contains "Alice"
```

`.insert` は要素を含む集合、`.erase` は要素を除いた集合を返す。`.contains` は有無を `Bool`、`.size` は異なる要素の数を返す。上の例では `"Alice"` を２回入れても要素数は２である。

## リスト・マップとの違い

```lean
import Std.Data.HashSet

def items : Std.HashSet Nat :=
  ({} : Std.HashSet Nat).insert 3 |>.insert 1 |>.insert 3

#guard ([3, 1, 3] : List Nat).length == 3
#guard items.size == 2
#guard items.toList.length == 2
```

[`List`](list.md) は順序と重複を保持するが、ハッシュ集合は要素の有無を管理する。`.toList` で列挙できるものの、並び順は前提にできない。順序付きで列挙するなら [`TreeSet`](tree_collections.md) を使う。

[`HashMap α β`](hashmap.md) はキーごとに値 `β` を保持するが、`HashSet α` は要素だけを保持する。要素の型には `[BEq α]` と `[Hashable α]` が必要である。

重複を数えず、登録した要素を正しく検索するためには、`==` が反射的・対称的・推移的な同値関係であり、`a == b` が `true` なら `hash a = hash b` になる必要がある。これは `EquivBEq` と `LawfulHashable` が表す性質である。型クラスの実装が存在するだけでは、この性質は保証されない。詳しくは[ハッシュマップの注意点](hashmap.md#キーに必要な操作と注意点)を参照。

ここでの集合は有限個の要素を格納するデータ構造である。条件を表す述語 `α → Prop` とは役割が違う。

参照：[公式 API：HashSet](https://lean-lang.org/doc/api/Std/Data/HashSet/Basic.html#Std.HashSet)。

[基本データ型の一覧に戻る](README.md)
