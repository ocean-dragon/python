from typing import List

from numpy import sort


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0  # 指针一：数组的索引
        for idxV in nums:  # 指针二：数组的值
            if idxV != val:
                nums[idx] = idxV
                idx += 1

        return idx


s = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]  # [3, 2, 2, 3]
cnt = s.removeElement(nums, 2)
print(nums)
