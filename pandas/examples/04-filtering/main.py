"""条件筛选示例。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_6() -> None:
    """条件筛选。"""
    sales = load("sales")
    mask = (sales["quantity"] >= 2) & (sales["product_id"] == "P1")
    print(sales.loc[mask, "sale_id"].tolist())


if __name__ == "__main__":
    lesson_6()
