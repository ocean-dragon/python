from typing import List


class Solution:
    def RemoveDuplicates(self, nums: List[int]) -> int:
        p1, p2 = 0, 0  # 两指针在同一组相同数之内丈量宽度
        idxV = 0
        l = len(nums)
        while p2 < l:
            while p2 < l and nums[p1] == nums[p2]:
                p2 += 1  # 一直移动p2，直到指向下一组
            nums[idxV] = nums[p1]
            if p2 - p1 >= 2:
                nums[idxV + 1] = nums[p1]
                idxV += 2
            else:
                idxV += 1
            p1 = p2  # 重新丈量下一组

        return idxV

    def RemoveDuplicates2(self, nums: List[int]) -> int:
        idx = 0  # 慢指针一：数组的索引
        for idxV in nums:  # 快指针二：数组元素值
            # 前两个直接放，同时也是为了避免后一个判断的越界
            # 后续的元素跟索引处前面的值比较，若是大体递增则元素值放在索引处
            if idx < 2 or nums[idx - 2] < idxV:
                nums[idx] = idxV
                idx += 1

        return idx


s = Solution()
nums = [1, 1, 1, 2, 2, 3]  # [1, 2, 3]
cnt = s.RemoveDuplicates(nums)
print(cnt, nums)
