# DS-002 ndarray 数组基础

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

shape 给出每轴长度，ndim 给出轴数，size 等于轴长度的乘积，dtype 描述元素存储类型。向量、矩阵和三维批次都是 ndarray。

## 完整代码与运行

打开[完整脚本](../../examples/01-array-basics/main.py)，从仓库根目录运行 `python numpy/examples/01-array-basics/main.py`。该脚本中的 `lesson_2()` 执行如下操作：

```python
vector = np.array([1, 2], dtype=np.int32)
matrix = np.array([[1, 2], [3, 4]], dtype=np.int32)
batch = matrix[None, :, :]
print(vector.shape, matrix.shape, batch.shape)
print(matrix.ndim, matrix.size, matrix.dtype)
```

## 实测输出

```text
(2,) (2, 2) (1, 2, 2)
2 4 int32
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

shape 为 (2,) 的数组与 (2, 1) 有不同的轴数。

## 练习题

为矩阵多加一行，并预测四个属性。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[数组创建](../02-array-basics/array-creation.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
