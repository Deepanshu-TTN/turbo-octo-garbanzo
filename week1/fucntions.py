# Define a function calculate_area that calculates the area of a rectangle and return the result. 
# If no width is provided, it defaults to 10.
def calculate_area(h, w=10):
    return h*w
print(calculate_area(21))

# Write a recursive function to compute the factorial of a non-negative integer.
def facto(n):
    if n==1:
        return n
    return n*facto(n-1)
print(facto(4))

# Write a function that takes one parameter as a string and reverse it and return.
def reverse(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
print(reverse("deepanshu"))

# Write a Python function that takes two parameters as lists and to sum all the numbers in a list and return a value.
a = [8, 2, 3, 0, 7]
b = [3, -2, 5, 1]
def concat_and_sum(l1, l2):
    return sum(l1+l2)
print(concat_and_sum(a,b))

# Write a Python function that takes a list and returns a new list with distinct and sorted elements from the first list. 
a = [4,1,2,3,3,1,3,4,5,1,7]
def sanitize_list(lisT):
    return sorted(list(set(lisT)))
print(sanitize_list(a) ==  [1,2,3,4,5,7])
