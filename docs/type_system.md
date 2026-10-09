# Lean 4 の型システムの基礎

Lean では、データ、関数、型、命題、証明を、いずれも型を持つ項（式）として扱う。
`3 : Nat` は自然数の値、`P : Prop` は命題、`h : P` はその命題の証明を表す。
型システムは、項がどの型に属するかを定め、証明が目的の命題の型を持つかを検査する基盤である。

以下では、この基盤とその利用を支える8つの特徴を説明する。
依存型や帰納型は型の構成方法、宇宙階層や証明の無関連性は型検査の規則に関わる。
停止性検査は再帰定義を受理する仕組み、追加公理は証明で利用できる前提であり、それぞれ役割が異なる。

## 1. 依存型

依存型（dependent types）は、値を使って型を指定できる仕組みである。
例えば `Fin n` は、0以上 `n` 未満の自然数を表す型であり、自然数の値 `n` に依存する。
`Fin 5` の値は0から4まで、`Fin 10` の値は0から9までに限られ、両者は異なる型である。
その値は自然数と上限未満である証明を組み合わせて構成するため、範囲の条件が型に含まれる。

関数の結果の型が引数に依存する場合を、依存関数型と呼ぶ。
`(n : Nat) → Fin (n + 1)` は、自然数 `n` を受け取り、その値に応じた `Fin (n + 1)` の値を返す型である。
次の関数は、どの `n` に対しても0を返す。0が `n + 1` 未満である証明も結果に含める。

```lean
def firstIndex (n : Nat) : Fin (n + 1) :=
  ⟨0, Nat.zero_lt_succ n⟩

example : (firstIndex 4).val = 0 := rfl
example : Fin 5 := firstIndex 4
```

`firstIndex 4` の型は `Fin (4 + 1)` であり、計算によって `Fin 5` として使える。
このように、Lean の型検査では定義を展開した計算も使い、型が一致するかを判定する。
依存型は、配列の添字や長さの条件を型に組み込むだけでなく、対象ごとに異なる命題の証明を返す関数にも使われる。

関連：[関数型](syntax/function_types.md)、[`Fin`](basic-types/fin.md)。
参照：[公式リファレンス：Functions](https://lean-lang.org/doc/reference/latest/The-Type-System/Functions/)。

## 2. 帰納型

帰納型（inductive types）は、コンストラクターによって値の構成方法を指定する型である。
Lean では `inductive` で宣言し、各コンストラクターがどの引数から値を作るかを定める。
例えば `Nat` には、ゼロを作る `Nat.zero` と、自然数からその次の自然数を作る `Nat.succ` がある。
自然数の2は `Nat.succ (Nat.succ Nat.zero)` に対応する。

帰納型の宣言からは、値を分解して計算や証明を行うための再帰子（recursor）が生成される。
`Nat.rec` は、ゼロの場合の結果と、`n` の結果から `n + 1` の結果を作る規則を受け取る。
次の例では、ゼロの場合に0を返し、次の自然数ではそれまでの結果に2を加える。

```lean
def doubleNat (n : Nat) : Nat :=
  Nat.rec 0 (fun _ previous => previous + 2) n

example : doubleNat 3 = 6 := rfl
```

再帰子が返す型を命題にすれば、同じ仕組みが数学的帰納法になる。
ゼロの場合の証明と、`n` での証明から `n + 1` での証明を作る規則により、すべての自然数について証明できる。
普段の `match` や `induction` は、この計算・証明の原理を使いやすく記述するための構文やタクティクスである。
帰納型には再帰的な出現に関する正値性などの条件があり、任意の自己参照を許すわけではない。

関連：[`inductive`](syntax/inductive.md)、[`induction`](tactics/induction.md)。
参照：[公式リファレンス：Inductive Types](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/)。

## 3. 命題と型の対応

命題と型の対応（Curry–Howard correspondence）は、命題を型として、その証明をその型の項として表現する考え方である。
Lean では `P : Prop` が命題を表し、`h : P` がその証明を表す。
証明するという操作は、目的の命題の型を持つ項を構成することに当たる。
例えば含意 `P → Q` の証明は、`P` の証明を受け取り、`Q` の証明を返す関数である。

```lean
example (P Q : Prop) (hp : P) (hpq : P → Q) : Q :=
  hpq hp

example (P Q : Prop) (hp : P) (hq : Q) : P ∧ Q :=
  And.intro hp hq
```

最初の例では、`hpq` に `hp` を渡すことで `Q` の証明を得る。
二つ目の例では、論理積 $P \land Q$ のコンストラクター `And.intro` に両方の証明を渡す。
論理和 $P \lor Q$ はどちらか一方の証明、存在命題 $\exists x,\ P(x)$ は対象とその性質の証明から構成する。

全称命題 $\forall x,\ P(x)$ の証明は、各 `x` に対して `P x` の証明を返す依存関数である。
タクティクスで書いた証明も、最終的にはこうした項に変換される。
Lean のカーネルは、その項の型を検査することで、宣言した前提や公理のもとで証明が正しいかを確認する。

関連：[論理の記号](syntax/logical_symbols.md)、[型による数学的対象の構成と性質の証明](mathematical_constructions.md)。
参照：[公式リファレンス：Propositions](https://lean-lang.org/doc/reference/latest/The-Type-System/Propositions/)。

## 4. 宇宙階層

宇宙（universe）は、型そのものを分類する型である。
`Nat : Type 0`、`Type 0 : Type 1`、`Type 1 : Type 2` のように、型にも上位の型があり、この階層はさらに上へ続く。
`Type` は `Type 0` の省略形である。
すべての型を「自分自身も含む一つの型」にまとめることで起こる矛盾を避けるため、階層を区別する。

一般的な記法は `Sort u` であり、`Prop` は `Sort 0`、`Type u` は `Sort (u + 1)` に対応する。
`Prop` は特別な宇宙で、任意の階層の対象について量化しても、結果の命題は `Prop` に属する。
例えば「任意の型の任意の値は自分自身に等しい」という命題も `Prop` に属する。

```lean
universe u

example : Prop := ∀ (A : Type u) (x : A), x = x

def keepValue {A : Type u} (x : A) : A := x

example : keepValue (3 : Nat) = 3 := rfl
example : keepValue Nat = Nat := rfl
```

`universe u` は、階層を固定せずに定義するための宇宙変数を宣言する。
`keepValue` は、自然数の値にも、型そのものにも使える宇宙多相な関数である。
一方、Lean の宇宙階層は非累積的であり、`Nat : Type 0` をそのまま `Nat : Type 1` として使うことはできない。
異なる階層で共通の定義を使う宇宙多相と、型を上位の階層へ包み直す `ULift` は、別の仕組みである。

関連：[`Prop`・`Type`・`Sort`・`universe`](syntax/universes.md)。
参照：[公式リファレンス：Universes](https://lean-lang.org/doc/reference/latest/The-Type-System/Universes/)。

## 5. 証明の無関連性

証明の無関連性（proof irrelevance）は、同じ命題に対する証明どうしを、型検査で区別しない性質である。
データ型 `Nat` の値1と2は異なるが、`P : Prop` の証明 `h1 : P` と `h2 : P` は定義上等しいものとして扱われる。
「定義上等しい」とは、別の等式の証明を使わず、型検査の規則によって等しいと判定されることをいう。
Lean では証明の無関連性がその規則に含まれるため、次の等式は `rfl` で証明できる。

```lean
example (P : Prop) (h1 h2 : P) : h1 = h2 := rfl

example (h1 h2 : 1 < 5) :
    (⟨1, h1⟩ : Fin 5) = ⟨1, h2⟩ := rfl
```

二つ目の例では、`Fin 5` に格納した自然数が同じなら、上限未満である証明の書き方が違っても値は定義上等しい。
この性質は証明の内容を比較する手間を省くが、異なる命題そのものを等しくする規則ではない。
論理的な同値の証明から命題の等しさを導くには、後述する `propext` を使う。

証明を通常の計算データとして区別しないため、`Prop` の帰納型を分解して `Type` のデータを取り出す操作には制限がある。
例えば存在命題の証明から、その対象を一般に計算可能な方法で取り出すことはできない。一方、`False` の除去などには例外がある。
コンパイル時には証明が消去されるので、範囲の証明を含む `Fin` などを使っても、証明自体を実行時データとして保持する必要はない。

参照：[公式リファレンス：Propositions](https://lean-lang.org/doc/reference/latest/The-Type-System/Propositions/)。

## 6. 再帰定義の停止性

停止性検査（termination checking）は、通常の再帰定義が無限に自分自身を呼び出さないことを確認する仕組みである。
無制限の再帰を証明に許すと、`False` の証明を作る関数が自分自身を呼ぶだけで、矛盾を導けてしまう。
Lean は再帰定義を、カーネルが受理できる再帰子などを使った項に変換する。
停止性は、この変換によって再帰関数を論理体系に組み込むための条件になる。

基本となる構造的再帰では、コンストラクターの構成要素へ再帰する。
次の関数は、`n + 1` の場合に、その構成要素である `n` に対して再帰する。
自然数を構成する `Nat.succ` を一つずつ取り除くため、最後は0の場合に到達する。

```lean
def sumTo : Nat → Nat
  | 0 => 0
  | n + 1 => sumTo n + (n + 1)

example : sumTo 3 = 6 := rfl
```

構造的再帰で表せない場合には、無限に下降できない関係を使う整礎再帰（well-founded recursion）を利用できる。
`termination_by` で減少する尺度などを指定し、必要なら `decreasing_by` で各再帰呼び出しの減少を証明する。
停止性の証明を要求しない `partial def` もあるが、戻り値の型に値が存在することが必要で、カーネルはその本体を展開しない。
`partial def` の実行時の計算はコンパイラが扱い、証明の型検査で使う計算とは区別される。

関連：[再帰定義](syntax/recursive.md)。
参照：[公式リファレンス：Recursive Definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/)。

## 7. 商型

商型（quotient types）は、指定した同値関係で結び付く値を同じものとして扱うための型である。
例えば自然数を3で割った余りで分類すると、1と4は同じ類に入り、余り0・1・2に対応する3つの類ができる。
Lean では、関係とその反射性・対称性・推移性の証明を `Setoid` にまとめ、`Quotient` に渡す。
`Quotient.mk` は元の値から商型の値を作り、`Quotient.sound` は関係が成り立つことから商型での等式を導く。

```lean
def sameRemainder : Setoid Nat where
  r a b := a % 3 = b % 3
  iseqv := ⟨fun _ => rfl, fun h => h.symm, fun h1 h2 => h1.trans h2⟩

def residue (n : Nat) : Quotient sameRemainder :=
  Quotient.mk sameRemainder n

example : residue 1 = residue 4 :=
  Quotient.sound (by decide : 1 % 3 = 4 % 3)

def remainder (q : Quotient sameRemainder) : Nat :=
  Quotient.lift (fun n => n % 3) (fun _ _ h => h) q

example : remainder (residue 4) = 1 := rfl
```

1と4という代表元が定義上等しくなるわけではなく、商型の値の等しさを命題として証明している。
商型から関数を定義する `Quotient.lift` には、同じ類の代表元から等しい結果を返すことの証明が必要になる。
この例の余りはその条件を満たし、代表元から作った値への適用は計算で簡約できる。

基礎となる `Quot` の構成・除去・計算規則はカーネルが扱い、関係から等式を導く `Quot.sound` は標準の公理である。
`Quotient` はこの仕組みを同値関係向けにまとめたもので、整数や有理数などを代表元によって構成する方法に使える。
条件を満たす値を選ぶ部分型に対し、商型は元の値どうしを同一視する点が異なる。

関連：[商型](basic-types/quotient.md)、[部分型](syntax/subtype.md)。
参照：[公式リファレンス：Quotients](https://lean-lang.org/doc/reference/latest/The-Type-System/Quotients/)。

## 8. 追加公理と古典論理

公理は、定義本体を持たずに導入される型付きの定数であり、その型が命題なら、その命題の証明として使える。
Lean の標準の数学的な公理には、前節の `Quot.sound` に加え、命題の外延性 `propext` と選択公理 `Classical.choice` がある。
`propext` は、論理的に同値な命題を、命題として等しいとする公理である。
例えば $P \leftrightarrow Q$ の証明から `P = Q` を得られるが、これは定義上の等しさを追加するものではない。

```lean
example (P Q : Prop) (h : P ↔ Q) : P = Q :=
  propext h

noncomputable def chooseElement {A : Type} (h : Nonempty A) : A :=
  Classical.choice h

theorem excludedMiddle (P : Prop) : P ∨ ¬ P :=
  Classical.em P

#print axioms excludedMiddle
```

`Nonempty A` は「`A` に値が存在する」という命題であり、`Classical.choice` はその証明から `A` の値を選び出す。
証明を分解して対象を計算する通常の操作とは異なり、この選択には一般に実行可能な計算手順がない。
そのため、選んだ値をデータとして使う `chooseElement` には `noncomputable` が必要になる。

これらの標準公理を使って排中律 $P \lor \neg P$ を導け、その定理が `Classical.em` である。
`#print axioms excludedMiddle` で、証明が依存する `propext`・`Classical.choice`・`Quot.sound` を確認できる。
公理を証明の中で使うだけなら、必ずしもデータを計算できなくなるわけではない。
公理は証明の前提なので、型検査が保証する正しさもそれらを前提としたものであり、任意に追加した公理の整合性まで Lean が確認するわけではない。

関連：[`opaque`・`axiom`](syntax/opaque_axiom.md)、[`noncomputable`](syntax/noncomputable.md)、[`#print`](commands/print.md)。
参照：[公式リファレンス：Axioms](https://lean-lang.org/doc/reference/latest/Axioms/)。

[リファレンスのトップに戻る](../README.md)
