# DS-007 广播

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

从最右轴对齐，轴长度相等或其中一个为 1 才兼容，缺失轴视为 1。广播节省显式重复输入的空间，但输出仍可能很大。

## 完整代码与运行

打开[完整脚本](../../examples/06-broadcasting/main.py)，从仓库根目录运行 `python numpy/examples/06-broadcasting/main.py`。该脚本中的 `lesson_7()` 执行如下操作：

```python
prices = np.array([[10, 20], [30, 40]])
fees = np.array([1, 2])
print((prices + fees).tolist())
print((prices + np.array([[1], [2]])).tolist())
```

## 实测输出

```text
[[11, 22], [31, 42]]
[[11, 21], [32, 42]]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

按行加偏移前先检查是否需要形状 (行数, 1)。

## 练习题

将形状 (2, 2) 与 (3,) 相加，解释失败的轴。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[随机数](../08-random/random.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
