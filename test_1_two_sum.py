from typing import List

import pytest


def twoSum(input_list: List[int], target_sum: int) -> List[int]:
    seen = {}
    for index, number in enumerate(input_list):
        remaining = target_sum - number
        if remaining in seen:
            return [seen[remaining], index]
        seen[number] = index
    return []


class TestTwoSum:
    @pytest.mark.parametrize(
        "input_list, target_sum, solution_indices",
        [
            ([3, 3], 6, [0, 1]),
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([1, 3, 5, 7], 10, [3, 1]),
            (
                [1, 2, 3, 4, 5],
                100,
                [],
            ),  # Check that unsolvable inputs return an empty list
        ],
    )
    def test_simple_cases(self, input_list, target_sum, solution_indices):
        assert twoSum(input_list, target_sum).sort() == solution_indices.sort()
