`rcases` は、仮定にある帰納型の値を、コンストラクターの構造に従って分解する tactic である。

例えば、

```text
h : ∃ x, P x
```

に対して、

```text
rcases h with ⟨x, hx⟩
```

と書くと、

```text
x  : α
hx : P x
```

を取り出せる。

入れ子の構造も一度に分解できる。

```text
h : ∃ x, P x ∧ Q x
```

なら、

```text
rcases h with ⟨x, hp, hq⟩
```

として、

```text
x  : α
hp : P x
hq : Q x
```

を得られる。

論理和のように複数のコンストラクターがある場合は `|` で場合分けする。

```text
h : (P ∧ Q) ∨ (R ∧ S)

rcases h with ⟨hp, hq⟩ | ⟨hr, hs⟩
```

これは左の場合と右の場合に分け、それぞれの中身も同時に分解する。

つまり、

```text
rcases h with ⟨x₁, x₂, ...⟩ | ⟨y₁, y₂, ...⟩ | ...
```

では、

- `|` がコンストラクターごとの場合分け
- `⟨...⟩` がその中身の分解

を表す。

`rcases` は、複数回の `cases` をパターンでまとめて書くための tactic と考えるとよい。