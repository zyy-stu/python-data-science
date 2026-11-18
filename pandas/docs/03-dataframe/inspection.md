# DS-012 查看 DataFrame

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

head 看样本，shape 看规模，dtypes 看推断类型，info 统计字段与非空情况，describe 快速检查数值分布。

## 完整代码与运行

打开[完整脚本](../../examples/02-dataframe/main.py)，从仓库根目录运行 `python pandas/examples/02-dataframe/main.py`。该脚本中的 `lesson_4()` 执行如下操作：

```python
sales = load('sales')
print(sales.head(2)['sale_id'].tolist())
print(sales.shape, sales['quantity'].dtype)
print(int(sales['quantity'].describe()['count']))
```

## 实测输出

```text
['S1', 'S2']
(5, 7) float64
4
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

样本行不能证明整列没有异常。

## 练习题

检查 quantity 的 dtype 与缺失数。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[loc 与 iloc](../05-selection/loc-iloc.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
