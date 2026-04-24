class Employee:
    def __init__(self, jps_employee_name):
        self.__jps_employee_name = jps_employee_name
        self.__jps_monthly_pay = 0

    def set_salary(self, jps_pay_amount):
        if jps_pay_amount > 0:
            self.__jps_monthly_pay = jps_pay_amount

    def get_salary(self):
        return self.__jps_monthly_pay


# example usage
jps_emp1 = Employee("Ana")
jps_emp1.set_salary(30000)

print("Salary:", jps_emp1.get_salary())

#JohnPaulSantos