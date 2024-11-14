def has_subarray_with_zero_sum(arr):
    prefix_sum = 0
    prefix_sum_map = {}

    for num in arr:
        prefix_sum += num
        if prefix_sum == 0:
            return True
        else:
            if prefix_sum in prefix_sum_map:
                return True
            else:
                prefix_sum_map[prefix_sum] = True
    return False

# arr = [3, 4, -7, 1, 2, -1]
arr = [1,-1,2,3, -3, -2]
result = has_subarray_with_zero_sum(arr)
print(result)