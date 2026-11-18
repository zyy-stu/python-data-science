# DS-019 merge 数据合并

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

merge 按键合并，left 保留左表所有行，inner 只保留匹配行。validate 校验基数，避免重复维表键导致事实行膨胀。

## 完整代码与运行

打开[完整脚本](../../examples/07-merge/main.py)，从仓库根目录运行 `python pandas/examples/07-merge/main.py`。该脚本中的 `lesson_11()` 执行如下操作：

```python
orders = load('orders')
users = load('users')
result = orders.merge(users, on='user_id', how='left', validate='many_to_one')
print(result[['order_id', 'region']].to_dict('records'))
```

## 实测输出

```text
[{'order_id': 'O1', 'region': '华东'}, {'order_id': 'O2', 'region': '华北'}, {'order_id': 'O3', 'region': '华东'}, {'order_id': 'O4', 'region': '华东'}]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

两边键 dtype 需要相容，缺失键的匹配语义也应检查。

## 练习题

构造一个未匹配的用户号，观察 left 和 inner 的区别。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[读取与保存 CSV](../11-input-output/csv.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
