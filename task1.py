'''
A prime number is a number that is only evenly divisble by itself and 1.
For example, the number 5 is prime because it can only be evenlly divided by 1
and 5. The number 6, however, is not prime because it can be divided evenly
by 2 and 3.

Write a Boolean function named is_prime which takes an integer as an argument
and returns true if the argument is a prime number, or false otherwise. 

Then write a program that generates six random number between 1 and 100 (inclusive) and print out the result like the following (each run will have six different random numbers):
The random number 87 is a not a prime number.
The random number 23 is a prime number.
The random number 34 is a not a prime number.
The random number 96 is a not prime number.
The random number 6 is a not a prime number.
The random number 11 is a prime number.
'''

# Import Libraries
import random

# Function to see whether number inputted is prime
def is_prime(integer):
    for num in range(1,integer + 1):
        if num == 1 or num == integer:
            continue
        else:
            if integer % num == 0:
                return False
    return True

# Function to generate 6 random numbers and use is_prime function  
def generate_six():
    for _ in range(6):
        x =  random.randint(1,100)
        if is_prime(x):
            print(f'The random number {x} is a prime number.')
        else:
            print(f'The random number {x} is not a prime number.')

# Initiate generate 6 function
generate_six()