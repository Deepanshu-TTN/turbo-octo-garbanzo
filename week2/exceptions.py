# Write a Python program that attempts to divide two numbers 
# and handles a ZeroDivisionError if the denominator is zero. Divide a by b and handle the exception and print the error
a = 10
b = 0
try:
    a/b
except ZeroDivisionError as z:
    print(f"error: {z}")


# Apply exception handling to below code and handle an exception if the index is out of range. 
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as i:
    print(f"error: {i}")

# Correct this below code with appropriate exception handlings. And finally print “Execution completed”
def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print("error:", e)
    except TypeError as e:
        print("error:", e)
    finally:
        print("Execution completed")

safe_divide(1, 0)
safe_divide(1, "a")
