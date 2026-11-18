"""数组创建示例。"""

import numpy as np


def lesson_3() -> None:
    """数组创建。"""
    print(np.array([2, 4]).tolist())
    print(np.zeros((1, 2), dtype=int).tolist())
    print(np.ones(2, dtype=int).tolist())
    print(np.full(2, 7).tolist())
    print(np.arange(0, 6, 2).tolist())
    print(np.linspace(0, 1, 3).tolist())
    print(np.identity(2, dtype=int).tolist())


if __name__ == "__main__":
    lesson_3()
