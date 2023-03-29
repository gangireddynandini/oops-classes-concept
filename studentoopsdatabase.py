import cx_Oracle
class student:
    def studdetail(self):
        self.sno=int(input("enter student numbr:"))
        self.sname=input("enter student name:")
        # marks of c
        while(True):
            self.c=int(input("enter of s1 marks:"))

            if(self.c<=100 and self.c>=0):
                break
        while (True):
            self.cpp = int(input("enter of s2 marks:"))
            if (self.cpp<= 100 and self.cpp >= 0):
                break
        while (True):
            self.py = int(input("enter of s3 marks:"))

            if (self.py <= 100 and self.py>= 0):
                break
    def compute(self):
        self.tot=self.c+self.cpp+self.py
        self.percent=(self.tot/300)*100
        if(self.c<=40) or (self.cpp<=40) or (self.py<=40):
            self.grade="fail"
        else:
            if (self.tot>=250) and (self.tot<=300):
                self.grade="Distinction"
            elif(self.tot >= 200) and (self.tot <=249):
                self.grade="first class"
            elif(self.tot >= 150) and (self.tot <= 199):
                self.grade="second clASS"
            elif(self.tot>=120) and (self.tot<=149):
                self.grade="third class"
    def savestuddat(self):
        con=cx_Oracle.connect("system/Nandu123@localhost/XE")
        cur=con.cursor()
        iq="insert into result values(%d,'%s',%d,%d,%d,%d,%d,'%s')"
        cur.execute(iq %(self.sno,self.sname,self.c,self.cpp,self.py,self.tot,self.percent,self.grade))
        con.commit()
        print("student record saved successfully")


s=student()
s.studdetail()
s.compute()
s.savestuddat()


