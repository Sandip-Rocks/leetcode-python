"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

 

Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        maxBanana = max(piles)
        left, right = 1, maxBanana

        while left <= right:
            mid = (left + right) // 2
            if self.canEatAll(mid, piles, h):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def canEatAll(self, speed: int, piles: list[int], h: int) -> bool:
        hours_required = 0
        for bananas in piles:
            hours_required += math.ceil(bananas / speed)
        return hours_required <= h

solution = Solution()
print(solution.minEatingSpeed([3, 6, 7, 11], 8))  # Output: 4

print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30

print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))  # Output: 23

"""
Explanation

1. Binary Search on Speed:

We calculate the maximum banana pile to set the right bound (right), with the minimum speed as 1 (left).
We use binary search on possible eating speeds from left to right.

2. Check Feasibility:

The canEatAll helper function calculates the total hours needed if Koko eats at a given speed.
It checks if eating at this speed allows Koko to finish within h hours.

3. Adjust Bounds:

If canEatAll returns True, then try a slower speed (right = mid - 1).
Otherwise, increase the speed (left = mid + 1).

4. Return:

Once the loop ends, left will be at the minimum speed required to finish within h hours.


### Time Complexity

The time complexity of this solution is \(O(n \log m)\), where:
- (n) is the number of piles.
- (m) is the largest pile size.

**Explanation**:
1. **Binary Search**: The binary search on the eating speed ranges from 1 to the maximum number of bananas in any pile, so it will perform \(O(\log m)\) steps.
2. **Feasibility Check (`canEatAll` method)**: For each speed considered in the binary search, the `canEatAll` function checks all piles to calculate the total hours, taking \(O(n)\) time.

So, the overall complexity is:
                                    (O(n log m))

### Space Complexity

The space complexity is \(O(1)\) because we use a constant amount of extra space, regardless of the input size:
- The `canEatAll` function only uses a few extra variables.
- No additional data structures are required that scale with the input.

### Summary

- **Time Complexity**: (O(n log m))
- **Space Complexity**: (O(1))
"""

