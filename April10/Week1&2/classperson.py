class Person:

    def __init__(self, full_name, person_age):
        self._full_name = full_name
        self._person_age = person_age

    def display_info(self):
        return f"Name: {self._full_name}, Age: {self._person_age}"


student_profile = Person("Robert", 22)

print(student_profile.display_info())