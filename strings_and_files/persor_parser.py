import datetime


class Test:
    def __init__(self):
        self.publiczne, self._chronione, self.__prywatne = 1, 2, 3
def main():
    test = Test()
    print(test.publiczne)
    print(test._chronione)
    print(test._Test__prywatne)
if __name__ == "__main__":
    main()


class Student:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,newname):
        self._name = newname

student = Student("dawid")
print(student._name)


class Student:
    _schoolName = 'XYZ School'  # protected class attribute
    students = 0
    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute
        Student.students += 1

x = datetime.date.today() - datetime.date.fromisocalendar(2001, 11, 1)
print(x)

student = Student("Dawid", 1)
student2 = Student("Patryk", 2)
student3 = Student("Patryk", 3)
student3.students = 0
print(Student.students)
print(student3.students)


class StudentChild(Student):

    def __init__(self, name, age, grade=[]):
        super().__init__(name, age)
        if grade is None:
            grade = []
        self.grade = grade

stud = StudentChild(1, "x")
print(stud.grade.append(1))
stud2 = StudentChild(1, "x")
print(stud2.grade)


class Student:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newname):
        self.__name = newname


student0 = Student("Dawid")
student0.name = 1
print(student0.__name)


class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

