"""
1423. Maximum Points You Can Obtain from Cards

leetcode: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

Youtube: https://www.youtube.com/watch?v=pBWCOCS636U&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=2

"""
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        lsum = sum(cardPoints[:k])
        max_sum = lsum

        for i in range(1, k+1):
            lsum = lsum - cardPoints[k-i] + cardPoints[n-i]

        max_sum = max(max_sum, lsum)

        return max_sum
    
if __name__ == "__main__":
    solution= Solution()
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    result = solution.maxScore(cardPoints, k)
    print(result)