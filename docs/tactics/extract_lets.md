# `extract_lets`

`extract_lets` は、**式の中にある `let` を、局所定義として外へ取り出す**タクティクスである。

ゴールに埋め込まれた値に名前を付けて、以後の証明で扱えるようにする。

```lean
example : (let n : Nat := 3; n = 3) := by
  extract_lets n
  rfl
```

取り出した後は、概ね次の状態になる。

```text
n : Nat := 3
⊢ n = 3
```

`extract_lets x y` と名前を指定できる。仮定を対象にするなら `extract_lets n at h` と書く。

`lift_lets` は式の奥にある `let` を式の外側へ移し、`extract_lets` はそれを局所定義として取り出すために使う。

参照：[Lean 4.34.1 の構文・実装](https://github.com/leanprover/lean4/tree/v4.34.1/src/Lean/Elab/Tactic)。

[タクティクス一覧に戻る](README.md)
