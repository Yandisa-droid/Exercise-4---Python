# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["banana","apple","pear","orange","tomato"]
# TODO: Use a for loop to print each fruit in the list
for x in fruits:
    print(fruits)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown
count = 5
# TODO: Use a while loop to create a countdown from 5 to 1
while count >0:
    print(count)
    count-=1  

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for num in range(2,22 ,2):
    print(num)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ["pink","red","blue","black","yellow"]
# TODO: Use a for loop to select and print 3 random colors from the list
colours = ["pink", "red","blue", "black", "yellow"]
random.colours = random.sample(colours,3)
for colours in colours:
    print(random.colours)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operation

print(math_operation.add(5,5))
print(math_operation.subtract(5,5))
print(math_operation.multiply(5,5))
print(math_operation.divide(5,5))

# TODO: Use a while loop to create a simple calculator
from math_operation import add, subtract, multiply, divide

while True:
    operator = input(" Enter operation: ")
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter first number"))

    if operator =="+":
        print(add(num1, num2))
        break

    elif operator == "-":
        print(subtract(num1, num2))
        break

    elif operator =="*":
        print(multiply(num1, num2))
        break

    elif operator == "/":
        print(divide(num1, num2))
        break