def length_of_subarray_with_zero_sum(arr):
    prefix_sum = 0
    prefix_sum_map = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            return i + 1  # Length of the subarray

        if prefix_sum in prefix_sum_map:
            return i - prefix_sum_map[prefix_sum]

        # Store the first occurrence of this prefix sum
        prefix_sum_map[prefix_sum] = i
        print(prefix_sum_map)

    return 0  # If no zero-sum subarray is found

# Test case
# arr = [3, 4, -7, 1, 2, -1, 2, -1, -2]
arr = [1,-1,2,3, -3, -2]
result = length_of_subarray_with_zero_sum(arr)
print(f"The length of the subarray with sum 0 is: {result}")
