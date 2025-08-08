Name = input("Enter the name =")
print(f"Hello {Name} welcome to python industry")

#(loop from 1-10)

for i in  range(1,11): 
    print(i) 


#(sum of first N number )

n= int(input("Enter a number"))
total = 0
for i in range(1,n+1):
 total +=i
print("SUM =", total) 

# (whileloop count till 5)

i = 1
while i<=5:
   print(i)
   i +=1

#(break on finding a number)

for i in range(1,11):
   if i==6:
      print("Found 6, breaking loop")
      break
   print(i)

#(continue to skip even number)

 
for i in range(1,11):
   if i %2 ==0 :
      continue
   print(i)