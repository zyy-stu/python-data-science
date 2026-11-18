# DS-016 缺失值

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

isna 识别缺失；dropna 适用于不能参与分析的行，fillna 需要合适的业务默认值。缺失数量不能直接解释为零。

## 完整代码与运行

打开[完整脚本](../../examples/05-cleaning/main.py)，从仓库根目录运行 `python pandas/examples/05-cleaning/main.py`。该脚本中的 `lesson_8()` 执行如下操作：

```python
sales = load('sales')
print(int(sales['quantity'].isna().sum()))
print(len(sales.dropna(subset=['quantity'])))
print(sales['quantity'].fillna(0).astype(int).tolist())
```

## 实测输出

```text
1
4
[2, 1, 1, 0, 3]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

检查缺失用 isna，避免与 NaN 直接作相等比较。

## 练习题

比较删除与填零后的行数，写清各自的假设。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[重复数据](../06-data-cleaning/duplicates.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
