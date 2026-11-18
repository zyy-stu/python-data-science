# DS-018 groupby 分组

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

groupby 将数据拆组，agg 对每组汇总，结果再合并。指定聚合列与指标，避免把标识符误当数值。

## 完整代码与运行

打开[完整脚本](../../examples/06-groupby/main.py)，从仓库根目录运行 `python pandas/examples/06-groupby/main.py`。该脚本中的 `lesson_10()` 执行如下操作：

```python
sales = load('sales').drop_duplicates('sale_id').dropna(subset=['quantity'])
counts = sales.groupby('product_id')['quantity'].sum().astype(int)
print(counts.to_dict())
```

## 实测输出

```text
{'P1': 5, 'P2': 1}
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

count 忽略缺失，size 计入组内全部行。

## 练习题

按用户分组，计算不同销售号的数量。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[merge 数据合并](../09-merge-join/merge.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
