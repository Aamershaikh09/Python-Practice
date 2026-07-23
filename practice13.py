# oops

class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("constructor")
        
    def hello(self):
        print("hello",self.name)

    def get_marks(self):
        print(self.marks)
    
   

s1=Student("Sumit",65)
print(s1.name,s1.marks)
s1.hello()
s1.get_marks()

s2=Student("Aamer",83)
print(s2.name,s2.marks)