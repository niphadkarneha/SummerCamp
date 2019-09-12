# Branches and Loops

# IF statements
gpa = 3.4
if gpa > 2.0:
    print ("Your application is accepted.") # indent for if statement condition

# IF statement with user input
gpa = input("What is your GPA?")
gpa = float(gpa) # use FLOAT to allow decimal places
if gpa > 2.0:
    print ("Your application is accepted.") # indent for if statement condition




# IF/ELSE statements
gpa = 1.4
if gpa > 2.0:
    print ("Welcome to Mars University!")
else:
    print ("Your application is denied.")
    
# Excersise: Rewrite the program below so that if the user 
# input age less than 0, print out “illegal age” and if the user 
# input age greater than 65, print out “you have already retired”.

age = input("How old are you? ")
age = int(age)
print("Your age is", age)
print("You have", 65 - age, "years until retirement")





# The FOR loop
for x in range(1, 6):
    print (x, "squared is", x * x)



# The RANGE function      
for x in range(5, 0, -1):
   (print (x))
print ("Blastoff!")    



# Cumulative loops
sum = 0
for i in range(1, 11):
   sum = sum + (i * i)
print("sum of first 10 squares is", sum)



# The BREAK statement
for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1:  # If the number is odd
       break        #  ... immediately exit the loop
    print(i)
print("done")



# The CONTINUE statement
for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 1:      # If the number is odd
       continue         # Don't process it
    print(i)
print("done")




# The WHILE statement
number = 1
while number < 200:
    print (number), 
    number = number * 2













