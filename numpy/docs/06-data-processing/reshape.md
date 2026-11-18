# DS-006 数组变形

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

reshape 可用一个 -1 推断轴长度，总元素数要一致。flatten 总是复制，ravel 尽量返回视图，transpose 重排轴，复制与否可用 shares_memory 检查。

## 完整代码与运行

打开[完整脚本](../../examples/05-reshape/main.py)，从仓库根目录运行 `python numpy/examples/05-reshape/main.py`。该脚本中的 `lesson_6()` 执行如下操作：

```python
a = np.arange(6).reshape(2, 3)
print(a.reshape(3, -1).tolist())
print(a.flatten().tolist(), a.ravel().tolist())
print(a.transpose().tolist())
print(np.shares_memory(a, a.flatten()), np.shares_memory(a, a.ravel()))
```

## 实测输出

```text
[[0, 1], [2, 3], [4, 5]]
[0, 1, 2, 3, 4, 5] [0, 1, 2, 3, 4, 5]
[[0, 3], [1, 4], [2, 5]]
False True
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

避免把 ravel 的结果当成一定独立的数据。

## 练习题

尝试 reshape(4, -1) 并解释异常。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[广播](../05-broadcasting/broadcasting.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
