`rcases` は、**仮定にある帰納型の値を、コンストラクターの構造に従って分解する tactic** である。

例えば、

```lean
h : ∃ x, P x
```

に対して、

```lean
rcases h with ⟨x, hx⟩
```

と書くと、

```lean
x  : α
hx : P x
```

を取り出せる。

入れ子の構造も一度に分解できる。

```lean
h : ∃ x, P x ∧ Q x
```

なら、

```lean
rcases h with ⟨x, hp, hq⟩
```

として、

```lean
x  : α
hp : P x
hq : Q x
```

を得られる。

論理和のように複数のコンストラクターがある場合は `|` で場合分けする。

```lean
h : (P ∧ Q) ∨ (R ∧ S)

rcases h with ⟨hp, hq⟩ | ⟨hr, hs⟩
```

これは左の場合と右の場合に分け、それぞれの中身も同時に分解する。

つまり、

```lean
rcases h with ⟨x₁, x₂, ...⟩ | ⟨y₁, y₂, ...⟩ | ...
```

では、

- `|` がコンストラクターごとの場合分け
- `⟨...⟩` がその中身の分解

を表す。

`rcases` は、複数回の `cases` をパターンでまとめて書くための tactic と考えるとよい。