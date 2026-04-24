# student_private.py

class Student:
    def __init__(self, jps_full_name, jps_student_number, jps_gpa_value):
        # private attributes
        self.__jps_full_name = jps_full_name
        self.__jps_student_number = jps_student_number
        self.__jps_gpa_value = jps_gpa_value

    def get_student_info(self):
        print("Name:", self.__jps_full_name)
        print("Student ID:", self.__jps_student_number)
        print("GPA:", self.__jps_gpa_value)


# example usage
jps_student1 = Student("Pedro Arabo", "2023-001", 1.75)

jps_student1.get_student_info()

#JohnPaulSantos