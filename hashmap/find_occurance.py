def find_occurance(arr):
    occurence_dictionary = {}
    for element in arr:
        if element in occurence_dictionary:
            occurence_dictionary[element] += 1
        else:
            occurence_dictionary[element] = 1
    return occurence_dictionary

arr = [1,3,5,1,5,3,2,3,4,2,1]
result = find_occurance(arr)
print(result)
