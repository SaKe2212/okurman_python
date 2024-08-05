
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Amount cannot be greater than balance.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


ob_1 = BankAccount('123')
ob_2 = BankAccount('456', 100)
#
#
# 1) deposit
# 2) withdraw
# 3) get balance
# 4) exit




people = []


def add_deposit(deposit):
    people.append(deposit)


def withdraw(name):
    if name not in people:
        print()
        print("Amount cannot be greater than balance.")
        print()
    else:
        people.remove(name)


def get_balance(self):
    return self.balance


def get_index(index):
    print()
    print(people[index - 1])
    print()




def main():
    while True:
        print("1) ")
        print("2) ")
        print("3) ")
        print("4) ")


        value = int(input("Выберите один вариант"))

        if value == 4:
            break
        elif value == 1:
            deposit = input("Enter name: ")
            add_deposit(person=deposit)
        elif value == 2:
            balance = input("Enter name: ")
            get_balance(name=balance)
        elif value == 3:
            withdraw(withdraw())
        elif value == 4:
            ind = int(input("Enter index: "))
            get_index(index=ind)









































































































ob_1.deposit(200)
ob_2.deposit(50)
print(ob_1.balance)
print(ob_2.balance)
ob_1.withdraw(100)
ob_2.withdraw(100)
print(ob_1.balance)
print(ob_2.balance)
ob_1.withdraw(200)
ob_2.withdraw(200)
print(ob_1.balance)
print(ob_2.balance)