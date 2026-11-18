# DS-009 Pandas 入门

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

Pandas 用带标签的 Series 和 DataFrame 表达表格，可读入 CSV 后选择、清洗、汇总。

## 完整代码与运行

打开[完整脚本](../../examples/02-dataframe/main.py)，从仓库根目录运行 `python pandas/examples/02-dataframe/main.py`。该脚本中的 `lesson_1()` 执行如下操作：

```python
orders = load('orders')
print(orders.shape, orders.columns.tolist())
```

## 实测输出

```text
(4, 2) ['order_id', 'user_id']
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

索引标签和业务主键是不同概念。

## 练习题

输出 orders 中不同用户数。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[Series 基础](../02-series/series.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
