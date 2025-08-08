from cars import car
from Calculator import calculator
from student import Student
# take car.
car1 = car("TATA",2024)
car2 = car("suzuki", 2024)
car1.Disply_info()
car2.Disply_info()

# calculator.
calcu = calculator()
print(calcu.add(5,3))
print(calcu.subtract(7,4))

# student.
child =[
     Student("Rahul",100),
     Student("prashant",80),
     Student("bera",70),
     Student("Aliesa",60),
     Student("vishal",35)
]
for student in child:
     student.Check_marks()
   
