from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        max_length = 0
        curr_sum = 0

        while r < len(nums):
            curr_sum += nums[r]

            while curr_sum > k and l <= r:
                curr_sum -= nums[l]
                l +=1

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length

if __name__ == '__main__':
    solution = Solution()
    result = solution.longestSubarray([2,5,1,7,10], k = 14)
    print(result)
