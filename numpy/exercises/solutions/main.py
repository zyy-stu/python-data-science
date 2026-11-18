"""逐题运行并校验参考答案。"""

import numpy as np

a = np.arange(6)

# 第 1 题
assert (np.array([1, 2, 3]) + 2).tolist() == [3, 4, 5]

# 第 2 题
assert np.zeros((2, 2), dtype=int).tolist() == [[0, 0], [0, 0]]

# 第 3 题
assert np.ones(3, dtype=int).tolist() == [1, 1, 1]

# 第 4 题
assert np.full(2, 7).tolist() == [7, 7]

# 第 5 题
assert np.arange(1, 6, 2).tolist() == [1, 3, 5]

# 第 6 题
assert np.linspace(0, 1, 3).tolist() == [0.0, 0.5, 1.0]

# 第 7 题
assert np.identity(2, dtype=int).tolist() == [[1, 0], [0, 1]]

# 第 8 题
assert int(np.arange(5)[-1]) == 4

# 第 9 题
assert np.arange(5)[1:4].tolist() == [1, 2, 3]

# 第 10 题
assert np.ones((2, 3)).size == 6

# 第 11 题
assert np.arange(6).reshape(3, 2).tolist() == [[0, 1], [2, 3], [4, 5]]

# 第 12 题
assert np.array([[2, 4]]).T.tolist() == [[2], [4]]

# 第 13 题
assert np.array([[1, 2], [3, 4]]).sum(axis=0).tolist() == [4, 6]

# 第 14 题
assert np.array([[1, 3], [5, 7]]).mean(axis=1).tolist() == [2.0, 6.0]

# 第 15 题
assert not np.shares_memory(a, a.flatten())

# 第 16 题
assert np.shares_memory(a, a.reshape(3, 2))

# 第 17 题
assert (np.array([[10, 20], [30, 40]]) + [1, 2]).tolist() == [[11, 22], [31, 42]]

# 第 18 题
assert a[a > 2].tolist() == [3, 4, 5]

# 第 19 题
assert bool(np.isin(np.random.default_rng(42).integers(1, 7, 4), range(1, 7)).all())

# 第 20 题
assert int((np.array([2, 3]) * [10, 20]).sum()) == 80

print("20 道练习校验通过")
