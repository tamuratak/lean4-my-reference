# `Std.HashMap α β`：ハッシュマップ

`Std.HashMap α β` は、`α` 型のキーから `β` 型の値を探す対応表である。例えば `Std.HashMap String Nat` なら、名前から点数を探せる。標準ライブラリの `import Std.Data.HashMap` を使う。

## マップの作成と値の検索

```lean
import Std.Data.HashMap

def scores : Std.HashMap String Nat :=
  ({} : Std.HashMap String Nat).insert "Alice" 10 |>.insert "Bob" 20

#guard scores.get? "Alice" == some 10
#guard scores.get? "Carol" == none
#guard scores.contains "Bob"
#guard scores.size == 2
```

`{}` は型に応じた空のコレクションを表す。`.insert key value` はキーと値を登録したマップを返す。`.get? key` は見つかれば `some value`、なければ `none` を返すので、結果は [`Option β`](option.md) になる。`.contains` はキーの有無を `Bool`、`.size` は登録されたキーの数を返す。

ここでの [`#guard`](../commands/guard.md) は具体的な計算結果を検査するコマンドであり、一般的な性質の証明を登録するものではない。

## 同じキーの更新と削除

```lean
import Std.Data.HashMap

def original : Std.HashMap String Nat :=
  ({} : Std.HashMap String Nat).insert "Alice" 10

def updated := original.insert "Alice" 30
def removed := updated.erase "Alice"

#guard original.get? "Alice" == some 10
#guard updated.get? "Alice" == some 30
#guard updated.size == 1
#guard removed.get? "Alice" == none
```

既存のキーに `.insert` すると、そのキーに対応する値を置き換える。同じキーで複数の値を保持する操作ではない。`.erase` はキーを削除したマップを返す。どちらも結果のマップを使う必要があり、元の名前の値を代入で変更する記法ではない。

## キーに必要な操作と注意点

キーの型には `[BEq α]`（`==` で比較する実装）と `[Hashable α]`（ハッシュ値を計算する実装）が必要である。`String`・`Nat` には標準の実装がある。自分の型で使う場合、上の更新・検索が期待どおりに動くためには次の二つの性質が必要になる。

- `a == b` が `true` になる関係が、反射的・対称的・推移的な同値関係であること。つまり、自分自身とは同じと判定し、比較の向きを逆にしても結果が変わらず、`a` と `b`、`b` と `c` が同じなら `a` と `c` も同じと判定する。
- `a == b` が `true` なら `hash a = hash b` であること。

これらはそれぞれ `EquivBEq` と `LawfulHashable` が表す性質である。マップを作るだけならこれらの証明は要求されないが、性質を満たさない実装では、同じキーが重複して登録されたり、登録したキーを検索できなかったりする。ハッシュ値の整合性だけでは十分ではない。

ハッシュ値が同じでもキーが同じとは限らない。マップはハッシュ値だけでなくキーの比較も使って区別する。

`.toList` はキーと値のペアのリストを返すが、キー順や挿入順を前提にしてはいけない。キー順で列挙したい場合は [`TreeMap`](tree_collections.md)、値を持たず要素の有無だけを管理したい場合は [`HashSet`](hashset.md) を使う。

参照：[公式 API：HashMap](https://lean-lang.org/doc/api/Std/Data/HashMap/Basic.html#Std.HashMap)。

[基本データ型の一覧に戻る](README.md)
