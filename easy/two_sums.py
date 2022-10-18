from typing import *


class Soultion:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()

        for i in range(len(nums)):
            r = target - nums[i]

            if r in m:
                return [i, m[r]]

            m[nums[i]] = i
