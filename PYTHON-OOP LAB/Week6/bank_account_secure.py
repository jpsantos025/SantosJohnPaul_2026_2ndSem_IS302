class BankAccount:
    def __init__(self, jps_starting_amount):
        self.__jps_current_balance = jps_starting_amount

    def deposit(self, jps_cash_in):
        self.__jps_current_balance += jps_cash_in

    def withdraw(self, jps_cash_out):
        if jps_cash_out <= self.__jps_current_balance:
            self.__jps_current_balance -= jps_cash_out
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__jps_current_balance


# example usage
jps_account1 = BankAccount(5000)
jps_account1.deposit(1000)
jps_account1.withdraw(2000)

print("Balance:", jps_account1.get_balance())

#JohnPaulSantos