# Load library
library(knitr)


##R list of integers
a <- c(1:9)
a

##R list of objects 
b <- c(1,3,8,12)
b

##Repeating string, number of times
mylist <- rep("R is so cool", 5)
mylist


##THIS IS AWESOME - it pulls up code for you
?matrix

## Create a matrix using variable "a" above
A <- matrix(a,ncol=3,byrow=TRUE)
A

## Convert "A" to dataframe called "mynames"
mydata <- data.frame(A)
names(mydata) <- c("Col1", "Col2", "Col3")
mydata

## Creating a mathematical function
myfunction <- function(x) {
  x <- x + 1
  x
}
myresult <- myfunction(a) # Apply "myfunction" to the values held by "A"
myresult # View results of mathematical operation on "A"

## Load senicData - replace directory below with location of file
mydata <- read.csv("c:/Users/Andrew/Desktop/SENIC.csv", header=TRUE) #replace "c:\mydata\mydatafile.csv"


head(mydata) # View top rows of senicData

##Drop 2 columns
mydata <- mydata[,-ncol(mydata)]
head(mydata)





# Exploring data
summary(mydata) # Provides basic descriptive statistics and frequencies

edit(mydata) # Open data editor

str(mydata) # Provides the structure of the dataset

names(mydata) # Lists variables in the dataset

head(mydata) # First 6 rows of dataset

head(mydata, n=10)# First 10 rows of dataset

head(mydata, n= -10) # All rows but the last 10

tail(mydata) # Last 6 rows

tail(mydata, n=10) # Last 10 rows

tail(mydata, n= -10) # All rows but the first 10

mydata[1:10, ] # First 10 rows

mydata[1:10,1:3] # First 10 rows of data of the first 3 variables


# Exploring the workspace
objects() # Lists the objects in the workspace

ls() # Same as objects()

remove() # Remove objects from the workspace

rm(list=ls()) #clearing memory space

detach(package:ABC) # Detached packages when no longer need them

search() # Shows the loaded packages

library() # Shows the installed packages

dir() # show files in the working directory






## Load adultData - replace directory below with location of file
adultData <- read.table("adult.data.csv", header=TRUE, sep=",",
                        colClasses = c("numeric", "factor",
                                       "numeric", "factor", "numeric", rep("factor",5),
                                       rep("numeric",3), rep("factor",2)), na.strings=" ?")
head(adultData)

## Output data to a new file - replace directory below with location of file
write.csv(adultData, file="adultDataClean.csv")
