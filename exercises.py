def calculate_area_triangle(base, height):
    return (base * height) / 2

print('Exercise 1:', calculate_area_triangle(7, 3))

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print('Exercise 2:', simple_interest(1000, 5, 2))

def apply_discount(price, discount):
    return price - (price * discount / 100)

print('Exercise 3:', apply_discount(100, 25))


def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9 / 5) + 32
    return (temperature - 32) * 5 / 9


print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


def sum_to(n):
    return sum(range(1, n + 1))


print('Exercise 5:', sum_to(6))

def largest(first, second, third):
    return max(first, second, third)


print('Exercise 6:', largest(1, 2, 3))

def calculate_tip(bill, percentage):
    return bill * percentage / 100


print('Exercise 7:', calculate_tip(50, 20))
# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.

def product(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print('Exercise 8:', product(2, 5, 5))
# Exercise 9: Basic Calculator
#
# Create a function named `basic_calculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basic_calculator(10, 5, 'subtract') should return 5.
# basic_calculator(10, 5, 'add') should return 15.
# basic_calculator(10, 5, 'multiply') should return 50.
# basic_calculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.

def basic_calculator(first, second, operation):
    if operation == 'add':
        return first + second
    if operation == 'subtract':
        return first - second
    if operation == 'multiply':
        return first * second
    if operation == 'divide':
        return first / second


print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
