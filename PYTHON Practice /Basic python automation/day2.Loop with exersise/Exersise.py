# (print all number from 1-n)

n = int(input("Enter the number="))
for i in range (1,n+1):
 print(i)  

# (print all even number from 1 to N)

num = int(input ("enter the number="))
for i in range (1,num+1): 
  if i % 2 == 0:
   print(i) 

# (print the multiplication table of a number) 

numb= int(input("enter the number to print the multiplication number="))
print ( f"\n Multiplication for the = {numb}  ")  
for i in range(1,11):
 print (f"{numb}* {i} = {numb*i}") 

 # (calculate the factorial number using for loop)
  
nu= int(input("enter the number to calculate the factorial = "))
factorial= 1 
step = []
for i in range(1, nu+1):
 factorial*=i
 step.append(str(i))
 step_str = "*" .join(step)
 print(f"The factorial {nu}!={nu}*{step_str} = {factorial}")


#(print star using nested loop)

Row=int(input("Enter the number of rows="))
for i in range(1,Row+1):
    for j in range(i):
     print("*",end='') 
    print()