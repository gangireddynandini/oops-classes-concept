class student:
    @classmethod
    def getcourse(cls):

        cls.crs="python"
    @classmethod
    def getdeveloper(Nandu):
        Nandu.developer="rossum"
s1=student()
s2=student()
s1.getcourse()
student.getdeveloper()
print(student.crs,s1.developer)
print(s2.crs,student.developer)


