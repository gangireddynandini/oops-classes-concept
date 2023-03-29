class student:
    @classmethod
    def getcourse(cls):
        cls.crs="python"
        cls.getdeveloper("rossum")
    @classmethod
    def getdeveloper(cls,dname):
        cls.developer=dname

    def getstuddetails(self,sno,sname,marks):
        self.snum=sno
        self.name = sname
        self.marks = marks
    def dispstuddata(self):
        print("student number is:{}".format(self.snum))
        print("student name is:{}".format(self.name))
        print("student marks={}".format(self.marks))
        print("student course={}".format(self.crs))
        print("student develper={}".format(self.developer))

s1=student()
s2=student()
s1.getstuddetails(10,"rs",67)
s2.getstuddetails(20,"tr",98)
s1.getcourse()
s1.dispstuddata()
s2.dispstuddata()