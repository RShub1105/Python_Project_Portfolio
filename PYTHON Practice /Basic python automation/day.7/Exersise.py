# Write a program to open a file. if it doesn't exist,print"file not found."
try:
    file=open("data.txt","r")
except FileNotFoundError:
        print("File Not found")
else:
      print(file.read())
      file.close()

# Ask a user for two number.Divide them safely.if denominartior is 0,handel it.
try:
      num = int(input("Enter the first number:"))
      nums = int(input("Enter the second number to divide the sum:"))
      print(num/nums)
except ValueError:
      print("Please enter the valid number!")
except ZeroDivisionError:
      print("The Number is not divisble by zero!")

# Write a funtion that accepts a list - if list is empty, raise an expection.
def check_list(my_list):
      if not my_list:
            raise Exception("list is empty")
      else:
            print("List has an element", my_list) 
            try:
                  check_list([])
            except Exception as e:
                  print("Error",e)

# Use try.. and expect to check if string input can be converted to integer. if not, show error.
while True:
    try:
        value= input("Enter the integer:")
        number = int(value)
        print("Thanku the number is :",number)
        break
    except ValueError:
          print("Please enter the number only!")
            