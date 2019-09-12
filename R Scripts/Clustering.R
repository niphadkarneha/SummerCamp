
# Clustering



library(readxl)
library(plyr)
library(ggplot2)
library(cluster)
library(factoextra)
library(mclust)
library(NbClust)



mydata <- read.csv("c:/Users/Andrew/Desktop/adult.data.csv", header=TRUE) #replace "c:\mydata\mydatafile.csv"





# Define data for easy analysis
# Dataset followed by column name
# Must be numerical/continuous variables
A <- mydata$Age   
E <- mydata$education.num

summary(A)
summary(E)


# Correlation matrix showing continuos variables
cm <- data.frame(A, E)
str(cm)
cor(cm)


# K cluster for Total # Age and Education
# Specify the number of clusers after the "x" in the code below starting with 'cl <-......"
# Kmeans can cluster with large dataset, no need for sampling

x <- cbind(A, E)
cl <- kmeans(x,3)

cl$cluster     # view cluster results

plot(A, E, col=cl$cluster, xlab="Age", ylab="Education", main="K-Means Clusters for Age \nand Years of Education", pch=20)
points(cl$centers, pch=4, lwd=2, col="blue")   # create a X to mark the center of each cluster


# Create a new column in the original dataset for cluster number for each obervation
dfclust <- cbind(mydata, cl$cluster)


# write .csv file with cluster output
# Change location below 
write.csv(dfclust, file = "C:/Users/aramlatc/Desktop/AdultData_ClusterResults.csv")



