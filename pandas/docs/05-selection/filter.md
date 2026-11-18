# DS-014 条件筛选

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

比较表达式生成布尔 Series。用 &、| 和 ~ 组合条件，每个比较加括号。筛选结果保留原行索引。

## 完整代码与运行

打开[完整脚本](../../examples/04-filtering/main.py)，从仓库根目录运行 `python pandas/examples/04-filtering/main.py`。该脚本中的 `lesson_6()` 执行如下操作：

```python
sales = load('sales')
mask = (sales['quantity'] >= 2) & (sales['product_id'] == 'P1')
print(sales.loc[mask, 'sale_id'].tolist())
```

## 实测输出

```text
['S1', 'S4']
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

Python 的 and/or 不能组合逐行布尔数组。

## 练习题

筛选数量大于等于 2 或商品为 P2 的记录。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[添加、修改与删除](../03-dataframe/mutation.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
