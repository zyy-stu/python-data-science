# 参考答案

从仓库根目录执行 `python pandas/exercises/solutions/main.py`，将逐题校验答案。

## 基础题

### 1. 读取用户表行数

使用 `len(users)` 将题目要求转成数组或表格操作。预期为 `3`。先尝试手算，再核对结果和形状。

### 2. 取用户表的地区列名

使用 `users["region"].name` 将题目要求转成数组或表格操作。预期为 `"region"`。先尝试手算，再核对结果和形状。

### 3. 提取前两位用户编号

使用 `users.head(2)["user_id"].tolist()` 将题目要求转成数组或表格操作。预期为 `["U1", "U2"]`。先尝试手算，再核对结果和形状。

### 4. 按标签获取 U2 的地区

使用 `users.set_index("user_id").loc["U2", "region"]` 将题目要求转成数组或表格操作。预期为 `"华北"`。先尝试手算，再核对结果和形状。

### 5. 取最后一行的用户编号

使用 `users.iloc[-1]["user_id"]` 将题目要求转成数组或表格操作。预期为 `"U3"`。先尝试手算，再核对结果和形状。

### 6. 筛选华东用户编号

使用 `users.loc[users["region"].eq("华东"), "user_id"].tolist()` 将题目要求转成数组或表格操作。预期为 `["U1", "U3"]`。先尝试手算，再核对结果和形状。

### 7. 只保留用户编号列并检查列名

使用 `users[["user_id"]].columns.tolist()` 将题目要求转成数组或表格操作。预期为 `["user_id"]`。先尝试手算，再核对结果和形状。

### 8. 删除地区列并检查列数

使用 `users.drop(columns="region").shape[1]` 将题目要求转成数组或表格操作。预期为 `1`。先尝试手算，再核对结果和形状。

### 9. 添加活动标志列并统计真值数量

使用 `int(users.assign(active=True)["active"].sum())` 将题目要求转成数组或表格操作。预期为 `3`。先尝试手算，再核对结果和形状。

### 10. 价格索引反转后与原有 Series 相加

使用 `(prices + prices.iloc[::-1]).tolist()` 将题目要求转成数组或表格操作。预期为 `[24000, 16000]`。先尝试手算，再核对结果和形状。

## 理解题

### 11. 统计原始销售表缺失数量

使用 `int(sales["quantity"].isna().sum())` 将题目要求转成数组或表格操作。预期为 `1`。先尝试手算，再核对结果和形状。

### 12. 删除数量缺失后统计行数

使用 `len(sales.dropna(subset=["quantity"]))` 将题目要求转成数组或表格操作。预期为 `4`。先尝试手算，再核对结果和形状。

### 13. 用 0 填充缺失数量并读取整型列表

使用 `sales["quantity"].fillna(0).astype(int).tolist()` 将题目要求转成数组或表格操作。预期为 `[2, 1, 1, 0, 3]`。先尝试手算，再核对结果和形状。

### 14. 找出重复的销售号

使用 `sales.loc[sales.duplicated("sale_id"), "sale_id"].tolist()` 将题目要求转成数组或表格操作。预期为 `["S2"]`。先尝试手算，再核对结果和形状。

### 15. 按销售号去重后统计记录数

使用 `len(sales.drop_duplicates("sale_id"))` 将题目要求转成数组或表格操作。预期为 `4`。先尝试手算，再核对结果和形状。

### 16. 按地区统计用户数

使用 `users.groupby("region").size().to_dict()` 将题目要求转成数组或表格操作。预期为 `{"华东": 2, "华北": 1}`。先尝试手算，再核对结果和形状。

## 实战题

### 17. 按商品统计清洗后件数

使用 `clean.groupby("product_id")["quantity"].sum().astype(int).to_dict()` 将题目要求转成数组或表格操作。预期为 `{"P1": 5, "P2": 1}`。先检查输入形状或列类型，再比较聚合或筛选结果。

### 18. 左连接订单与用户并检查行数

使用 `len(orders.merge(users, on="user_id", how="left", validate="many_to_one"))` 将题目要求转成数组或表格操作。预期为 `4`。先检查输入形状或列类型，再比较聚合或筛选结果。

### 19. 标记两件及以上的键盘销售记录

使用 `sales.loc[sales["quantity"].ge(2) & sales["product_id"].eq("P1"), "sale_id"].tolist()` 将题目要求转成数组或表格操作。预期为 `["S1", "S4"]`。先检查输入形状或列类型，再比较聚合或筛选结果。

### 20. 导出用户表到 CSV 文本再读取地区列

使用 `pd.read_csv(StringIO(users.to_csv(index=False)))["region"].tolist()` 将题目要求转成数组或表格操作。预期为 `["华东", "华北", "华东"]`。先检查输入形状或列类型，再比较聚合或筛选结果。

[返回练习](../questions/README.md)
