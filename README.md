与えられた群の情報を元にその群のデータを求めるスクリプト

# 実行方法
- `python3 app.py`：`group.json` のデータを使う．
- `python3 app.py -i input`：`group.json` の代わりに `input` を使う．

# group.json の記法
二面体群 $D_4$ の例
```json
{
    "order": 8,
    "numOfGenerators": 2,
    "relations": {
        "a": 4,
        "b": 2,
        "ba": [3, 1]
    }
}
```
以下，$i$ 番目のアルファベットを $\sigma_i$ と表すことにする．
- `order`：群の位数．$1$ 以上の整数である必要がある．実行時間的に最大サイズは $20$ 程度．
- `numOfGenerators`：生成元の個数．アルファベットで管理しているため，$1$ 以上 $26$ 以下の整数である必要がある．$i$ 番目の生成元を  $\sigma_i$ と表す．このとき，生成元の個数を $n$ とすると，与えられた群の元は $\sigma_1^{k_1} \sigma_2^{k_2} \cdots \sigma_n^{k_n}$ という形で一意的に表される必要がある．
- `relations`：生成元の関係式．以下の情報を入れる必要がある．
    - $\sigma_i$：生成元の各 $\sigma_i$ の位数を $2$ 以上の整数で与える．また，生成元の取り方の条件より，$order = \mathrm{ord}(\sigma_1) \times \mathrm{ord}(\sigma_2) \times \cdots \times \mathrm{ord}(\sigma_n)$ を満たす必要がある．
    - $\sigma_i \sigma_j \: (i > j)$：この元を $\sigma_1^{k_1} \sigma_2^{k_2} \cdots \sigma_n^{k_n}$ と表した時の $(k_1, k_2, \ldots, k_n)$ を与える．$k_i$ は $0$ 以上 $\mathrm{ord}(\sigma_i)$ 以下である必要がある．

すなわち上の例は，二面体群 $D_4$ を，
$$
    \langle a, b \mid a^4 = b^2 = e, ba = a^3b \rangle
$$
と表した時の情報と対応している．

$\mathbb{Z} / 2\mathbb{Z} \times \mathbb{Z} / 2\mathbb{Z}$ の例
```json
{
    "order": 4,
    "numOfGenerators": 2,
    "relations": {
        "a": 2,
        "b": 2,
        "ba": [1, 1]
    }
}
```
