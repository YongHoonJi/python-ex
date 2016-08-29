'''
Created on 2016. 8. 29.

@author: YonghoonJi
'''
'''
syntax
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
'''
class Parent:
    parentAttr = 100
    def __init__(self):
        print("calling parent constructor")
    
    def parentMethod(self):
        print('calling parent method')
    
    def setAttr(self, attr):
        Parent.parentAttr = attr
        
    def getAttr(self):
        print('Parent attribute :', Parent.parentAttr)
        
    def myMethod(self):
        print('calling parent method - override')
        
class Child(Parent):#define child class
    def __init__(self):
        print('calling child constructor')
        
    def childMethod(self):
        print('calling child method')
        
    def myMethod(self):
        print('calling child method - override')

''' inheritance test code'''
c = Child() #instance of Child
c.childMethod()
c.parentMethod()
c.setAttr(20)
c.getAttr()
''' overriding test '''
c.myMethod()

''' overriding operator
http://blog.eairship.kr/287
 '''
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   # 기본 함수에 대한 오버라이딩으로 벡터의 계산 (plus에 대한 연산이 이루어짐)
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
  
   def __sub__(self,other):
      return Vector(self.a - other.a, self.b - other.b)  

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
print (v1 - v2)

''' 
data hiding
: use underscore prefix (__) 
'''
class HidingValue:
    __hiddenScore = 0
    
    def count(self):
        self.__hiddenScore += 1
        print(self.__hiddenScore)
        
counter = HidingValue()
counter.count()
counter.count()
