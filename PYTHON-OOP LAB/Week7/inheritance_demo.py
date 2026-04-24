class Animal:
    def __init__(self, jps_animal_name):
        self.jps_animal_name = jps_animal_name

    def speak(self):
        print(self.jps_animal_name, "makes a sound")


class Cow(Animal):
    def moo(self):
        print(self.jps_animal_name, "Moo")


# example usage
jps_cow1 = Cow("Bessie")
jps_cow1.speak()
jps_cow1.moo()

#JohnPaulSantos