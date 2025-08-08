#Define a simple funtion.
def greet():
    print("Hello RS welocome to python!")
    
    greet()

# Funtion and Arrgument.
def Welcome(name):
    print("Hello",name,"Your are amazing")
    
    Welcome("RS")

# Funtion with return.
def add(a,b):
 return a+b
result=add(9,7)
print("Sum is", result)

#defult parameter.
def say_Hello(Name="friend"):
   print("Hi",Name)

say_Hello()
say_Hello("RS")

# Funtion to check the prime number.

def is_prime(n):
   if n<=1:
      return False
   for i in range(2,n):
      if n%1==0:
         return False
      return True
   print(n(7)) 