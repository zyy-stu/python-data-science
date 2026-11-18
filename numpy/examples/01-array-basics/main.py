"""NumPy 入门、ndarray 数组基础示例。"""

import numpy as np


def lesson_1() -> None:
    """NumPy 入门。"""
    values = np.array([1, 2, 3])
    print((values + 10).tolist())


def lesson_2() -> None:
    """ndarray 数组基础。"""
    vector = np.array([1, 2], dtype=np.int32)
    matrix = np.array([[1, 2], [3, 4]], dtype=np.int32)
    batch = matrix[None, :, :]
    print(vector.shape, matrix.shape, batch.shape)
    print(matrix.ndim, matrix.size, matrix.dtype)


if __name__ == "__main__":
    lesson_1()
    lesson_2()
