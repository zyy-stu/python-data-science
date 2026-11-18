# DS-017 重复数据

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

duplicated 返回重复位置，drop_duplicates 依据指定列保留一条。业务主键与全行是否完全相同是两种标准。

## 完整代码与运行

打开[完整脚本](../../examples/05-cleaning/main.py)，从仓库根目录运行 `python pandas/examples/05-cleaning/main.py`。该脚本中的 `lesson_9()` 执行如下操作：

```python
sales = load('sales')
print(sales.loc[sales.duplicated(subset='sale_id'), 'sale_id'].tolist())
print(len(sales.drop_duplicates(subset='sale_id')))
```

## 实测输出

```text
['S2']
4
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

同键字段冲突时，先核对来源再决定保留规则。

## 练习题

找出重复销售号并比较两条原始记录。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[groupby 分组](../08-groupby/groupby.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
