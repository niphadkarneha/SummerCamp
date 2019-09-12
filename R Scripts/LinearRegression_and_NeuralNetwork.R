
# Machine Learning with Regression
# Comparison of a Linear Model with an Articial Neural Network


# Upload the Boston dataset 
# Load the neuralnet package

library(neuralnet)
library(MASS)
data <- Boston

# Create a linear model (LM) to predict the house value variable (medv)
index <- sample(1:nrow(data),round(0.75*nrow(data)))  #take a sample of 75 percent of the data
train <- data[index,]   # create a training set from the data
test <- data[-index,]   # create a testing set from the data
lm.fit <- glm(medv~., data=train) # initial a linear model
summary(lm.fit)   # summary of results
pr.lm <- predict(lm.fit,test)   # make prediction from linear model
MSE.lm <- sum((pr.lm - test$medv)^2)/nrow(test)   #MSE is mean squared error, will be used to measure accuracy


# Now create Artificial Neural Network (NN)

# Before creating a neural network to compare to the above linear model
# the data must be normalized. This means that the data must be converted to a scale
# in a range from 0 to 1
maxs <- apply(data, 2, max) 
mins <- apply(data, 2, min)
scaled <- as.data.frame(scale(data, center = mins, scale = maxs - mins))

train_nn <- scaled[index,]    # create a training set from the scaled data
test_nn <- scaled[-index,]    # create a testing set from the scaled data

# Initiate neural network. Will predict "medv" (the median house value in Boston) using all other variables
n <- names(train_nn)
f <- as.formula(paste("medv ~", paste(n[!n %in% "medv"], collapse = " + "))) # creates a formula to insert into the nn algorithm
nn <- neuralnet(f, data=train_nn, hidden=c(5,3),linear.output=T)

# Notes:
# function "neuralnet" above uses the input followed by output, then arguments
# hidden = number of layers separated by comma and number of neurons in each
# linear output = depends on if a linear model is necessary




# Plot a diagram of the NN
plot(nn)

# The black lines show the connections between each layer and the weights on each connection, which 
# calculates how important that node is for the next layer



# Make prediction with test data
pr.nn <- compute(nn,test_nn[,1:13])

pr.nn_ <- pr.nn$net.result*(max(data$medv)-min(data$medv))+min(data$medv)
test.r <- (test_nn$medv)*(max(data$medv)-min(data$medv))+min(data$medv)

MSE.nn <- sum((test.r - pr.nn_)^2)/nrow(test_nn)


# Comparison of the MSE (mean squared error) of the LM compared to the NN
print(paste(MSE.lm,MSE.nn))

par(mfrow=c(1,2)) # view 2 plots side by side to compare

# Plot of the real value compared to the neural network predicted value
plot(test$medv,pr.nn_,col='red',main='Real vs Predicted by NN',xlab = "Real Amount", ylab = "NN Predicted Amount", pch=18,cex=0.7)
abline(0,1,lwd=2)
legend('bottomright',legend='NN',pch=18,col='red', bty='n')

# Plot of real amount vs. linear model amount
plot(test$medv,pr.lm,col='blue',main='Real vs predicted LM',xlab = "Real Amount", ylab = "LM Predicted Amount", pch=18, cex=0.7)
abline(0,1,lwd=2)
legend('bottomright',legend='LM',pch=18,col='blue', bty='n', cex=.95)

# Plot of real amount vs. nn predicted amount with linear model values overlayed on top
plot(test$medv,pr.nn_,col='red',main='Real vs predicted NN', xlab = "Real Amount", ylab = "Predicted Amount", pch=18,cex=0.7)
points(test$medv,pr.lm,col='blue',pch=18,cex=0.7)
abline(0,1,lwd=2)
legend('bottomright',legend=c('NN','LM'),pch=18,col=c('red','blue'))

