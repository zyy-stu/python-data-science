# DS-005 数组运算

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

加减乘除针对对应元素，矩阵乘法使用 @。聚合沿指定轴折叠，二维数组的 axis=0 为逐列结果，axis=1 为逐行结果。

## 完整代码与运行

打开[完整脚本](../../examples/04-array-operations/main.py)，从仓库根目录运行 `python numpy/examples/04-array-operations/main.py`。该脚本中的 `lesson_5()` 执行如下操作：

```python
a = np.array([[2, 4], [6, 8]])
b = np.array([[1, 2], [3, 4]])
print((a + b).tolist(), (a - b).tolist())
print((a * b).tolist(), (a / b).tolist())
print(a.sum(axis=0).tolist(), a.mean(axis=1).tolist())
print(a.min(), a.max())
```

## 实测输出

```text
[[3, 6], [9, 12]] [[1, 2], [3, 4]]
[[2, 8], [18, 32]] [[2.0, 2.0], [2.0, 2.0]]
[8, 12] [3.0, 7.0]
2 8
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

整数真除结果为浮点数。

## 练习题

预测 axis 改为 1 后的求和结果。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[数组变形](../06-data-processing/reshape.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
