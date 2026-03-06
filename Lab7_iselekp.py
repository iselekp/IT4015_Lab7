#Task 1 - printing a message
print("Hello, Python World!")
#Task 2.0 - creating variables
name = "Karl Isele"
age = 24
height = 1.85
#Task 2.1 - printing variables
print("My name is " + name + ".")
print("I am " + str(age) + " years old.")
print("I am " + str(height) + " meters tall.")
#Task 3.0 - creating a list
favorite_foods = ["apples", "bananas", "blueberries", "pizza"]
#Task 3.1 - printing a list
print("My favorite foods in a list: " + str(favorite_foods))
#Task 3.2 - creating a dictionary
book_info = {"title": "A Wizard of Earthsea", "author": "Ursula K. Le Guin", "year": "1968"}
#Task 3.3 - printing a dictionary
print("I am currently reading: " + str(book_info))
#Task 4.0 - capturing user input
number = int(input("Enter a number: "))
#Task 4.1 - branching flow control
if number > 0:
    print(str(number) + " is positive.")
elif number < 0:
    print(str(number) + " is negative.")
else:
    print(str(number) + " is zero.")
#Task 4.2 - looping flow control
print("My favorite foods are ", end='')
i = 1
for food in favorite_foods:
    print(food, end='')
    if i < len(favorite_foods) - 1:
        print(", ", end='')
    if i == len(favorite_foods) - 1:
        print(" and ", end='')
    i = i + 1
print(".")
#Task 5 - defining a function
def greet(name):
    print("Hello " + name)
#Task 6 - combining concepts

