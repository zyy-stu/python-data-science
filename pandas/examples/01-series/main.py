"""Series 基础示例。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_2() -> None:
    """Series 基础。"""
    prices = load("products").set_index("product_id")["price_cents"]
    print(prices.loc["P1"], prices.index.tolist())
    print((prices + prices.iloc[::-1]).tolist())


if __name__ == "__main__":
    lesson_2()
