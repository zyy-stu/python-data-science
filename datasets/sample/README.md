# 教学模拟数据

本数据为自行生成的虚构记录，不含真实用户。格式为 UTF-8 CSV，首行为字段名，金额单位为分。

| 文件 | 字段说明 |
| --- | --- |
| [users.csv](users.csv) | user_id 为用户编号，region 为地区 |
| [orders.csv](orders.csv) | order_id 为订单编号，user_id 关联用户 |
| [products.csv](products.csv) | product_id 为商品编号，name 为名称，price_cents 为目录价 |
| [sales.csv](sales.csv) | sale_id 为销售记录编号，order_id 为订单编号，user_id 为用户编号，product_id 为商品编号，date 为销售日期，quantity 为件数，unit_price_cents 为成交单价 |

销售表保留一条重复 S2 和 S3 的缺失数量，用于演示清洗。可从仓库根目录用 `pd.read_csv("datasets/sample/sales.csv", encoding="utf-8")` 读取。
