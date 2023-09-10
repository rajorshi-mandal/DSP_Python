#Day 3

#Introduction to python tuples,dictionary,conditional checking,loops

print("1 : Containers : Tuples,Dictionaries \n2 : Conditional checking and loops","\n")

print("//Tuple//")
T = (1,2.3,"RCCIIT")  #initialising a tuple
print(type(T))

print(T[1])
print(T[-1])
print(T[-1][0:3])
print(T[-1][-1:-4:-1])
print(type(T[-1]))
print(T,"\n")

#for only one element the type of the container becomes the element type
#To get tuple we have to add a ","
T = ("RCCIIT")
print("For only one element in tuple : ",type(T),"\n")

#Dictionary
print("//Dictionary//")
RCCIIT = {"Dept" : ["ECE","CSE","IT","EE"], "STD" : [120,210,120,60]}
print(type(RCCIIT))
print("Departments : {}".format(RCCIIT["Dept"]))
print("Total students in each department : {}".format(RCCIIT["STD"]))
print(type(RCCIIT["Dept"]))
print(type(RCCIIT["Dept"][-2]),"\n")

#To know all the keys in the created dictionary
print(RCCIIT.keys(),"\n")

#Converting to other containers using type casting
print("Dictionary typecast to list : ",list(RCCIIT.keys()))
print("Dictionary typecast to tuple : ",tuple(RCCIIT.keys()),"\n")

print("//Condition checking(using boolean)//")
#Condition checkings with boolean
var1 = True
var2 = False

var3 = var1 and var2
print(type(var1),type(var2))
print(var3,"\n")

x = 2
y = 3
z = x == y
print(z)

w = not var2
print(w,"\n")

print("//using if-else//")
#Condition checking with if-else
age = 20
if age >= 18:
    print("You are eligible to vote")
else:
    print("You aren't elegible to vote")

a = 10
b = 20
c = 30

print("//using elif//")
#elif condition
if a > b and b > c:
    print("Max value is {}".format(a))
elif b > a and a > c:
    print(" Max value is {}".format(b))
else:
    print("Max value is {}".format(c))
print("\n")

#Loops
#for
print("//for loop//")
for i in range(5):
    print(i,"-> RCCIIT")
print("\n")
for j in range(0,10,2):
    print(j)
print("\n")

#functions
#Here is the syntax of defining a function in python

print("//function//")
def func_name(var1 = 100,var2 = 200):
    if var1 > var2:
        print("var1 is greater than var2")
        return "first condition was executed"
    elif var1 < var2:
        print("var1 is lesser than var2")
        return "second condition was executed"
    else:
        print("Both are equal !!")
        return "last condition was executed"
#print("\n")
print(func_name()) #Since, no arguments are passed the parameters will be used
print(func_name(200))   #for only one argument the first parameter will be modified by default
print(func_name(var2 = 80)) #this specifically modifies the variable passed (here it is the second parameter in function)
