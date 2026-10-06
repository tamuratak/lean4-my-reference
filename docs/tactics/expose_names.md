# `expose_names`

`expose_names` は、仮定の内部名を、証明から参照できる名前にするタクティクスである。

名前を付けずに導入した仮定を、後から参照したいときに使う。

```lean
import Std.Tactic

example (P : Prop) : P → P := by
  intro
  expose_names
  assumption
```

生成された名前はエディターの証明状態で確認できる。自分で分かりやすい名前を選びたい場合は `rename_i hp` の方が適している。

`expose_names` は、既に導入されている参照不能な名前を公開する。一方、`unhygienic` は内側のタクティクスがこれから自動生成する名前を、証明から参照できる通常の名前として導入するようにする。

```lean
import Std.Tactic

example : ∀ x : Nat, x = x := by
  unhygienic
    intro
    exact Eq.refl x
```

通常の `intro` では、名前を指定しなかった `x` は自動生成名として表示され、そのまま `exact Eq.refl x` とは書けない。この例では `unhygienic` の内側で導入するので、`x` を参照できる。

自動生成名はタクティクスの実装や周囲の名前に左右されるため、それに依存する証明は壊れやすい。通常の証明では `intro x` や `rename_i` で明示的に名前を付ければ十分である。

参照：[公式 API：`expose_names`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.exposeNames)、[公式 API：`unhygienic`](https://lean-lang.org/doc/api/Init/Tactics.html#Lean.Parser.Tactic.tacticUnhygienic_)。

[タクティクス一覧に戻る](README.md)
