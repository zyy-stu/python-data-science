"""loc 与 iloc示例。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_5() -> None:
    """loc 与 iloc。"""
    users = load("users").set_index("user_id")
    print(users.loc["U1":"U2", "region"].tolist())
    print(users.iloc[:2, 0].tolist())
    print(users.at["U1", "region"], users.iat[0, 0])


if __name__ == "__main__":
    lesson_5()
