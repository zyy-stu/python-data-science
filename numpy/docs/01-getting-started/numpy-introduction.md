# DS-001 NumPy 入门

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

列表加法拼接序列，数组加法按元素运算。数组以形状与 dtype 描述数据，适合数值向量运算。

## 完整代码与运行

打开[完整脚本](../../examples/01-array-basics/main.py)，从仓库根目录运行 `python numpy/examples/01-array-basics/main.py`。该脚本中的 `lesson_1()` 执行如下操作：

```python
values = np.array([1, 2, 3])
print((values + 10).tolist())
```

## 实测输出

```text
[11, 12, 13]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

列表不能直接与整数相加。

## 练习题

把标量 10 改成 2，比较与列表加法的区别。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。下一篇是[ndarray 数组基础](../02-array-basics/ndarray.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
