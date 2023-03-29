class student:
    def getstud(self):#instance method
        self.sno=int(input("enter student number:"))
        self.sname=input("enter student name:")
        self.marks=int(input("enter marks:"))

    def employee(self):
        self.eno=int(input("enter employee number:"))
        self.ename=input("enter employee name:")
        self.sal=int(input("enter employee salary:"))

    def teacher(self):
        self.tno=int(input("enter teacher number:"))
        self.tname=input("enter teacher namme:")
        self.tsub=input("enter student subject:")
    @staticmethod
    def alldata(nandu,hold):
        print("display the {} related data".format(hold))
        for a,b in nandu.__dict__.items():
            print("{}-->{}".format(a,b))
        print("-"*30)
#main method
s=student()
empl=student()
teac=student()
a=student()
s.getstud()
empl.employee()
teac.teacher()
a.alldata(s,student)
a.alldata(empl,empl)
a.alldata(teac,teac)




