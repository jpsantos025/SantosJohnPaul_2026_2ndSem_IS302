class Person:
    def __init__(self, jps_full_name, jps_years_old):
        self.jps_full_name = jps_full_name
        self.jps_years_old = jps_years_old


class Student(Person):
    def __init__(self, jps_full_name, jps_years_old, jps_program):
        super().__init__(jps_full_name, jps_years_old)
        self.jps_program = jps_program

    def display_student(self):
        print("Name:", self.jps_full_name)
        print("Age:", self.jps_years_old)
        print("Course:", self.jps_program)


# example usage
jps_student1 = Student("Pedro Arabo", 20, "BSIS")
jps_student1.display_student()

#JohnPaulSantos
