"""广播示例。"""

import numpy as np


def lesson_7() -> None:
    """广播。"""
    prices = np.array([[10, 20], [30, 40]])
    fees = np.array([1, 2])
    print((prices + fees).tolist())
    print((prices + np.array([[1], [2]])).tolist())


if __name__ == "__main__":
    lesson_7()
