# `#print`・`#print sig`

`#print 名前` は、登録されている宣言の型と本体などを表示するコマンドである。

```lean
def double (n : Nat) : Nat := n + n

#check double
#print double
```

`#check double` では主に型を確認し、`#print double` では定義の本体も読める。表示は概ね次の形になる。

```text
def double : Nat → Nat :=
fun n => n + n
```

定理も表示できる。

```lean
theorem keepProof (P : Prop) (h : P) : P := by
  exact h

#print keepProof
```

`by` で書いたタクティクスの文字列ではなく、それが作った証明項が表示される。長い証明の場合は、表示される項も大きくなることがある。

`#print sig` は本体を省き、宣言の種類や型を表示する。

```lean
def double (n : Nat) : Nat := n + n

#print sig double
```

`#print` は宣言名を受け取る。任意の式の型なら [`#check`](check.md)、具体的な計算なら [`#eval`](eval.md) を使う。

文字列を直接表示する書き方もある。

```lean
#print "Inspect the next declaration"
```

これは文字列をメッセージとして表示し、`IO` のプログラムを実行するものではない。

依存公理は [`#print axioms`](print_axioms.md)、関数の定義の等式は [`#print equations`](print_equations.md) を参照。

参照：[公式リファレンス：Interacting with Lean](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/)。

[`#` コマンドの一覧に戻る](README.md)
