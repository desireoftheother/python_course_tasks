from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        diffs_dict = {num: (target-num, index) for index, num in enumerate(nums)}
        for num, diff_i in diffs_dict.items():
            diff = diff_i[0]
            index = diff_i[1]
            if diff in nums_set:
                if index != nums.index(diff):
                    return [index, nums.index(diff)]
