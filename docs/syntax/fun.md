# `fun … => …`・`(· + 1)`

`fun x => 本体` は、名前を登録せず、その場で関数を作る構文である。

```lean
def addOne : Nat → Nat := fun x => x + 1

example : (fun x : Nat => x + 1) 3 = 4 := rfl
example : addOne 3 = 4 := rfl
```

`x` はこの関数の入力を表す。`=>` の右側が、入力から返す値を計算する式である。型は周囲から推論できるが、必要なら `fun (x : Nat) => …` と明示する。

複数の引数は並べて書ける。

```lean
example : (fun (x y : Nat) => x + y) 2 3 = 5 := rfl
example : (fun x : Nat => fun y : Nat => x + y) 2 3 = 5 := rfl
```

この二つは、最初に `x`、次に `y` を受け取る同じ関数である。`=>` の代わりに `↦` も使える。

括弧の中の `·` は、短い匿名関数の引数になる。

```lean
#eval [1, 2, 3].map (· + 1)
example : (· + ·) (2 : Nat) 3 = 5 := rfl
```

`(· + 1)` は `fun x => x + 1`、`(· + ·)` は `fun x y => x + y` に相当する。`#eval` の出力は `[2, 3, 4]` である。

`by` の中でゴールを分けて書く先頭の `·` とは用途が違う。そちらは[タクティクスの複数ゴール構文](../tactics/semicolon.md)を参照。

引数の成分をその場で取り出す `fun (x, y) => …` と、分岐を並べる `fun | … => …` は[パターンを使う `fun`](fun_patterns.md)を参照。

参照：[公式リファレンス：Functions](https://lean-lang.org/doc/reference/latest/Terms/Functions/)。

[文法要素の一覧に戻る](README.md)
