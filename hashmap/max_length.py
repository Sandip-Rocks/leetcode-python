"""
https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23}
Output: 5
Explanation: The longest subarray with sum equals to 0 is {-2, 2, -8, 1, 7}


Input: arr[] = {1, 2, 3}
Output: 0
Explanation: There is no subarray with 0 sum


Input:  arr[] = {1, 0, 3}
Output:  1
Explanation: The longest sub-array with sum equal to 0 is {0}
"""

# Function to return the length of the largest subarray
# with sum 0
def max_len(arr):
  
    # Map to store the previous sums
    map = {}

    currsum = 0
    ans = 0

    # Traverse through the given array
    for i in range(len(arr)):
      
        # Add current element to currsum
        currsum += arr[i]

        # If the currsum is 0, update ans
        if currsum == 0:
            ans = i + 1

        # Check if this currsum is seen before
        if currsum in map:
            # If this currsum is seen before, update ans
            ans = max(ans, i - map[currsum])
        else:
          
            # If this currsum is not seen before, add it to the map
            map[currsum] = i

    return ans

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(max_len(arr))
