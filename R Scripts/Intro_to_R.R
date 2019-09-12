
# Try installing a package
install.packages("abc") # This will install the package "abc"

# Load the package --ABC-- to your workspace
library(abc) 

# Install the following packages (to be used in these lessons):
install.packages("foreign")
library(foreign)
install.packages("car")
install.packages("Hmisc")
install.packages("reshape")




# Mathematical operations
3+3
3*3
3/3
3^3
2+2+2+2
87/9
2 * 9 *10
2**2
2**3
2**4
2**5
2**6
c(1, 1) + c(1, 1)



##R calculation for square root
sqrt(3)



# Assigning variables
x <- 56
print (x)

y <- 100
print (x+y)

x <- rnorm(10, mean=0, sd=1) # Creates 10 random numbers (normal dist.), syntax rnorm(n, mean, sd)
x
x <- data.frame(x) # stores the values of x as a dataframe, allows mathematical operations on all values in x


# Getting help
?plot # Get help for an object, in this case for the --plot- function. You can also type: help(plot)

??regression # Search the help pages for anything that has the word "regression". You can also type:
help.search("regression")

apropos("age") # Search the word "age" in the objects available in the current R session.

help(package=car) # View documentation in package 'car'. You can also type: library(help="car")

help(DataABC) # Access codebook for a dataset called 'DataABC' in the package ABC

args(log) # Description of the command.







