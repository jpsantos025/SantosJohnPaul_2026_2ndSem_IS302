class Person:
    def __init__(self, jps_full_name, jps_age_value):
        self.jps_full_name = jps_full_name
        self.jps_age_value = jps_age_value

    def display_info(self):
        print("Name:", self.jps_full_name)
        print("Age:", self.jps_age_value)


class Student(Person):
    def __init__(self, jps_full_name, jps_age_value, jps_enrolled_course):
        super().__init__(jps_full_name, jps_age_value)
        self.jps_enrolled_course = jps_enrolled_course

    def display_info(self):
        print("Name:", self.jps_full_name)
        print("Age:", self.jps_age_value)
        print("Course:", self.jps_enrolled_course)


class Teacher(Person):
    def __init__(self, jps_full_name, jps_age_value, jps_assigned_subject):
        super().__init__(jps_full_name, jps_age_value)
        self.jps_assigned_subject = jps_assigned_subject

    def display_info(self):
        print("Name:", self.jps_full_name)
        print("Age:", self.jps_age_value)
        print("Subject:", self.jps_assigned_subject)


# example usage
jps_student1 = Student("Pedro", 20, "BSIS")
jps_teacher1 = Teacher("Mr. Minchin", 40, "Programming")

print("Student Info:")
jps_student1.display_info()

print("\nTeacher Info:")
jps_teacher1.display_info()

#JohnPaulSantos