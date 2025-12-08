'''Objective: Ask the user for their name and greet them.
Task: Write a program that asks the user for their name and then prints a greeting   message using their name.'''
user = input("Hello user! What might your name be? ")
print(f"Pleasent afternoon {user}")


'''Objective: Perform basic arithmetic operations based on user input.
Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.'''
number_1 = int(input("Hello again user!, may I interest you in a number?"))
number_2 = int(input("Great choice! Almost makes me wanna ask for another: "))
print(f"{number_1} + {number_2} = {number_1 + number_2}")
print(f"{number_1} x {number_2} = {number_1 * number_2}")
print(f"{number_1} / {number_2} = {number_1 / number_2}")

'''Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.'''
user_input = input("Who are your favorite n people(I like my people comma-seperated): ")
input_list = user_input.split(',')
print(type(input_list), input_list)


'''Task: Ask the user to enter their age and check if they are eligible to vote based on their age.'''
just_a_number = int(input("And how long have u been here(age)? "))
if(just_a_number < 18):
    print("I'm afraid you cannot vote here, have an ice cream instead.")
else:
    print("Perfect! you can vote, here's an ice cream anyways ;)")


'''For value = 3.14159, Using f-string print output for only up to 2 decimal places.
Output: 3.14'''
value = 3.14159
print(f'{value:0.2f}')