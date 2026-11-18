# DS-008 随机数

## 学习目标与前置知识

能运行本节实验，解释输出及其边界。需要掌握 Python 变量、列表、函数及终端命令。

## 环境与示例数据

使用 Python 3.11+、NumPy 2.2.6、Pandas 2.2.3。从仓库根目录运行 `python -m pip install -r requirements-dev.txt`。输入是示例代码内的固定小数组或固定种子。

## 概念与原理

用 default_rng 创建独立 Generator。integers 默认排除高端；random 生成 [0,1)；normal、uniform 分别生成正态与均匀样本。固定种子便于复现。

## 完整代码与运行

打开[完整脚本](../../examples/07-random/main.py)，从仓库根目录运行 `python numpy/examples/07-random/main.py`。该脚本中的 `lesson_8()` 执行如下操作：

```python
rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=4).tolist())
print(rng.random(2).round(3).tolist())
print(rng.normal(0, 1, 3).round(3).tolist())
print(rng.uniform(10, 20, 2).round(3).tolist())
```

## 实测输出

```text
[1, 5, 4, 3]
[0.859, 0.697]
[-1.951, -1.302, 0.128]
[17.861, 11.281]
```

共享脚本会按顺序打印它包含的各节结果。

## 常见错误

复用同一生成器时，调用会推进随机状态。

## 练习题

分别用相同种子新建两个生成器，比较首批结果。 更多练习见[题目](../../exercises/questions/README.md)及[答案](../../exercises/solutions/README.md)。

## 总结与下一篇

用一个小输入复现结果，再修改输入验证边界。从[专题知识目录](../README.md)选择后续方向。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
