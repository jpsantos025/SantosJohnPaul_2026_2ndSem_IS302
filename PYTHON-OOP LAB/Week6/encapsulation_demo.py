class Person:
    def __init__(self, jps_full_name, jps_years_old):
        # private attributes
        self.__jps_full_name = jps_full_name
        self.__jps_years_old = jps_years_old

    # getter method for name
    def get_name(self):
        return self.__jps_full_name

    # getter method for age
    def get_age(self):
        return self.__jps_years_old


# example usage
jps_person1 = Person("Pedro Arabo", 21)

print("Name:", jps_person1.get_name())
print("Age:", jps_person1.get_age())

#JohnPaulSantos