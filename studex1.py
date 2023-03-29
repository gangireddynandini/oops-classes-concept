class student:pass
#main program
s1=student()
s2=student()
print("content of s1 before reading the data{} and number of values {}".format(s1.__dict__,len(s1.__dict__)))
print("content of s1 before reading the data={} and number of values {}".format(s2.__dict__,len(s2.__dict__)))
print("_"*20)
print("_"*20)
#add instance data members to s1
s1.sno=10
s1.name="rs"
s1.marks=22.22
print("content of s1 after adding the data={} and number of values{}".format(s1.__dict__,len(s1.__dict__)))
s2.stno=20
s2.name="Nandu"
s2.marks=42.67
print("content of s2 after adding the data={} and number of values={}".format(s2.__dict__,len(s2.__dict__)))




