# DS-020 读取与保存 CSV

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。数据来自[仓库教学 CSV](../../../datasets/sample/README.md)。

## 概念与原理

read_csv 负责解析文本；to_csv 默认输出索引，需要 index=False 避免生成额外列。显式指定编码，标识符列按字符串处理。

## 完整代码与运行

打开[完整脚本](../../examples/08-csv/main.py)，从仓库根目录运行 `python pandas/examples/08-csv/main.py`。该脚本中的 `lesson_12()` 执行如下操作：

```python
users = load('users')
with TemporaryDirectory() as tmp:
    output = Path(tmp) / 'users.csv'
    users.to_csv(output, index=False, encoding='utf-8')
    restored = pd.read_csv(output, dtype={'user_id': 'string'})
    print(restored.columns.tolist(), restored['user_id'].tolist())
```

## 实测输出

```text
['user_id', 'region'] ['U1', 'U2', 'U3']
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

CSV 不保存原始 dtype，读回时按需要声明。

## 练习题

另存一份仅含用户编号的 CSV 并回读。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。从[专题知识目录](../README.md)选择后续方向。

[官方参考资料](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/index.html)
