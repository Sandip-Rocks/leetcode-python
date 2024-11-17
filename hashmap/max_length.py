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
    presum = {}

    sum = 0
    max_len = 0

    # Traverse through the given array
    for i in range(len(arr)):
      
        # Add current element to sum
        sum += arr[i]

        # If the sum is 0, update max_len
        if sum == 0:
            max_len = i + 1

        # Check if this sum is seen before
        if sum in presum:
            # If this sum is seen before, update max_len
            max_len = max(max_len, i - presum[sum])
        else:
          
            # If this sum is not seen before, add it to the map
            presum[sum] = i

    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(max_len(arr))
