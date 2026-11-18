"""索引与切片示例。"""

import numpy as np


def lesson_4() -> None:
    """索引与切片。"""
    values = np.arange(6)
    grid = values.reshape(2, 3)
    print(values[-1], grid[1, 2])
    print(values[1:4].tolist(), grid[:, 1:].tolist())
    print(grid[grid % 2 == 0].tolist())


if __name__ == "__main__":
    lesson_4()
