install.packages("pROC")
library(pROC)
library(rpart)

df <- read.csv("C:/Users/Andrew/Desktop/train.csv")
dftest <- read.csv("C:/Users/Andrew/Desktop/testReport.csv")

# Generate new column for all observations where target = true
a <- rep(0, nrow(df))
a[which(df$TARGET == "TRUE")] <- 1
df$TRUES <- a

#Split dataframe into training and testing data
a <- sample(c(1:nrow(df)), size = nrow(df) * 0.7, replace = FALSE)
train <- df[a,]
test <- df[-a,]

#Grow tree
#rpart command generates tree
#"~" separates what is to be predicted, the output (Target), from the input (Beds, Baths, Lot.size)
RP1 <- rpart(TARGET ~ BEDS + BATHS + LOT.SIZE, data=train, control = rpart.control(minsplit = 15, cp = 1e-04))  

#Make prediction from test split
Pred1 <- predict(RP1, test[, c("BEDS","BATHS","LOT.SIZE")])
test$Prediction1 <- Pred1  

#Generate roc curve to examine accuracy
ROC1 <- roc(test$TRUES, test$Prediction1)  
plot(ROC1, col = "blue")

#Calculate auc
auc1 <- auc(ROC1)
auc1

#Display the results of decision tree
printcp(RP1)
#visualize cross-validation results
plotcp(RP1)
#Detailed summary of splits
summary(RP1) 

#Plot tree
plot(RP1, uniform=TRUE, main="Classification Tree for TARGET")
text(RP1, use.n=TRUE, all=TRUE, cex=.8)

#Use test report to make new prediction
pred <- predict(RP1, newdata=dftest)
pred
