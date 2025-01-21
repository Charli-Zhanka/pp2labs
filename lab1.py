#CASTING-EX
#1
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#COMMENTS-EX
#1
#This is a comment
print("Hello, World!")

#2
print("Hello, World!") #This is a comment
#3
#print("Hello, World!")
print("Cheers, Mate!")
#4
#This is a comment
#written in
#more than just one line
print("Hello, World!")
#5
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#DATATYPES-EX
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)#	range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)#	bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray

#DATATYPES
#1
x = 5
print(type(x))
#int

#2
x = "Hello World"
print(type(x))
#str

#3
x = 20.5
print(type(x))
#float

#4
x = ["apple", "banana", "cherry"]
print(type(x))
#list

#5
x = ("apple", "banana", "cherry")
print(type(x))
#tuple

#6
x = {"name" : "John", "age" : 36}
print(type(x))
#dict

#7
x = True
print(type(x))
#bool
#EXAMPLES
#syntax error
#1
if 5 > 2:
    print("Five is greater than two!")
#2
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
    print("Five is greater than two!") 
    
    #comments
#3
#print("Hello, World!")
print("Cheers, Mate!")
 
   #Variable
   #4
x = str(3)    
y = int(3)    
z = float(3)
 #5
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#6

x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

#numbers
#7
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#8
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#string

#9
a="qwerty1234"
print(a)

#10
a = "Hello, World!"
print(a.upper())
#11
a = "Hello, World!"
print(a.lower())
#NUMBERS-EX
#1
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#2
print(type(x))
print(type(y))
print(type(z))
#3
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
#4
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#5
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#NUMBERS
#1
x = 5
x = float(x)

#2
x = 5.5
x = int(x)

#3
x = 5
x = complex(x)
#STRING-EX
#1.1
print("Hello")
print('Hello')
#1.2
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#1.3
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#2.1
b = "Hello, World!"
print(b[2:5])
#2.2
b = "Hello, World!"
print(b[:5])
#2.3
b = "Hello, World!"
print(b[2:])
#2.4
b = "Hello, World!"
print(b[-5:-2])
#3.1
a = "Hello, World!"
print(a.upper())
#3.2
a = "Hello, World!"
print(a.lower())
#3.3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#4.1
a = "Hello"
b = "World"
c = a + b
print(c)
#4.2
a = "Hello"
b = "World"
c = a + b
print(c)
#5.1
age = 36
txt = "My name is John, I am " + age
print(txt)
#5.2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#6.1
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#STRINGS
#1
x = "Hello World"
print(x)

#2
txt = "Hello World"
x = txt[0]

#3
txt = "Hello World"
x = txt[2:5]

#4
txt = "Hello World"
x = txt.strip()

#5
txt = "Hello World"
txt =txt.upper()

#6
txt = "Hello World"
txt=txt.lower()

#7
txt = "Hello World"
txt=txt.replace("H","J")

#8
age=36
txt = "My name is John, and I am {}"
print(txt.format(age))
#SYNTAX-EX
#1
if 5 > 2:
  print("Five is greater than two!")
  
#2
#Syntax Error:

if 5 > 2:
    print("Five is greater than two!")

#3
if 5 > 2:
     print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
#4
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")
#5
x = 5
y = "Hello, World!"
#SYNTAX
#1.1
print("Hello world")
#2.1
if 5>2 :
    print("Yes")

#VARIABLES-EX
#GLOBAL
#1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


myfunc()

print("Python is " + x)
#4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#MULTIPLE-VALUES
#1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#2
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#OUTPUT
#1
x = "Python is awesome"
print(x)
#2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#4
x = 5
y = 10
print(x + y)
#5
x = 5
y = "John"
print(x + y)
#6
x = 5
y = "John"
print(x, y)
#names.py
#1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#variables.py
#1
x = 5
y = "John"
print(x)
print(y)

#2
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#3
x = 5
y = "John"
print(type(x))
print(type(y))

#4
x = "John"
# is the same as
x = 'John'

#5
a = 4
A = "Sally"
#A will not overwrite a
#VARIBLES
#1.1
carname ="Volva"
#1.2
x=50
#1.3
x=5
y=10
print(x+y)
#1.4
x=5
y=10
z=x+y
print(z)
#1.5
x ,y, z = "Orange", "Banana", "Cherry"
#1.6
x = y = z = "Orange"
#1.7
def myfunc():
    global   x
    x = "fantastic"
    