# DS-004 索引与切片

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

整数索引选一个位置，切片右边界不包含。多轴用逗号分隔；基本切片通常共享存储，布尔和整数数组索引生成副本。

## 完整代码与运行

打开[完整脚本](../../examples/03-indexing/main.py)，从仓库根目录运行 `python numpy/examples/03-indexing/main.py`。该脚本中的 `lesson_4()` 执行如下操作：

```python
values = np.arange(6)
grid = values.reshape(2, 3)
print(values[-1], grid[1, 2])
print(values[1:4].tolist(), grid[:, 1:].tolist())
print(grid[grid % 2 == 0].tolist())
```

## 实测输出

```text
5 5
[1, 2, 3] [[1, 2], [4, 5]]
[0, 2, 4]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

布尔掩码需要与它索引的维度匹配。

## 练习题

选择第二列并构造仅保留大于 2 的布尔掩码。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[数组运算](../04-array-operations/operations.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
