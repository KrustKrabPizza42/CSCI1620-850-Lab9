# Parent Class
class Account():

    def __init__(self, name, balance=0):

        self.__account_name = name

        self.set_balance(balance)


    def deposit(self, amount):

        if amount > 0:

            self.set_balance(self.get_balance() + amount)

            return True
        
        return False
    

    def withdraw(self, amount):

        if amount <= self.get_balance() and amount > 0:

            self.set_balance(self.get_balance() - amount)

            return True
        
        return False
    

    def get_balance(self):

        return self.__account_balance
    
    def get_name(self):

        return self.__account_name

    def set_balance(self, value):

        if value < 0:

            self.__account_balance = 0

        else:
            
            self.__account_balance = value

    def set_name(self, value):

        self.__account_name = value

    def __str__(self):

        return f'Account Name = {self.get_name()}, Account Ballance = ${self.get_balance():0.2f}'
    
class SavingAccount(Account):

    MINIMUM = 100

    RATE = 0.02

    def __init__(self, name):

        super().__init__(name, self.MINIMUM)

        self.__deposit_count = 0

    def apply_interest(self):

        if self.__deposit_count % 5 == 0:

           super().deposit(super().get_balance() * 0.02)

    def deposit(self, amount):

        if super().deposit(amount):
    
            self.__deposit_count += 1

            self.apply_interest()
            
            return True
        
        return False
    
    def withdraw(self, amount):

        if self.get_balance() - amount >= 100:    

            return super().withdraw(amount)
        
        else:
            return False
    
    def get_balance(self):

        return super().get_balance()
    
    def get_name(self):

        return super().get_name()
    
    def set_balance(self, value):

        if value >= self.MINIMUM:

            super().set_balance(value)
        
        else:

            super().set_balance(self.MINIMUM)
    
    def set_name(self, value):

        super().set_name(value)

    def __str__(self):

        return f'Savings Account: Account Name = {self.get_name()}, Account Balance = ${self.get_balance():0.2f}'


    

