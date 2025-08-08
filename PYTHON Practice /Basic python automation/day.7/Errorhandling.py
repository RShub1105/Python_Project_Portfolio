#Basic try and except.
try:
    num = int(input("Enter a number="))
    print(10/num)
except:
    print("oops something wents wrong.")

# specific error handling.
try: 
    num= int(input("Enter number:"))
    print(7/num)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("cannot divide by zero!")

# else and finally.
try:
    f=open("test.txt","r")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())
    f.close()
finally:
    print("This run no matter what.")

# Raising custome error.
age = int(input("Enter your age:"))
if age < 18:
 raise Exception("You must be atleast 18.")
else:
    print("Access Granted.")
