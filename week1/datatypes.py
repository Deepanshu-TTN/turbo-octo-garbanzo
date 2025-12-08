"""Task: Convert the following values to the specified types and print the results
Convert 3.75 to an integer and print the value


Convert "123" to a float and print the value


Convert 0 to a boolean and print the value


Convert False to a string and print the value
"""

print(int(3.75))
print(float("123"))
print(bool(0))
print(str(False))





'''Convert all characters in the string to uppercase. x = "hello"'''
x = "hello"
print(x.upper())





''' Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. And convert it to integer.'''
x = 5
y = 3.14
z = x + y
print(type(z))
z = int(z)
print(type(z))





"""Given the string s = 'hello', perform the following operations:
Convert the string to uppercase.


Replace 'e' with 'a'.


Check if the string starts with 'he'.


Check if the string ends with 'lo'.
"""
s = 'hello'
ea_replaceed_s = s.replace('e', 'a')
print(s, ea_replaceed_s)
print(s.startswith('he'))
print(s.endswith('lo'))