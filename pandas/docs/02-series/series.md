# DS-010 Series 基础

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

Series 是带索引的一维数据。给索引命名后可按标签取值；两个 Series 运算时按标签对齐。

## 完整代码与运行

打开[完整脚本](../../examples/01-series/main.py)，从仓库根目录运行 `python pandas/examples/01-series/main.py`。该脚本中的 `lesson_2()` 执行如下操作：

```python
prices = load('products').set_index('product_id')['price_cents']
print(prices.loc['P1'], prices.index.tolist())
print((prices + prices.iloc[::-1]).tolist())
```

## 实测输出

```text
12000 ['P1', 'P2']
[24000, 16000]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

不同索引进行运算时，缺失标签可能产生空值。

## 练习题

从价格 Series 中筛选大于 1000 的值。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[DataFrame 基础](../03-dataframe/dataframe.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
