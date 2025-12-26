# Given a list of numbers, find and print the maximum and minimum values.
nums = [1, 2, 3, 4, 5]
max_value = max(nums)
min_value = min(nums)
print(f'List: {nums} max: {max_value} min: {min_value}')

# Given two lists below, merge the values from both lists to one and print
a = [1,2,3,4]      
b = [5,6,7,8] 
print(f"concatinated list: {a + b}")

# From a list, print the number of times the value 3 appears in the list:
a = [1,3,4,5,2,1,3,9,3]
print(f"in list: {a}, 3 appears {a.count(3)} times")

# From below list, Sort the list and print
a = [1,3,4,5,2,1,3,9,3]
print(sorted(a))

# Given a set, add the element 6 to it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(f"numbers: {numbers}")

# Given a set, remove the element 3 from it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)

# Given two sets, find and print their intersection.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"intersection: {set1.intersection(set2)}")

# Given a tuple, count and print the number of occurrences of the element 'apple'.
fruits = ('apple', 'banana', 'apple', 'cherry')
print(f"in fruits {fruits} apple occurs {fruits.count("apple")} times")

# Given two tuples, concatenate them and print the result.
tuple1 = (1, 2, 3)     
tuple2 = (4, 5, 6)
print(f"concatenated: {tuple1 + tuple2}")

# Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"age: {person.get("age")}")

# Add new key,  gender to dictionary and assign “M” to it and print
person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"] = "M"
print(person)

# Remove the key "city" from the above Dict and print
print(person.pop("city"))
# Given two dictionaries, merge them into one
dict1 = {"a": 1, "b": 2}    
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)
