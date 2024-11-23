class Person:
    def __init__(self, name, age, city, gender, eatVar):
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
        self.eatVar = eatVar
    def __str__(self):
        return f"name: {self.name}\nage: {self.age}\ncity: {self.city}\ngender: {self.gender}"

    def eat(self):
        if self.gender.lower() == "male":
            print(f"     {self.name} can eat more.")
        else:
            print(f"     {self.name} can eat less.")

    def study(self):
        if self.gender.lower() == "male":
            print(f"     {self.name} can study Medicine.")
        else:
            print(f"     {self.name} can study Math.")

    def sleep(self):
        if self.gender.lower() == "male":
            print(f"     {self.name} can sleep less.")
        else:
            print(f"     {self.name} can sleep longer.")

    def play(self):
        if self.gender.lower() == "male":
            print(f"     {self.name} can play soccer.")
        else:
            print(f"     {self.name} can play tennis.")

employee = Person("John", 35, "Delhi", "male", "more")
student = Person("Dessy", 20, "Pune", "female", "less")

print(employee)
employee.eat()
employee.study()
employee.sleep()
employee.play()

print("\n" + "-"*30 + "\n")

print(student)
student.eat()
student.study()
student.sleep()
student.play()