# while loop

count = 1
while (count <= 3):
    print("Hello Geek")
    count = count + 1

# for loop
# iterating over a list

print("List Iteration:")
l = ["geeks","for","geeks"]
for i in l:
    print(i)

# iterating over a tuple

print("Tuple Iteration:")
t = ("geeks","for","geeks")
t = t + ("is",)
for i in t:
    print(i)

# iterating over a String

print("String Iteration:")
s = "geeks"
for i in s:
    print(i)

# iterating by index

print("Iterating by Index:")
index = ["geeks","for","geeks"]
for i in range(len(index)):
    print (index[i])

# Prints all letters except 'e' and 's'

print ("Continue Statement:")
for letter in s:
    if letter == 'e' or letter == 's':
        continue
    print ("Current Letter:",letter)

# Prints all letters except 'e' and 's'

print ("Break Statement:")
for letter in s:
    if letter == 'e' or letter == 's':
        break
    print ("Current Letter:",letter)

# Functions

# Creating a function
def my_function(fname):
    print(fname + "Refsnes")

# Calling a function
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Function with default parameter

def my_function(country = "Norway"):
    print("I am from",country)

my_function("Sweden")
my_function()
my_function("South Korea")

# Passing list as parameter

def my_function(f):
    for i in f:
        print("Fruit:",i)

fruits = ["Apple","Banana","Cherry","Strawberry"]
my_function(fruits)

# Function with Return Values

def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(5))
print(my_function("Table"))

# Keyword Arguments

def my_function(child3,child2,child1):
    print("The youngest child is",child3)
    print("The youngest child is",child1)
    print("The youngest child is",child2)

my_function(child1 = "Emil",child2 = "Tobias",child3 = "Linus")

# Classes/Objects

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello my Name is",self.name)

print("Class and Object:")
p1 = Person("John",23)
p1.my_function()
print(p1.age)

p2 = Person("Aliya",20)
p2.my_function()
print(p2.age)

# Insertion Sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

arr = [5,3,4,1,2]
insertion_sort(arr)
print(arr)


    



