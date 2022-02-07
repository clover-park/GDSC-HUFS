#혼공파 08-1 클래스의 기본

#from msilib.schema import SelfReg


class Student:
    def __init__(self, name, korean, english, math, science):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.science = science

    def sum(self):
        return self.korean+self.math+\
        self.english+self.science

    def average(self):
        return self.sum()/4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.sum(),self.average())

student_list = [
Student("monica",100,100,100,100),
Student("ross",97,54,87,100),
Student("rachel",65,43,69,73),
Student("joey",75,42,75,12),
Student("phoebe",64,88,92,92)
    ]

print("이름", "총점", "평균",sep='\t')
for student in student_list:
    print(student.to_string())