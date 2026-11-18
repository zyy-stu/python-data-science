# DS-003 数组创建

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

array 从序列构造，zeros、ones、full 从形状填充。arange 用步长，linspace 用采样数量并默认包含终点。identity 创建方形单位阵。

## 完整代码与运行

打开[完整脚本](../../examples/02-array-creation/main.py)，从仓库根目录运行 `python numpy/examples/02-array-creation/main.py`。该脚本中的 `lesson_3()` 执行如下操作：

```python
print(np.array([2, 4]).tolist())
print(np.zeros((1, 2), dtype=int).tolist())
print(np.ones(2, dtype=int).tolist())
print(np.full(2, 7).tolist())
print(np.arange(0, 6, 2).tolist())
print(np.linspace(0, 1, 3).tolist())
print(np.identity(2, dtype=int).tolist())
```

## 实测输出

```text
[2, 4]
[[0, 0]]
[1, 1]
[7, 7]
[0, 2, 4]
[0.0, 0.5, 1.0]
[[1, 0], [0, 1]]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

浮点步长优先用 linspace 控制点数。

## 练习题

创建 3×3 单位阵和 0 到 1 的 5 个等距点。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[索引与切片](../03-indexing-slicing/indexing.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
