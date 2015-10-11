# -*- coding: utf-8 -*-
from practices.practice1 import solution
import pytest

test_practice_cases = [
    {
        "input_list": [("biaozhu", 6, 332, "标注1"),
                       ("huaxian", -10, 2),
        ],
        "output_set": {("biaozhu", 6, 299, "标注1"),
                       ("huaxian", 0, 2),
        }
    },
    {
        "input_list": [("biaozhu", 6, 10, "标注1"),
                       ("huaxian", 3, 10),
                       ("huaxian", 12, 20),
                       ("huaxian", 4, 14),
                       ("biaozhu", 9, 14, "标注2"),
        ],
        "output_set": {("biaozhu", 6, 10, "标注1"),
                       ("huaxian", 3, 20),
                       ("biaozhu", 9, 14, "标注2"),
        }
    },
    {
        "input_list": [("huaxian", -2, 10),
                       ("biaozhu", 6, 10, "标注1"),
                       ("huaxian", -3, 20),
                       ("huaxian", 50, 100),
                       ("biaozhu", 290, 300, "标注2"),
        ],
        "output_set": {("biaozhu", 6, 10, "标注1"),
                       ("huaxian", 0, 20),
                       ("huaxian", 50, 100),
                       ("biaozhu", 290, 299, "标注2"),
        }
    },
    {
        "input_list": [ ("huaxian", 5, 50),
                        ("huaxian", 10, 20),
                        ("huaxian", 50, 100),
        ],
        "output_set": {("huaxian", 5, 100)
        }
    },
]

@pytest.mark.parametrize('case', test_practice_cases)
def test_practice1(case):
    sol = solution(case["input_list"])
    assert len(sol) == len(case["output_set"])
    assert set(sol) == case["output_set"]
