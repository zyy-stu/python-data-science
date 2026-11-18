"""缺失值、重复数据示例。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_8() -> None:
    """缺失值。"""
    sales = load("sales")
    print(int(sales["quantity"].isna().sum()))
    print(len(sales.dropna(subset=["quantity"])))
    print(sales["quantity"].fillna(0).astype(int).tolist())


def lesson_9() -> None:
    """重复数据。"""
    sales = load("sales")
    print(sales.loc[sales.duplicated(subset="sale_id"), "sale_id"].tolist())
    print(len(sales.drop_duplicates(subset="sale_id")))


if __name__ == "__main__":
    lesson_8()
    lesson_9()
