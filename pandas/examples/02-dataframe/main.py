"""Pandas 入门、DataFrame 基础、查看 DataFrame、添加、修改与删除示例。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_1() -> None:
    """Pandas 入门。"""
    orders = load("orders")
    print(orders.shape, orders.columns.tolist())


def lesson_3() -> None:
    """DataFrame 基础。"""
    users = load("users")
    print(users[["user_id", "region"]].to_dict("records"))
    print(type(users["region"]).__name__, type(users[["region"]]).__name__)


def lesson_4() -> None:
    """查看 DataFrame。"""
    sales = load("sales")
    print(sales.head(2)["sale_id"].tolist())
    print(sales.shape, sales["quantity"].dtype)
    print(int(sales["quantity"].describe()["count"]))


def lesson_7() -> None:
    """添加、修改与删除。"""
    users = load("users")
    users["active"] = False
    users.loc[users["user_id"].eq("U1"), "active"] = True
    print(users.drop(columns="region")["active"].tolist())


if __name__ == "__main__":
    lesson_1()
    lesson_3()
    lesson_4()
    lesson_7()
