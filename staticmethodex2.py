class student:
    def getstud(self):#instance method
        self.sno=int(input("enter student number:"))
        self.sname=input("enter student name:")
        self.marks=int(input("enter marks:"))
        self.alldata(self,student)
    @staticmethod
    def alldata(nandu, hold):
        print("display the {} related data".format(hold))
        for a, b in nandu.__dict__.items():
            print("{}-->{}".format(a, b))
        print("-" * 30)
class employee:
    def employee(self):
        self.eno=int(input("enter employee number:"))
        self.ename=input("enter employee name:")
        self.sal=int(input("enter employee salary:"))
        student.alldata(self, employee)
class teacher:
    def teacher(self):
        self.tno=int(input("enter teacher number:"))
        self.tname=input("enter teacher namme:")
        self.tsub=input("enter student subject:")
        student.alldata(self, teacher)


#main method
s=student()
e=employee()
t=teacher()
s.getstud()
e.employee()
t.teacher()




