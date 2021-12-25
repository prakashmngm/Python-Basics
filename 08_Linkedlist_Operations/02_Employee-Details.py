'''
Create an Employee class with 3 instance variables : name, age, salary, workExp
And  method 1: printEmployeeDetails()
And method 2 : salary > 50000 , workExp > 5 , MotorBike
               salary > 30000-50000 , workExp = 3-5 , TV
               rest all cases , Bicycle
               
'''

class Employee:
    def __init__(self,name,age,salary,workExp,NewyearGift = None):
        self.emp_name = name
        self.emp_age = age
        self.emp_salary = salary
        self.emp_workExp = workExp
        self.emp_newyearGift = NewyearGift
    def printEmployeeDetails(self):
        print(self.emp_name,self.emp_age,self.emp_salary,self.emp_workExp,self.emp_newyearGift)
    def employeeNewyearGift(self):
        if(self.emp_salary > 50000 and self.emp_workExp > 5):
            self.emp_newyearGift = 'MotorBike'
        elif(self.emp_salary > 30000 and self.emp_salary <= 50000 and self.emp_workExp >3 and self.emp_workExp <= 5):
            self.emp_newyearGift = 'TV'
        else:
            self.emp_newyearGift = 'Bicycle'
        
emp1 = Employee('lokesh',30,90000,7)
emp2 = Employee('surya',28,50000,5)
emp3 = Employee('suresh',29,30000,5)
emp4 = Employee('ramesh',27,40000,4)
emp5 = Employee('krishna',26,35000,3)

emp_list = [emp1,emp2,emp3,emp4,emp5]

motorbike_list = []
tv_list = []
bicycle_list = []

for obj in emp_list:
    obj.employeeNewyearGift()
    obj.printEmployeeDetails()
for obj in emp_list:
    if(obj.emp_newyearGift == 'MotorBike'):
        motorbike_list.append(obj.emp_name)
    elif(obj.emp_newyearGift == 'TV'):
        tv_list.append(obj.emp_name)
    else:
        bicycle_list.append(obj.emp_name)
print(motorbike_list,tv_list,bicycle_list)


