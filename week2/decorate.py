# 1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.
import time
def time_this(func):
    def inner(arg):
        start = time.time_ns()
        result = func(arg)
        print(f"{func.__name__} took {time.time_ns()-start} ns")
        return result
    return inner

@time_this
def appendor(some_list):
    for i in range(1, 1001):
        some_list.append(i)
    return some_list
print(len(appendor([0])))

# 2. Create a parameterised decorator retry that retries a function a specified number of times.
def retry(n):
    def retry(func):
        def inner(arg):
            for _ in range(n):
                func(arg)
        return inner
    return retry

@retry(3)
def may_fail(name):
        print(f"Hello, {name}!")
may_fail("deepanshu")

# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
def validate_positive(func):
    def inner(arg):
        if arg<=0:
            raise ValueError("NOT POSITIVE!!")
        return func(arg)
    return inner

@validate_positive
def square_root(x):
    return x ** 0.5

try:
    square_root(-100)
except ValueError as v:
    print(f"error: {v}")

# 4. Create a decorator cache that caches the result of a function based on its arguments.
# Write a cache decorator for it to check if the calculation is already performed then return the result.
def cache(func):
    cache = {}
    def inner(arg):
        if arg in cache:
            return cache[arg]
        cache[arg] = func(arg)
        return cache[arg]
    return inner

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x
	
expensive_computation(5)
expensive_computation(5)


# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.
def requires_permission(func):
    def inner(*args):
        if 'admin' in args[0]['permissions']:
            func(*args)
            return
        print("Access denied.")
    return inner

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test’']}
delete_user(user1, 20)
delete_user(user2, 19)