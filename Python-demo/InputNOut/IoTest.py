'''
Created on 2016. 8. 25.

@author: YonghoonJi
'''
import os

''' input args from console '''
''''x=input("something:")'''
'''print(x)'''  

''' file open '''
''' file object = open(file_name [, access_mode][, buffering]) '''
fo = open("test.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()

''' write something to file '''
# Open a file
fo = open("test.txt", "w")
fo.write("I wrote something serious.")
fo.close();

''' read content from a file '''
fo = open("test.txt", "r+")
str = fo.read()
print("read string is ", str)
fo.close()

''' make a directory by using os module '''
os.mkdir("test")
''' change directory '''
'''os.chdir("path") '''