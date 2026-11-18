# DS-011 DataFrame 基础

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

DataFrame 的行列都有标签，各列可有不同 dtype。从 CSV 或等长列构造表。单列选择返回 Series，列清单选择返回 DataFrame。

## 完整代码与运行

打开[完整脚本](../../examples/02-dataframe/main.py)，从仓库根目录运行 `python pandas/examples/02-dataframe/main.py`。该脚本中的 `lesson_3()` 执行如下操作：

```python
users = load('users')
print(users[['user_id', 'region']].to_dict('records'))
print(type(users['region']).__name__, type(users[['region']]).__name__)
```

## 实测输出

```text
[{'user_id': 'U1', 'region': '华东'}, {'user_id': 'U2', 'region': '华北'}, {'user_id': 'U3', 'region': '华东'}]
Series DataFrame
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

用双层方括号保留二维结果。

## 练习题

交换两列的顺序并检查列名。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[查看 DataFrame](../03-dataframe/inspection.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
