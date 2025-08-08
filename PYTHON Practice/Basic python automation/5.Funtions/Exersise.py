# Write a funtion that takes a list of numbers and return the sum
def sums(Num):
  return sum(Num)
my_list=input("Enter the number list:")

number_list= [float(numb.strip())for numb in my_list.split()]
result= sums(number_list)
print("The sum is:",result)


#WAF for calculate the rectangel area (L*B)
def calculate_rectangle_area(L,B):
    area = L * B 
    return area

L= float(input("Enter the length of the rectangle:"))
B= float(input("Enter the Breath of the rectangle:"))
area=calculate_rectangle_area(L,B) 
print(f"The area of rectangle is: {area}") 

#WAF that take a string and return how many vowel its have. 
def count_vowels(s):
 vowels="aieouAIEOU"
 count=0
 for char in s:
   if char in vowels:
     count+=1
 return count
text = input("Enter any name character:")
print("Number the Vowels",count_vowels(text)) 

#Create a calculator funtion that perfoms +,-,*,%.
def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  return x%y
a=int(input("Give first number :"))
b=int(input("Give second number :"))

print("Addition",add(a,b))
print ("Substracte", sub(a,b))
print ("Multiplication", mul(a,b))
print ("Division",div(a,b)) 

#create a funtion that accept the list of numbers and retur the largest one.
def large_num(Numbers):
  if not Numbers:
    return None
  largest=Numbers[0]
  for Numbs in Numbers:
    if Numbs  > largest:
      largest=Numbs
      return largest
Numbers_lsit=[93,92]
print(large_num(Numbers_lsit))

#WAF that takes student's marks and print the grades(A/B/C/D/F).
def mark_students(marks1,marks2):
  average= (marks1+marks2)/2
  if average >= 90:
    Grade = "A"
  elif average >= 80:
    Grade = "B"
  elif average >= 70:
    Grade = "C"
  elif average >= 60:
    Grade = "D"
  else:
    Grade = "F"
    print(f"Average{average},Grade:{Grade}")
    