"""
https://leetcode.com/problems/merge-sorted-array/description/
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(n):
            nums1[m + i] = nums2[i]

        gap = (m + n + 1) // 2

        while gap > 0:
            i = 0
            while i + gap < m + n:
                if nums1[i] > nums1[i + gap]:
                    nums1[ i + gap], nums1[i] = nums1[i], nums1[i + gap]
                i +=1

            if gap == 1:
                break 
            gap = (gap + 1) // 2
        print(f'nums1 = {nums1}')

if __name__ == '__main__':
    solution = Solution()
    solution.merge([1,2,3,0,0,0], 3, [2,5,6],3)