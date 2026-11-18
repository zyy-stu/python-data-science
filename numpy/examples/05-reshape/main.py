"""数组变形示例。"""

import numpy as np


def lesson_6() -> None:
    """数组变形。"""
    a = np.arange(6).reshape(2, 3)
    print(a.reshape(3, -1).tolist())
    print(a.flatten().tolist(), a.ravel().tolist())
    print(a.transpose().tolist())
    print(np.shares_memory(a, a.flatten()), np.shares_memory(a, a.ravel()))


if __name__ == "__main__":
    lesson_6()
