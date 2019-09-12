# Strings

'spam eggs'  # single quotes

'doesn\'t'  # use \' to escape the single quote

"doesn't"  # ...or use double quotes instead

'"Yes," he said.'

"\"Yes,\" he said."

'"Isn\'t," she said.'

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)  # with print(), \n produces a new line







# If you don’t want characters prefaced by \ to be interpreted as special characters, 
# you can use raw strings by adding an r before the first quote

print('C:\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote








# Triple-quotes: 
""" to span multiple lines
stuff
more stuff 
even more stuff

"""







# Repeat using *
# Concatenation using +

3 * 'un' + 'ium'








# Indexing strings 
word = 'Python'

word[0]  # character in position 0

word[5]  # character in position 5

# Negative index starts counting from the right

word[-1]  # last character

word[-2]  # second-last character

word[-6]





# Slicing gives a substring
word[0:2]  # characters from position 0 (included) to 2 (excluded) 'Py'
word[2:5]  # characters from position 2 (included) to 5 (excluded) 'tho'

#An omitted first index defaults to zero
#An omitted second index defaults to the size of the string
word[:2]   # character from the beginning to position 2 (excluded)

word[4:]   # characters from position 4 (included) to the end

word[-2:]  # characters from the second-last (included) to the end




