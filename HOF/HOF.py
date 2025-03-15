
'''
Questions:
1   - Given a list of strings `["1", "2", "3", "4"]`, use `map()` to convert them into integers.

2   - Given a list of numbers `[2, 4, 6, 8]`, use `map()` to return a new list containing their squares.

3   - Given a list `[1, 2, 3, 4, 5, 6, 7, 8, 9]`, use `filter()` to extract only even numbers.

4  - Given a list of words `["apple", "banana", "kiwi", "strawberry", "grape"]`, use `filter()` to get words with more than 5 letters.

5  - Given a list `[10, 20, 30, 40]`, use `reduce()` to find the sum of all elements.

6  - Given a list `[3, 8, 2, 5, 10, 6]`, use `reduce()` to find the maximum value.

7  - Given a list `[1, 2, 3, 4, 5]`, use `reduce()` to compute the product of all elements.

8  - Given a list of temperatures in Fahrenheit `[32, 50, 77, 104]`, use `map()` to convert them to Celsius.  

9  - Given `["level", "python", "radar", "world", "madam"]`, use `filter()` to return only palindromes.

10  - Given a sentence `"Python is fun and powerful"`, use `map()` and `len()` to count the number of characters in each word.
'''
# =====================================================================
l = ["1", "2", "3", "4"] # 1

result = list(map(lambda x: int(x), l))

# =====================================================================
l = [2, 4, 6, 8] # 2

result = list(map(lambda x: x ** 2, l))

# =====================================================================
l = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 3

result = list(filter(lambda x : x % 2 == 0, l))

# =====================================================================

l = ["apple", "banana", "kiwi", "strawberry", "grape"] # 4

result = list(filter(lambda x: len(x) > 5, l))

# =====================================================================
from functools import reduce # 5
l = [10, 20, 30, 40]

result = reduce(lambda x, y: x+y,l)

# =====================================================================
l = [3, 8, 2, 5, 10, 6] # 6

result = reduce(lambda x , y: x if x > y else y, l)

# =====================================================================

l = [1, 2, 3, 4, 5] # 7

result = reduce(lambda x, y: x * y ,l)

# =====================================================================

l = [32, 50, 77, 104] # 8

result = list(map(lambda f: (f - 32) * (5/9), l))

# =====================================================================

l = ["level", "python", "radar", "world", "madam"] # 9

result = list(filter(lambda st: st[::-1]== st , l))

# =====================================================================
st = "Python is fun and powerful" # 10
result = list(map(lambda word : len(word) ,st.split()))
print(result)
