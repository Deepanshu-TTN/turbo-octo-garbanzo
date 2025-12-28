# 1 . Write a Python program to read the entire content of a file named sample.txt and display it.
with open("sample.txt", 'r') as file:
    for line in file.readlines():
        print(line, end="")
    print()

# 2. Write a Python program to count the number of words in a file named words.txt
with open("words.txt", "r") as file:
    words = [word for word in line for line in file.readlines()]
    print(len(words))

# 3.Create a program to write the string “Hello, Python!” into a file named output.txt.
with open("output.txt","w+") as file:
    file.write("Hello, python!")

# 4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

import csv
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.


