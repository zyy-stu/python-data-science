# DS-013 loc 与 iloc

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

loc 根据标签访问，标签切片通常包含结束标签；iloc 根据从零开始的位置访问，上界排除。at 与 iat 用于标量访问。

## 完整代码与运行

打开[完整脚本](../../examples/03-selection/main.py)，从仓库根目录运行 `python pandas/examples/03-selection/main.py`。该脚本中的 `lesson_5()` 执行如下操作：

```python
users = load('users').set_index('user_id')
print(users.loc['U1':'U2', 'region'].tolist())
print(users.iloc[:2, 0].tolist())
print(users.at['U1', 'region'], users.iat[0, 0])
```

## 实测输出

```text
['华东', '华北']
['华东', '华北']
华东 华东
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

标签为整数也不代表它是行位置。

## 练习题

选最后一行，分别用标签和位置表达。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[条件筛选](../05-selection/filter.md)。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
