# Functions
# 1 print
# can change separator with sep=
# can change the end (default \n, with end = )

# 2 help to give doc on functions
# can be used with created functions

# 3 range
# by default, range(x) will go up to the value x without going up to it

# 4 map
# apply a function to iterated objects
# can be used with custom functions
# often used map(lambda x: x + "s")

# 5 filter
# related to map
# take all items in iterable object. Will keep item if function is true

# 6 sum
# will return the sum
# can paramater with start value

# 7 sorted
# sort iterable object in ascending or descending order
# parameter reverse to reverse order
# can pass key of dictionnary to sort (example, age)

# 8 enumerate
# using for loops, when we want to use the index as well as the value

# 9 zip
# when indexes of two lists don't match
# will automatically handle different lengths of lists
# useful when corresponding values in multiple lists

# 10 open
# open("filename", "file mode")
# r for read
# w for overwrite, will overwrite the file
# a for append
# need to close file after opening 
# Better to use 
# with open("filename", "w") as file:
    #file.write("eee")
# will close automatically even if error occurs

