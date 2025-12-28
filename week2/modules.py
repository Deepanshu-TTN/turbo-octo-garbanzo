# Using datetime, ​​add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time
from datetime import datetime
from datetime import timedelta
given = datetime(2020, 3, 22, 10, 0)
new = given + timedelta(days=7, hours=12)
print(f"given: {given}, new: {new}")

# Code to get the dates of yesterday, today, and tomorrow.
def get_yesterday_today_tomorrow():
    _now = datetime.now()
    return _now - timedelta(days=1), _now, _now + timedelta(days=1)


# Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
import os
cwd = os.getcwd()
print(f"current working directory: {cwd}")

test_dir = os.path.join(cwd, "test")
os.mkdir(test_dir)
print(f"created directory: {test_dir}")
print(f"contents of cwd: {[entry for entry in os.listdir(cwd)]}")
os.rmdir(test_dir)
print(f"Removed directory: {test_dir}")

# Write a Python program to rename a file from old_name.txt to new_name.txt.
old = "old_name.txt"
new = "new_name.txt"
if not os.path.exists(old):
    with open(old, "w", encoding="utf-8") as f:
        f.write("content content content\n" * 5)
os.rename(old, new)
print(f"renamed {old} -> {new}")

# Create a file and Write a Python program to get the size of a file named example.txt 
os.rename(new, "example.txt")
size = os.path.getsize("example.txt")
print(f"size: {size} bytes")

# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00
date_str = "Feb 25 2020 4:20PM"
dt = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
print(dt)

# Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18
date = datetime(2025, 2, 25)
new_date = date - timedelta(days=7)
print("date:", new_date.date())

# Format the date 2020-02-25 as "Tuesday 25 February 2020"
date = datetime(2020, 2, 25)
formatted = date.strftime("%A %d %B %Y")
print(formatted)