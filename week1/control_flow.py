# For loop
"""Write a program that takes the input from the user and checks if a number is even or odd."""
n = int(input())
print("Even" if n % 2 == 0 else "Odd")


"""Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”"""
s = input()
rev = ""
for ch in s:
    rev = ch + rev
print("Palindrome" if s == rev else "Not Palindrome")

"""Using the input from the user, Generate the first N numbers of the Fibonacci sequence."""
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(f"{a} ")
    a, b = b, a + b

"""From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]"""
lst = [1,2,3,4,5]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == 9:
            print([lst[i], lst[j]])

# While loop
"""Print all even numbers between 1 and 20 using a while loop."""
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# Break
'''Find the first occurrence of a number in a list and stop further searching. '''
numbers = [10, 20, 30, 40, 50]
search_for = 30

for n in numbers:
    if n == search_for:
        print("nound:", n)
        break

# Continue
"""Using continue statement, print only the odd numbers from 1 to 10."""
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# Pass
# What will be the output 
# for i in range(5):
#     if i == 3:
#         pass  
#     print(i)

# Match
"""Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements."""
day = input()

match day.lower():
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Weekday")



