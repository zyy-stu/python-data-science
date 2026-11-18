"""逐题运行并校验参考答案。"""

from io import StringIO
from pathlib import Path

import pandas as pd

data = Path(__file__).resolve().parents[3] / "datasets" / "sample"
users = pd.read_csv(data / "users.csv")
orders = pd.read_csv(data / "orders.csv")
products = pd.read_csv(data / "products.csv")
sales = pd.read_csv(data / "sales.csv")
prices = products.set_index("product_id")["price_cents"]
clean = sales.drop_duplicates("sale_id").dropna(subset=["quantity"])

# 第 1 题
assert len(users) == 3

# 第 2 题
assert users["region"].name == "region"

# 第 3 题
assert users.head(2)["user_id"].tolist() == ["U1", "U2"]

# 第 4 题
assert users.set_index("user_id").loc["U2", "region"] == "华北"

# 第 5 题
assert users.iloc[-1]["user_id"] == "U3"

# 第 6 题
assert users.loc[users["region"].eq("华东"), "user_id"].tolist() == ["U1", "U3"]

# 第 7 题
assert users[["user_id"]].columns.tolist() == ["user_id"]

# 第 8 题
assert users.drop(columns="region").shape[1] == 1

# 第 9 题
assert int(users.assign(active=True)["active"].sum()) == 3

# 第 10 题
assert (prices + prices.iloc[::-1]).tolist() == [24000, 16000]

# 第 11 题
assert int(sales["quantity"].isna().sum()) == 1

# 第 12 题
assert len(sales.dropna(subset=["quantity"])) == 4

# 第 13 题
assert sales["quantity"].fillna(0).astype(int).tolist() == [2, 1, 1, 0, 3]

# 第 14 题
assert sales.loc[sales.duplicated("sale_id"), "sale_id"].tolist() == ["S2"]

# 第 15 题
assert len(sales.drop_duplicates("sale_id")) == 4

# 第 16 题
assert users.groupby("region").size().to_dict() == {"华东": 2, "华北": 1}

# 第 17 题
assert clean.groupby("product_id")["quantity"].sum().astype(int).to_dict() == {"P1": 5, "P2": 1}

# 第 18 题
assert len(orders.merge(users, on="user_id", how="left", validate="many_to_one")) == 4

# 第 19 题
assert sales.loc[sales["quantity"].ge(2) & sales["product_id"].eq("P1"), "sale_id"].tolist() == [
    "S1",
    "S4",
]

# 第 20 题
assert pd.read_csv(StringIO(users.to_csv(index=False)))["region"].tolist() == [
    "华东",
    "华北",
    "华东",
]

print("20 道练习校验通过")
