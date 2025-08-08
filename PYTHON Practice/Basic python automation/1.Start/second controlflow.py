# (print the number is even or odd )

num= int(input("Enter a number ="))
if num % 2 == 0: 
    print("Even")
else:
    print("odd") 


#(take 3 number and give the greatest one)

a = int(input("Enter the first number ="))
b = int(input("Enter the second number ="))
c = int(input("Enter the third number ="))
if a >= b and a >= c :
   print("Greatest number is =", a)
elif b >= c:
   print("Greast number is =",b)
else:
   print("Greatest number is =",c ) 


# (grading system)

marks = int(input("Enter the marks ="))
if marks >= 90:
   print("Grade A")
elif marks >= 75: 
   print("Grade B")
elif marks >= 60:
   print("Grade C")
elif marks >= 40:
   print("Grade D")
else: 
   print ("Grade F(Fail)") 

#(voter elgibility) 

Age = int(input("Enter your Age ="))
if Age >= 18:
   print("You are eligeble for vote")
else:
   print("You are not eligeble for vote")

# (login system)
 
Correct_username = 'UserID'
Correct_password = '12345'

Username = input("Username =")
Password = input("password =")
if  Correct_username == Username and Correct_password == Password :
 print("Login sucessfully") 
else:
   print("invalid userid or password")


   # (check if the year is leap or not)
 
Year = int(input("Enter your Year ="))
if (Year % 4 == 0 and Year % 100 !=0) or (Year % 400 == 0):
   print(f"{Year} is a leap year.")
else:
   print(f"{Year} is not a leap year.")
   