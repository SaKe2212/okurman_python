class BankAccount:
    def __init__(self, account_number, initial_balance):
         self.account_number = account_number,
         self.initial_balance = initial_balance,



    def deposit(self,  amount):
        if amount > 0:
            self.balance += amount,
            print(f" Вы {amount}  пополнили баланс")
            print(f" Ваш баланс на нынешний момент {self.balance} В рублях")
        else:
            amount < 0
            print("«Вы не можете добавить 0, даже если можете».")



    @property
    def balance(self, balance):
         return self.__balance


    @balance.setter
    def balance(self, balance):
        self.__balance = balance
        print(f" Ваш баланс на нынешний момент {self._balance} В рублях")




    def withdraw(self, balance):
        if balance > 0:
            print(int(input().split()(" Ведите сууму которую хотите вывести")))
        else:
            balance < 1
            print(" Вы не можете выести сууму менше 1 ")


































































































































































