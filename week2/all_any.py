# Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
numbers = [1, 2, 3, 4, 5]
print(all([num >= 0 for num in numbers]))
# #Expected Output : True

# Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
numbers = [1, 3, 5, 7, 8]
print(any([num%2==0 for num in numbers]))
# #Expected Output: True

# Determine if any number in a list is divisible by 5 an print.
my_list = [1, 3 , 5, 6, 10]
print(any([num%5==0 for num in my_list]))