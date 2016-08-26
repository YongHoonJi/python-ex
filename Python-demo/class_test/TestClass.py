'''
Created on 2016. 8. 26.
@author: YonghoonJi
'''
from class_test.CustClass import Employee
#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

''' is and getter and setter '''
print(hasattr(emp1, 'salary'))    # Returns true if 'salary' attribute exists
print(getattr(emp1, 'salary'))    # Returns value of 'salary' attribute
setattr(emp1, 'salary', 7000) # Set attribute 'salary' at 7000
print(getattr(emp1, 'salary'))
delattr(emp1, 'salary')    # Delete attribute 'salary'

'''reflection'''
emp1.displayReflective()

''' inheritance
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite 
'''


