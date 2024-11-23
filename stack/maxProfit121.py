"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        ans = 0
        min_price = prices[0]

        for price in prices:
            ans = max(ans, price - min_price)
            min_price = min(min_price, price)
        return ans

if __name__ == '__main__':
    solution = Solution()
    prices = [100,80,60,70,60,75,85]
    result = solution.maxProfit(prices)
    print(result) # Output: 25

"""
TC: O(n)
SC: O(1)
"""