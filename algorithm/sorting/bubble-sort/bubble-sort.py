from typing import List
import random

"""
implement bubble sort using list
"""


def sort(unsorted_list: List[int]) -> List[int]:
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        target_list = unsorted_list
        for i in range(len(target_list)):
            for j in range(len(target_list) - i - 1):
                if target_list[j] > target_list[j + 1]:
                    # swap
                    temp = target_list[j]
                    target_list[j] = target_list[j + 1]
                    target_list[j + 1] = temp
        return target_list


if __name__ == "__main__":
    unsorted_list = [random.randint(-100, 100) for _ in range(10)]
    print(unsorted_list)
    assert sorted(unsorted_list) == sort(unsorted_list)
    print(sort(unsorted_list))
