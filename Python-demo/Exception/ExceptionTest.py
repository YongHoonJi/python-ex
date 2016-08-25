'''
Created on 2016. 8. 25.

@author: YonghoonJi
'''

''' assertion : assert Expression[, Arguments] '''
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
#print (KelvinToFahrenheit(-5))

''' Exception '''
fh = open("test.txt", "r")
try:
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
finally:
   fh.close()
   
''' finally '''
try:
    fh = open("test.txt", "w")
    fh.write("this is for test finally statement.")
finally:
    print("error: can't find the file.")
    fh.close()
    
''' raise an exception '''
def raiseException( level ):
    if level <1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level

raiseException(-1)

''' user exception '''