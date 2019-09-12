# Decision Tree

# "party" package = Aka "A laboratory for recursive partitioning"
# Details avialable here: https://cran.r-project.org/web/packages/party/party.pdf

install.packages("party")
library(party)

# This module will use a built-in dataset on reading skills. It will be used to determine if a person is a native speaker based on
# the variables: age, reading score, and shoe size

# View first few records from dataset
print(head(readingSkills)) 

# Create the input data frame.
inputdata <- readingSkills[c(1:105),]

# Create a chart with a chart file a name to visualize results
png(file = "decision_tree.png")

# Create the tree using "ctree" command, to predict "nativeSpeaker", based on everything after "~" symbol
Decision.tree <- ctree(nativeSpeaker ~ age + shoeSize + score, data = inputdata)

# View details of tree input and output
Decision.tree

# Visualize the tree
plot(Decision.tree)

# Save the file
dev.off()