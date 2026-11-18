"""groupby 分组示例。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_10() -> None:
    """groupby 分组。"""
    sales = load("sales").drop_duplicates("sale_id").dropna(subset=["quantity"])
    counts = sales.groupby("product_id")["quantity"].sum().astype(int)
    print(counts.to_dict())


if __name__ == "__main__":
    lesson_10()
