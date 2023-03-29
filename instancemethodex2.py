class student:
    crs="python"
    def getstuddata(nand):
        nand.no = int(input("enter student number:"))
        nand.sname = input("enter student name:")
        nand.marks = float(input("enter student marks:"))
        nand.studdispstuddata()
    def studdispstuddata(nandu):
        print("student number is:{}".format(nandu.no))
        print("student name is:{}".format(nandu.sname))
        print("student marks is{}:".format(nandu.marks))
        print("course",nandu.crs)
        print("_" * 20)


# main program
s1 = student()
s2 = student()
print("content of s1 before adding=", s1.__dict__)
print("content of s2 before adding=", s2.__dict__)
print("_" * 30)
print("first student information")
s1.getstuddata()
print("second student information")
s2.getstuddata()
print("_" * 20)




