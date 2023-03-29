class student:
    @classmethod
    def getcourse(cls):
        cls.crs="python"
        cls.getdeveloper()
    @classmethod
    def getdeveloper(Nandu):
        student.dev="rossum"
s1=student()
s2=student()
s1.getcourse()
print(student.crs,s1.dev)
print(s2.crs,student.dev)


