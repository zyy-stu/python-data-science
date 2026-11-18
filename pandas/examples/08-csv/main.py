"""读取与保存 CSV示例。"""

from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "datasets" / "sample"


def load(table: str) -> pd.DataFrame:
    """读取仓库中的教学表。"""
    return pd.read_csv(DATA / f"{table}.csv", encoding="utf-8")


def lesson_12() -> None:
    """读取与保存 CSV。"""
    users = load("users")
    with TemporaryDirectory() as tmp:
        output = Path(tmp) / "users.csv"
        users.to_csv(output, index=False, encoding="utf-8")
        restored = pd.read_csv(output, dtype={"user_id": "string"})
        print(restored.columns.tolist(), restored["user_id"].tolist())


if __name__ == "__main__":
    lesson_12()
