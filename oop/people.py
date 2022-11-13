# Refactor Student class,
# take care of access modifier
# use setter/properties
# add data validation
# add possibility to clear grades list


import datetime

class Person:

    def __init__(self, name, surname, year_of_birth):
        self.__name = name
        self._surname = surname
        self.__year_of_birth = year_of_birth

    def print_full_name(self):
        print(f"{self.__name} {self.surname}")
        # print("{} {}".format(self.name, self.surname))
        # print(self.name + " " + self.surname)

    def get_age(self):
        return datetime.date.today().year - self.__year_of_birth

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname


class Student(Person):

    grades = []

    def __init__(self, name, surname, year_of_birth, grades=None):
        super().__init__(name, surname, year_of_birth)
        if grades is not None:
            self.grades = grades
        else:
            self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.grades.append(grade)

    def get_average(self):
        return sum(self.grades)/len(self.grades)

    def clear_grades(self):
        self.grades = []


stefan = Student("Stefa", "Przpadek", 1999, [1, 2])
stefan.add_grade(3)
stefan.add_grade(4)
print(stefan.get_average())

#stefan2 = Student("Stefa", "Przpadek", 1999)
print(Student.grades)








class Car:

    _turn_on = False
    __vin = "xyz"

    def __init__(self, model):
        self.model = model

    @property
    def turn_on(self):
        return self._turn_on

    @turn_on.setter
    def turn_on(self, state):
        self._turn_on = state


my_car = Car("Fiat")

print(my_car.turn_on)
my_car.turn_on = True
print(my_car.turn_on)
# print(my_car.__vin)
#print(my_car._Car__vin)







class Truck(Car):

    def __init__(self, engine, model):
        super().__init__(model)
        self.engine = engine
