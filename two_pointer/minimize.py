"""

Minimize (max(A[i], B[j], C[k]) – min(A[i], B[j], C[k])) of three different sorted arrays

https://www.geeksforgeeks.org/minimize-maxai-bj-ck-minai-bj-ck-three-different-sorted-arrays/

Given three sorted arrays A, B, and C of not necessarily same sizes. 
Calculate the minimum absolute difference between the maximum and minimum number of any triplet A[i], B[j], C[k]
such that they belong to arrays A, B and C respectively, i.e.,
minimize (max(A[i], B[j], C[k]) – min(A[i], B[j], C[k]))

Input : A : [ 1, 4, 5, 8, 10 ]
        B : [ 6, 9, 15 ]
        C : [ 2, 3, 6, 6 ]
Output : 1

"""

def minimize(A, B, C):
    # Initialize pointers for A, B, C
    i, j, k = 0, 0, 0
    min_diff = float('inf')  # Start with an infinitely large difference

    # Traverse until we reach the end of any of the arrays
    while i < len(A) and j < len(B) and k < len(C):
        # Current elements from each array
        a, b, c = A[i], B[j], C[k]

        # Calculate current maximum and minimum
        current_max = max(a, b, c)
        current_min = min(a, b, c)

        # Update the minimum difference
        min_diff = min(min_diff, current_max - current_min)

        # Move the pointer for the minimum value
        if current_min == a:
            i += 1
        elif current_min == b:
            j += 1
        else:
            k += 1

    return min_diff

# Driver code
A = [5, 8, 10, 15]
B = [6, 9, 15, 78, 89]
C = [2, 3, 6, 6, 8, 8, 10]

# Call the solve function and print the result
print(minimize(A, B, C))  # Output the minimum absolute difference

"""
TC: O(n+ m + k), where n, m and k are the lengths of A, B and C respectively
SC: O(1)
"""