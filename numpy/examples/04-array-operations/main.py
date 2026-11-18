"""数组运算示例。"""

import numpy as np


def lesson_5() -> None:
    """数组运算。"""
    a = np.array([[2, 4], [6, 8]])
    b = np.array([[1, 2], [3, 4]])
    print((a + b).tolist(), (a - b).tolist())
    print((a * b).tolist(), (a / b).tolist())
    print(a.sum(axis=0).tolist(), a.mean(axis=1).tolist())
    print(a.min(), a.max())


if __name__ == "__main__":
    lesson_5()
