# 1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10  numbers 
def fibona():
    current, next1 = 0, 1
    while True:
        yield current
        current, next1 = next1, current + next1

generator1 = fibona()
for _ in range(10):
    print(next(generator1))
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.

#   Input n=3
def infinite_multiples(n):
    factor = 1
    while True:
        yield n* factor
        factor+=1
generator2 = infinite_multiples(3)
print([next(generator2) for _ in range(100)])
# Output:
# 3
# 6
# 9
# 12
# 15
# …

# 3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
def repeat_word(word, times):
    for i in range(times):
        yield word
word = "hello"
times = 5
generator3 = repeat_word(word, times)
for i in generator3:
    print(i)
