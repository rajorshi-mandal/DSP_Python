#Day2 

#Learning about Python containers (List)

#List = In Python, a list is a versatile and widely used data structure that allows you to store a collection of items, such as numbers, strings, or even other objects. Lists are ordered, mutable (which means you can change their contents), and can contain elements of different data types.

L = [1, 'A', "RCCIIT", 15.54, [10,30]]    #using [10,30] shows python supports nested lists too and all types of data in a single list

print(L[0:3])  #Python takes upto one less than the final index value

#we are using slicing technique of Python
print(L[-1:-2:-1])     #Forcing to iterate with negative indexes
print(L[4][1])         #Accessing element thourgh nested list
print("List length is : {}".format(len(L)))

print(L[2][3:6])    #Here we are performing slicing in the string of the list's 3rd element
print(L[2][-1:-4:-1])
print(L[2][-3:6])   #Using both positive and negatives indexes for accessing list elements
print(type(L))
