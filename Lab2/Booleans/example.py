#2
a = 200
b = 33
if b > a:
    print("b is greater than a") 
else:
    print("b is not greater than a")  #b is not greater than a

#3
print(bool("Hello")) #True
print(bool(15))  #True

#4
x = "Hello"
y = 15
print(bool(x)) #True
print(bool(y)) #True

#5
bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True

#6
bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False

#7
class myclass():
      def __len__(self):
          return 0

myobj = myclass()
print(bool(myobj)) #False

#8
def myFunction() :
      return True

print(myFunction()) #True

#9
def myFunction() :
      return True

if myFunction():
  print("YES!")  #YES!
else:
  print("NO!") 
  
#10
x = 200
print(isinstance(x, int))  #True
