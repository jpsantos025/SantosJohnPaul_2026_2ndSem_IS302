class Employee:
    def __init__(self, jps_employee_name, jps_monthly_salary):
        self.jps_employee_name = jps_employee_name
        self.jps_monthly_salary = jps_monthly_salary


class Manager(Employee):
    def __init__(self, jps_employee_name, jps_monthly_salary, jps_division):
        super().__init__(jps_employee_name, jps_monthly_salary)
        self.jps_division = jps_division

    def display_manager(self):
        print("Name:", self.jps_employee_name)
        print("Salary:", self.jps_monthly_salary)
        print("Department:", self.jps_division)


# example usage
jps_manager1 = Manager("Pedro", 85000, "IT")
jps_manager1.display_manager()

#JohnPaulSantos