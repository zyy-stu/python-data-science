"""随机数示例。"""

import numpy as np


def lesson_8() -> None:
    """随机数。"""
    rng = np.random.default_rng(42)
    print(rng.integers(1, 7, size=4).tolist())
    print(rng.random(2).round(3).tolist())
    print(rng.normal(0, 1, 3).round(3).tolist())
    print(rng.uniform(10, 20, 2).round(3).tolist())


if __name__ == "__main__":
    lesson_8()
