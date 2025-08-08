#Create list from 5 favorite movies and print each one.

movies=("I","x","cars","TZP","r-one")
for n in movies:
 print(n)

#Ask the user for 5 number and store them in a list. print the list.

Num= []
for i in range(5):
  num=float(input(f"Enter the number{i+1}="))
  Num.append(num)
  print("The list of number is = ",Num)

 #print only even number from the loop.

Numbs=[1,2,3,4,5,6,7,8,9]

for numbe in Numbs:
  if numbe % 2 == 0:
   print(numbe)

#create a tuple of 5 colors and print them using loops

colors= ("red","green","blue","orange","black")
for color in colors:
  print (color) 

#reversel list

my_list =[1,2,3,4]
reversed_lsit=[]

for rev in range(len(my_list)-1,-1,-1):
  reversed_lsit.append(my_list[rev])
  print(reversed_lsit) 