# Intro to Python


# The PRINT statement
print("text")
print("Hello, world!")
print("")         
print("Suppose two swallows \"carry\" it together.")
print('African or "European" swallows?')



# Mathematical operations
2+2
50 - 5*6
(50 - 5*6) / 4
8 / 5  # division always returns a floating point number
17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # result * divisor + remainder



# Variables
print ("Subtotal:")
print (38 + 40 + 30)

print ("Tax:")
print ((38 + 40 + 30) * .09)

print ("Tip:")
print ((38 + 40 + 30) * .15)

print ("Total:")
print (38 + 40 + 30 + (38 + 40 + 30) * .15 + (38 + 40 + 30) * .09)

# Use variables to simplify code
x = (38 + 40 + 30) # create a new variable for x to subsitute (38+40+30)
print (x)
print ("Subtotal:", x) # print the phrase "Subtotal" followed by the new variable value

tax = (x * .09) # create a new variable called "tax"
print ("Tax:", tax) #text strings are enclosed in "", values/variables are not

tip = (x * .15)
print ("Tip:", tip)

total = (x + tax + tip)
print ("Total:", total)



# Parameters
print(sqrt(25)) # This will generate an error message

from math import * # To use math commands, import the math library

print(sqrt(25))
print(sqrt(15 + 10 * 10 + 6))
x = 5
print(sqrt(x + sqrt(16)))




# INPUT statement
age = input("How old are you? ")
age = int(age) #convert text value to an integer
print("Your age is", age)
print("You have", 65 - age, "years until retirement")


# Exercise: write a program to convert temperature from Fahrenheit to Celsius. 
# The program should ask the user for input of a Fahrenheit value, which it will then convert to Celsius.
# Hint: formula is : c = ((f-32)*5)/9
 





