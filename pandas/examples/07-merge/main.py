"""merge 数据合并示例。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_11() -> None:
    """merge 数据合并。"""
    orders = load("orders")
    users = load("users")
    result = orders.merge(users, on="user_id", how="left", validate="many_to_one")
    print(result[["order_id", "region"]].to_dict("records"))


if __name__ == "__main__":
    lesson_11()
