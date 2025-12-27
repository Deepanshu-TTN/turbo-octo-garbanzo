# Find the Maximum and Minimum Values in a List
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(f'List: {numbers} max: {max(numbers)} min: {min(numbers)}')

# Given a set of numbers, find the maximum and minimum values.
setn = {5, 10, 3, 15, 2, 20}
print(f"set: {setn} max: {max(setn)} min: {min(setn)}")

# Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
def find_min_max(listn):
    # return min([(len(word), word) for word in listn], key=lambda x:x[0])[1], max([(len(word), word) for word in listn], key=lambda x:x[0])[1]
    return min(listn, key=len), max(listn, key=len)
print(find_min_max(words))
# Output: ('kiwi', 'grapefruit')