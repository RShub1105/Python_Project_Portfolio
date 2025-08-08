#make a student class attribute:name,marks check pass and fail.
class Student:
    def __init__(self,Name,Marks):
        self.name = Name
        self.marks = Marks
    def Check_marks(self):
        if self.marks >= 40:
            print(f"{self.name} has passed with {self.marks} marks.")
        else:
            print(f"{self.name} has Failed with {self.marks} marks.")

# child =[
    # Student("Rahul",100),
    # Student("prashant",80),
    # Student("bera",70),
    # Student("Aliesa",60),
    # Student("vishal",35)
    # ]
# for student in child:
    # student.Check_marks()
 
    #    