"""执行示例、练习答案及销售分析。"""

import json
import runpy
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = json.loads((ROOT / "tests" / "expected-output.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize(("path", "expected"), EXPECTED.items(), ids=EXPECTED)
def test_script_output(path: str, expected: str) -> None:
    result = subprocess.run(
        [sys.executable, "-X", "utf8", str(ROOT / path)],
        capture_output=True,
        encoding="utf-8",
        timeout=30,
        check=True,
    )
    assert result.stdout.rstrip("\n") == expected


def test_sales_analysis() -> None:
    analyze = runpy.run_path(ROOT / "projects/sales-analysis/main.py")["analyze"]
    assert analyze() == {
        "raw_rows": 5,
        "duplicates": 1,
        "incomplete": 1,
        "total_cents": 68000,
        "product": {("P1", "键盘"): 60000, ("P2", "鼠标"): 8000},
        "user": {"U1": 24000, "U2": 8000, "U3": 36000},
        "month": {"2026-01": 32000, "2026-02": 36000},
    }
