# Given a list of numeric strings, convert them into integers. Using List Comprehensions
strings = ["1", "2", "3", "4", "5"]
ints = [int(number) for number in strings]
print(ints)
#Expected output : [1, 2, 3, 4, 5]

# Extract all integers from a list that are greater than 10. Using List Comprehensions
numbers = [1, 5, 13, 4, 16, 7]
print([num for num in numbers if num > 10])
#Expected output :[13, 16]

# Create a list of squares for numbers from 1 to 5. Using List Comprehensions
print([n**2 for n in range(1,6)])
#Expected output :[1, 4, 9, 16, 25]

# Convert a 2D list into a 1D list.Using List Comprehensions
matrix = [[1, 3, 4], [23, 32, 56, 74], [-2, -6, -9]]
print([j for i in matrix for j in i])
#Expected output : [1, 3, 4, 23, 32, 56, 74, -2, -6, -9]

# Given two lists, keys = ['a', 'b', 'c'] and values = [1, 2, 3], create a dictionary using dictionary comprehension.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print({k:v for k in keys for v in values})
#Expected output : {'a': 1, 'b': 2, 'c': 3}

# Given the dictionary scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}, create a new dictionary containing only the students who scored above 80
scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90}
print({k:v for k,v in scores.items() if v > 80})
#Expected output : {'Alice': 85, 'Charlie': 90}
