# Using below list and enumerate(), print index followed by value. 

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i} {fruit}")
# Output: 
# 0 apple
# 1 banana
# 2 cherry

# Using below dict and enumerate, print key followed by value
person = {"name": "Alice", "age": 30, "city": "New York"}
for i, (key, value) in enumerate(person.items()):
    print(F"{key}: {value}")
# Output:
# name: Alice
# age: 30
# city: New York

# Given the list , use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print([(i, fruit) for i, fruit in enumerate(fruits, 1) if i%2==0])
#   Output: [(2, 'banana'), (4, 'date')]
