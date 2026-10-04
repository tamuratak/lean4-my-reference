# 追加ライブラリのタクティクス

ここでは **Lean 本体に同梱されない、追加ライブラリのタクティクス**を説明する。Lean 本体・`Std` の操作は[標準タクティクス一覧](../tactics/README.md)に置き、ここには混ぜない。

- [mathlib4 のタクティクス](mathlib/README.md)：数値計算、多項式、不等式、論理、式変形、有限な場合分け。
- [Aesop のタクティクス](aesop/README.md)：論理の操作や補題の適用を組み合わせる証明探索と、探索規則の追加。

mathlib4 は数学の定義・定理と多くのタクティクスを含むライブラリである。Aesop は証明探索のパッケージで、mathlib4 の依存にも含まれる。mathlib を使うプロジェクトでも、`aesop` の提供元は Aesop と区別する。

## やりたいことから選ぶ

| やりたいこと | 提供元と候補 |
| --- | --- |
| 数値だけの等式・不等式を計算する | mathlib：[norm_num](mathlib/norm_num.md) |
| 多項式の等式を展開・整理して証明する | mathlib：[ring](mathlib/ring.md) |
| 仮定やゴールの多項式を標準形にする | mathlib：[ring_nf](mathlib/ring_nf.md) |
| 線形な等式・不等式を組み合わせる | mathlib：[linarith](mathlib/linarith.md) |
| 平方や積も利用して不等式を証明する | mathlib：[nlinarith](mathlib/nlinarith.md) |
| 式が正・非負・非零であることを示す | mathlib：[positivity](mathlib/positivity.md) |
| 分母を払ってから等式を証明する | mathlib：[field_simp](mathlib/field_simp.md) |
| 論理構造を自動で分解して証明する | mathlib：[tauto](mathlib/tauto.md)、Aesop：[aesop](aesop/aesop.md) |
| 補題を登録して探索に使わせる | Aesop：[規則の追加](aesop/rules.md) |

## 標準との境界

提供元は **このリファレンスで対象にする Lean のバージョン**を基準にする。過去に mathlib で提供されていた名前でも、現在は本体に移っているものがある。

| 名前 | このリファレンスでの扱い |
| --- | --- |
| `rcases`・`rintro`・`obtain`・`omega`・`grind` | Lean 本体。標準タクティクス側に置く |
| `norm_cast`・`push_cast`・`exact_mod_cast` | Lean 本体。mathlib では追加の型や補題も利用できる |
| `ext`・`simp` | 操作自体は Lean 本体。mathlib は利用する補題も追加する |
| `ring`・`linarith`・`norm_num`・`push_neg` | mathlib 側に置く |
| 通常の `by` 証明の `by_contra` | Batteries 由来。mathlib 経由で使う操作として mathlib 側で説明する |
| `aesop`・`aesop?` | Aesop 側に置く |

標準の操作に mathlib の補題が追加されることと、操作自体が追加ライブラリに属することは別である。

## 例の実行と検証

各例は必要な `import` を明示している。コードブロックを一つずつ Lean ファイルにコピーし、依存ライブラリを持つ Lake プロジェクト内で `lake env lean Example.lean` とすれば実行できる。Aesop の例では `import Aesop` だけを使う。

このリポジトリの `lakefile.toml` は mathlib v4.34.0 のコミットを固定し、`lake-manifest.json` はその依存も固定している。Aesop は mathlib が指定する依存を使用する。依存先の既存チェックアウトの状態には依存しない。

初回は、GitHub にアクセスできる環境で依存を取得する。`--keep-toolchain` は対象の Lean 4.34.1 を維持するために付ける。

```sh
lake --keep-toolchain update
```

続いて、例に使うモジュールをビルドする。mathlib v4.34.0 が指定する Lean は 4.34.0 なので、4.34.1 では配布済みキャッシュをそのまま使えるとは限らない。ここではソースからのビルドを前提とする。

```sh
lake build Mathlib.Data.Real.Basic Mathlib.Data.Int.Order.Basic Mathlib.Data.Fintype.Fin \
  Mathlib.Tactic.Ring Mathlib.Tactic.NormNum Mathlib.Tactic.Linarith \
  Mathlib.Tactic.Positivity Mathlib.Tactic.FieldSimp Mathlib.Tactic.Abel \
  Mathlib.Tactic.LinearCombination Mathlib.Tactic.Push Mathlib.Tactic.ByContra \
  Mathlib.Tactic.Contrapose Mathlib.Tactic.Convert Mathlib.Tactic.CongrExclamation \
  Mathlib.Tactic.GCongr Mathlib.Tactic.FinCases Mathlib.Tactic.IntervalCases \
  Mathlib.Tactic.Choose Mathlib.Tactic.Tauto Aesop
python3 scripts/check_examples.py
```

標準ページは従来どおり `lean` で検証し、`Mathlib` または `Aesop` をインポートする例だけを `lake env lean` に渡す。追加ライブラリの例には共通インポートを補わない。

既に依存をビルドした別の Lake プロジェクトを使う場合は、パスを指定できる。ただし Lean のバージョンはリポジトリと一致する必要がある。

```sh
python3 scripts/check_examples.py --library-project /path/to/project docs/library-tactics/mathlib/ring.md
```

- `lean`：穴のない証明・定義。自動検証の対象。
- `text`：仮定・ゴールの表示など、説明用の断片。
- `lean-incomplete`：仮の穴を残した操作例。完成例の検証対象には含めない。

## 検証と参照方針

標準ページの対象は Lean 4.34.1。追加ライブラリの依存は mathlib v4.34.0（`5ed2965256430c3649e86755f9576b54eca72435`）、Aesop はその依存（`355695d523e41d0554926416cba2a2b3544fbbc9`）に固定した。ただし **追加例の Lean 4.34.1 での検証は未完了**である。

作成環境では固定した依存の一部を取得できなかったため、追加例のコンパイルは、手元の mathlib `bc5fddb836ac5f7939c4f017fbafb89edbbd34d0` とその Aesop `a90fbf7b02ff06a0deebf74088dff9e5fe02c9ea`、Lean 4.35.0-rc3 で確認した。これは互換性の追加確認であり、固定バージョンでの成功を意味しない。

異なる Lean バージョンの環境で追加確認を行う場合だけ、`--allow-library-toolchain-mismatch` を明示する。スクリプトはバージョンの違いと、固定バージョンでは未検証であることを表示する。

説明は各ライブラリの宣言の説明・同梱資料と、例の実行結果を確認して作成した。参照リンクは、このリポジトリの方針に従って Lean 公式リファレンスと公式 API に限定する。これらは Lean 本体の資料であり、mathlib・Aesop 固有の仕様を説明する資料としては扱わない。各ページの公式リンクは、標準側の操作や共通概念との比較用である。

- [Lean 公式リファレンス：タクティクス](https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/)
- [Lean 公式 API ドキュメント](https://lean-lang.org/doc/api/)

[リファレンスの入口に戻る](../../README.md)
