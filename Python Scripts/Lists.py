# Lists

# A list can hold any kind of value
list1 = ['physics', 'chemistry', 1997, 2000] 
print (list1)

list2 = [1, 2, 3, 4, 5 ]
print (list2)

list3 = ["a", "b", "c", "d"] 
print (list3)

list4 = []
print (list4)


# Access elements in a list
list1 = ['physics', 'chemistry', 1997, 2000]; 
list2 = [1, 2, 3, 4, 5, 6, 7 ]; 

print ("list1[0]: ", list1[0])  # show the first value
print ("list2[1:5]: ", list2[1:5])  # show the second - fourth values


# Traversing a list
values = [32, 54, 67.5, 29, 35, 80, 115, 44.5, 100, 65 ]
for i in range(10):
	print(i, values[i])


# Reverse order
values = [32, 54, 67.5, 29, 35, 80, 115, 44.5, 100, 65 ]
print(values[-2]) # show the value two steps away from the end


# Updating elements in list
list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ") 
print (list[2]) 
list[2] = 2001 
print ("New value available at index 2 : ") 
print (list[2]) 


# Adding elements to a list
friends = []        # new list with no values
friends.append("Harry")     # add Harry to empty list
friends.append("Emily")
friends.append("Bob")
friends.append("Cari")
print (friends)


# Inserting elements 
friends.insert(1, "Cindy")  # make Cindy the second person in the list
friends.insert(5, "Bill")   
print (friends)



# Finding an element
if "Cindy" in friends:
	print("She’s a friend")


# Remove an element
friends.pop(1)      # remove by index location
friends.remove("Emily")         # remove by value
print (friends)



# Concatenation and Replication
myFriends = ["Fritz", "Cindy"]
yourFriends = ["Lee", "Pat", "Bob"]

ourFriends = myFriends + yourFriends
print(ourFriends)


# Slicing a list
values = [32, 54, 67.5, 29, 35, 80, 115, 44.5, 100, 65]

part = values[3:6]
print (part)

part = values[:6]
print (part)

part = values[5:]
print (part)


# List of lists
rows = 4
cols = 3

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12]]

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end=" ")
    print(" ")









