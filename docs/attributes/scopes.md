# 属性の有効範囲：`local`・`scoped`

属性の前の `local`・`scoped` は、**その属性の効果がどこで有効になるか**を指定する。属性によって対応する指定や細かな意味が異なるので、ここでは `simp` を例にする。

## `local`：現在の範囲だけ

```lean
def wrap (n : Nat) : Nat := n

theorem wrap_eq (n : Nat) : wrap n = n := rfl

section
attribute [local simp] wrap_eq

example (n : Nat) : wrap (wrap n) = n := by
  simp
end

example (n : Nat) : wrap n = n := by
  simp only [wrap_eq]
```

セクション内では `simp` が `wrap_eq` を自動で使う。`end` の後では局所的な登録の効果がなくなる。定理は残るので、外でも名前を指定して使える。

宣言と同時に付ける場合は、`@[local simp] theorem ...` と書く。`local` が制限するのは属性の効果であり、宣言の名前の公開範囲を決める `private` とは別である。

## `scoped`：名前空間を開いた場所で

```lean
namespace Wrapping

def wrap (n : Nat) : Nat := n

@[scoped simp] theorem wrap_eq (n : Nat) : wrap n = n := rfl

end Wrapping

section
open scoped Wrapping

example (n : Nat) : Wrapping.wrap (Wrapping.wrap n) = n := by
  simp
end
```

`wrap_eq` の簡単化規則を `Wrapping` のスコープに関連付ける。`open scoped Wrapping` の後では、その規則を通常の `simp` で使える。

`open scoped` はスコープに関連付いた効果を有効にするが、`Wrapping.wrap` のような名前を短くするための操作ではない。そのため例では修飾した名前を使っている。通常の `open Wrapping` でもスコープの効果は有効になり、名前も短く書ける。

## 何も付けない場合

`@[simp]` のように指定がなければ、通常はその登録が以後の環境で有効になり、そのファイルをインポートした側でも利用される。`namespace` の中に書いただけで `scoped` になるわけではない。

| 指定 | `simp` 属性の効果 |
| --- | --- |
| `simp` | 以後の環境と、そのモジュールを読み込んだ側で有効 |
| `local simp` | 現在のセクションや名前空間の範囲だけで有効 |
| `scoped simp` | 関連付いた名前空間の中や、それを開いた範囲で有効 |

参照：[公式リファレンス：Attributes](https://lean-lang.org/doc/reference/latest/Attributes/)、[Namespaces and Sections](https://lean-lang.org/doc/reference/latest/Namespaces-and-Sections/)。

[属性の一覧に戻る](README.md)
