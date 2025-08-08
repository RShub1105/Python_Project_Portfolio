#Create a dictinary with your personal information.
User = {
    "Name":"Rahul",
    "Age" : 26,
    "city": "JSR",
    "Skills" : "Python",

}
print(User["Name"])
print(User["Age"])
print(User["city"])
print(User["Skills"])
print (User) 

#Ask the user for 3 product and there price.store them in a dictionary and print them
Products = {}
for i in range(3):
    name = input(f"Enter the product{i+1}:")
    price = float(input(f"Enter the price of the {name}:"))
Products[name] = price 
print("\nProduct List:")
for Product,Price in Products.items():
 print(f"{Product}:${price:.2f}")

#Create a list of 10 numbers with duplicate.Convert it into a set and print unique number.
Unique_nums = {1,2,3,4,4,6,3,7,9,5}
print(Unique_nums)
Unique_nums.add(10)
print(Unique_nums)

#create a dictionary of the students and there grades.Loop and print student who passed (grade_>40)
Students = {
   "Raj":55,
   "rahul":95,
   "priya":70,
   "diana":38,
   "bob":32
} 
print("Student who has passed")
for name , grade in Students.items():
   if grade>=40:
      print(f"{name}: {grade}") 

# use a set to find a common element between two lists.
a= [1,2,3,4,5]
b= [4,5,6,7,8]

common = set(a) & set(b)
print("common elemnt", common)
