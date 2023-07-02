class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
    def result(self):
        if self.marks<=35:
            print(f'{self.name} Failed, He/she should read well for suplementary')
        elif self.marks>35 and self.marks<70:
            print(f'Congratulations !!! {self.name} have passed with good marks')
        else :
            print(f'Celebrations!!! {self.name} got Distinction')
students=[]
n=int(input('Enter no.of students : '))
for i in range(n):
    name=input('Enter student name for record : ')
    marks= int(input('Enter marks of the student : '))
    s=Student()
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
print()
print('*'*10+'Student Results'+'*'*10)
print()
for s in students:
    print('Student Name : ',s.getName())
    print('Student Marks : ',s.getMarks())
    s.result()
