class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def introduce(self):
        text = "My name is {} and I am {} years old."
        return text.format(self._name, self._age)


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self._student_id = student_id

    def introduce(self):
        text = "My name is {}, I am {}, my student ID is {}."
        return text.format(self._name, self._age, self._student_id)


def run():
    p = Person("Ilyas", 33)
    s = Student("Amina", 19, "CS-2403")

    print(p.introduce())
    print(s.introduce())


run()
