import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',passwd='root')
print('type of conn=',type(con))
print("python program obtains connecion from mysql")



#Program for storing sno,sname ,marks in an object of Programmer-defined class #StudEx1.py-
---Instance Data members class Student:pass #main program s1=Student() s2=Student()
print("Content of s1 before adding the data={} and Number of values={}".format(s1.__dict__,
len(s1.__dict__))) print("Content of s2 before adding the data={} and Number of values=
{}".format(s2.__dict__, len(s2.__dict__))) print("-"*50) #add Instance Data Members to s1
s1.sno=10 s1.name="RS" s1.marks=22.22 print("Content of s1 after adding the data={} and
Number of values={}".format(s1.__dict__, len(s1.__dict__))) #add Instance Data Members to s2
s2.stno=20 s2.sname="TR" s2.smarks=42.22 print("Content of s2 after adding the data={} and
Number of values={}".format(s2.__dict__, len(s2.__dict__)))