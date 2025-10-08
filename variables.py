# Demonstrate how variables are created and how they work.
# Author: Timea Croucamp
# Date: 08/10/2025
# Version 1.0

# Different types of variables
# Store a tring
greeting = "Hello World!"
print(greeting)

name = "Timea"

# Store a number
my_number = 80 # assigned 80 to the variable called my_number
print(my_number)

my_number2 = 7
print (my_number)
# Assign the value of one variable to another
my_number = greeting
print(my_number) # Don't assign values to virables that don't make sense

'''Do calculations with variables and store the result
in another variable. I can now 
press enter
as many times
as
I
like'''

# Creating new variable
num_1 = 5
num_2 = 18 

sum1 = 5 + 18 # This is not good practice.
print(sum1)

sum1 = num_1 + num_2
print(sum1) # This is better practice

sum_string1 = "18"
sum_string2 = "5"

# Adding two strings together. This is called concatenation
sum = sum_string1 + sum_string2
print(sum)

# Print formatting. f stands for 'format' and insert the value of variables into the curly brackets
print(f"My calculation for adding {num_1} and {num_2} together is {sum1}.")
print("My calculation for adding {} and {} together is {}.".format(num_1, num_2))

# Greet someone
print ("Kia ora, my name is", name )
print (f"Kia ora, my name is {name}.")
print("Kia ora, my name is {} ".format(name))
