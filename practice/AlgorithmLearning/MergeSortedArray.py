from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        r1 = m - 1
        r2 = n - 1
        while r2 >= 0:
            if r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[i] = nums1[r1]
                r1 -= 1
            else:  # nums1[r1] <= nums2[r2]
                nums1[i] = nums2[r2]
                r2 -= 1
            i -= 1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


s = Solution()
num1 = [1, 2, 3, 0, 0, 0]
s.merge2(num1, 3, [2, 5, 6], 3)
print(num1)
