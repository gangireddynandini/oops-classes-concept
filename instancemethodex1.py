class student:
        def getstuddata(s1):
            s1.no = int(input("enter student number:"))
            s1.sname = input("enter student name:")
            s1.marks = float(input("enter student marks:"))
        def studdispstuddata(nandu):
            print("student number is:{}".format(nandu.no))
            print("student name is:{}".format(nandu.sname))
            print("student marks is{}:".format(nandu.marks))
            print("_"*20)

#main program
s1=student()
s2=student()
print("content of s1 before adding=",s1.__dict__)
print("content of s2 before adding=",s2.__dict__)
print("_"*30)
print("first student information")
s1.getstuddata()
print("second student information")
s2.getstuddata()
print("_"*20)
print("displaying the first stud detais")
s1.studdispstuddata()
print("displaying the second student details")
s2.studdispstuddata()



