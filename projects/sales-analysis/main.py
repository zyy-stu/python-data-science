"""读取、清洗并分析教学销售数据。"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "datasets" / "sample"


def analyze(data_dir: Path = DATA) -> dict[str, object]:
    """返回质量指标和按商品、用户、月份汇总的销售额。"""
    raw = pd.read_csv(data_dir / "sales.csv", encoding="utf-8")
    products = pd.read_csv(data_dir / "products.csv", encoding="utf-8")
    users = pd.read_csv(data_dir / "users.csv", encoding="utf-8")

    # 全行重复可直接去除，有冲突的业务键需要人工核对。
    sales = raw.drop_duplicates().copy()
    if sales["sale_id"].duplicated().any():
        raise ValueError("销售编号对应多条冲突记录")
    for column in ("quantity", "unit_price_cents"):
        sales[column] = pd.to_numeric(sales[column], errors="coerce")
    sales["date"] = pd.to_datetime(sales["date"], format="%Y-%m-%d", errors="coerce")
    before_cleanup = len(sales)
    sales = sales.dropna(
        subset=["date", "quantity", "unit_price_cents", "product_id", "user_id"]
    ).copy()
    for column in ("quantity", "unit_price_cents"):
        if sales[column].lt(0).any() or sales[column].mod(1).ne(0).any():
            raise ValueError(f"{column} 必须为非负整数")
        sales[column] = sales[column].astype("int64")
    sales["revenue_cents"] = sales["quantity"] * sales["unit_price_cents"]
    sales["month"] = sales["date"].dt.to_period("M").astype(str)
    sales = sales.merge(products[["product_id", "name"]], how="left", validate="many_to_one")
    sales = sales.merge(users, on="user_id", how="left", validate="many_to_one")
    if sales[["name", "region"]].isna().any().any():
        raise ValueError("存在未匹配的商品或用户")

    return {
        "raw_rows": len(raw),
        "duplicates": len(raw) - before_cleanup,
        "incomplete": before_cleanup - len(sales),
        "total_cents": int(sales["revenue_cents"].sum()),
        "product": sales.groupby(["product_id", "name"])["revenue_cents"].sum().to_dict(),
        "user": sales.groupby("user_id")["revenue_cents"].sum().to_dict(),
        "month": sales.groupby("month")["revenue_cents"].sum().to_dict(),
    }


if __name__ == "__main__":
    for metric, value in analyze().items():
        print(f"{metric}: {value}")
