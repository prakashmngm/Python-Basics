class Student:
    def __init__(self,name,age,marks):
        self.student_name = name
        self.student_age = age
        self.student_marks = marks
    def printDatavariables(self):
        print(self.student_name,self.student_age,self.student_marks)
    def passOrFail(self):
        if(self.student_marks > 40):
            print(self.student_name+' passed the exam')
        else:
            print(self.student_name+' failed the exam')
        
student1 = Student('lokesh',30,10)

student1 = Student('prakash',27,50)
print(student1.student_marks)

student1.printDatavariables()
student1.passOrFail()

student2 = Student('surya',29,50)
student2.printDatavariables()
student2.passOrFail()



'''
print(id(student1))
print(id(student2))

student2 = student1
student2.student_age = 100

student2.printDatavariables()
'''



    
